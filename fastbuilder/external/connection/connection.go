package connection

import (
	"crypto/ecdsa"
	"crypto/elliptic"
	"crypto/rand"
	"crypto/x509"
	"encoding/binary"
	"fmt"
	"io"
	"net"
	"sync"

	kcp "github.com/xtaci/kcp-go/v5"
)

// not stream, but ensure a frame is send/recv
type ReliableConnection interface {
	SendFrame([]byte) error
	RecvFrame() ([]byte, error)
	Close()
}

type ReliableConnectionServerHandler interface {
	Listen(address string) error
	SetOnNewConnection(func(ReliableConnection))
	SetOnAcceptNewConnectionFail(func(error))
	SetOnServerDown(func(interface{}))
}

type ConnectionServerHandler struct {
	onAcceptNewConnectionFail func(error)
	onNewConnection           func(ReliableConnection)
	OnNewKCPConnection        func(*kcp.UDPSession)
	onServerDown              func(interface{})
}

const (
	DATA_SHARDS   = 10
	PARITY_SHARDS = 3
	ENCRYPTION_ON = false
)

func (s *ConnectionServerHandler) Listen(address string) error {
	//listener, err := kcp.ListenWithOptions(address, nil, DATA_SHARDS, PARITY_SHARDS)
	listener, err := net.Listen("tcp", address)
	if err != nil {
		return fmt.Errorf("listen fail (err=%v)", err)
	}
	fmt.Println("listen @ address", err)
	go func() {
		defer func() {
			r := recover()
			s.onServerDown(r)
		}()
		for {
			proxyConn, err := listener.Accept()
			if err != nil {
				fmt.Printf("Transfer: accept new connection fail\n\t(err=%v)\n", err)
				if s.onAcceptNewConnectionFail != nil {
					s.onAcceptNewConnectionFail(err)
				}
				continue
			}
			remoteDescription := proxyConn.RemoteAddr().String()
			fmt.Printf("Transfer: accept new connection @ %v\n", remoteDescription)
			var chann ReliableConnection
			chann = &StreamChannelWrapper{reader: proxyConn, writer: proxyConn, writeLock: sync.Mutex{}}
			connectionCloser := func() {
				proxyConn.Close()
			}
			if ENCRYPTION_ON {
				encryptionConn := &EncryptedChannel{
					connection: chann,
					isInitator: false,
					closer:     connectionCloser,
				}
				if encryptionConn.Init() != nil {
					//fmt.Printf("Transfer: encryption init fail\n")
					s.onAcceptNewConnectionFail(fmt.Errorf("encryption init fail: %v", err))
					continue
				}
			}
			s.onNewConnection(chann)
		}

	}()
	return nil
}

func (s *ConnectionServerHandler) SetOnNewConnection(fn func(ReliableConnection)) {
	s.onNewConnection = fn
}
func (s *ConnectionServerHandler) SetOnAcceptNewConnectionFail(fn func(error)) {
	s.onAcceptNewConnectionFail = fn
}
func (s *ConnectionServerHandler) SetOnServerDown(fn func(r interface{})) {
	s.onServerDown = fn
}

func ClientDial(address string) (ReliableConnection, error) {
	//conn, err := kcp.DialWithOptions(address, nil, DATA_SHARDS, PARITY_SHARDS)
	conn, err := net.Dial("tcp", address)
	if err != nil {
		return nil, err
	}
	var chann ReliableConnection
	chann = &StreamChannelWrapper{reader: conn, writer: conn, writeLock: sync.Mutex{}}
	if ENCRYPTION_ON {
		encryptedConn := &EncryptedChannel{
			connection: chann,
			isInitator: true,
		}
		if err := encryptedConn.Init(); err != nil {
			return nil, err
		}
		chann = encryptedConn
	}
	return chann, nil
}

// Frame -> Stream -> Frame

type ByteReaderWrapper struct {
	reader io.Reader
	buf    []byte
}

func (brw *ByteReaderWrapper) ReadByte() (byte, error) {
	if brw.buf == nil {
		brw.buf = make([]byte, 1)
	}
	_, err := brw.reader.Read(brw.buf)
	if err != nil {
		return 0, err
	}
	return brw.buf[0], nil
}

type StreamChannelWrapper struct {
	reader    io.Reader
	writer    io.Writer
	isClosed  bool
	writeLock sync.Mutex
}

const MAX_STD_HEADER_LEN = 1 << 15

func (_ *StreamChannelWrapper) Close() {
	// Not exported
}

func (scw *StreamChannelWrapper) RecvFrame() ([]byte, error) {
	// get length info
	length := uint64(0)
	header2Byte := make([]byte, 2)
	n, err := scw.reader.Read(header2Byte)
	if err != nil || n != 2 {
		scw.isClosed = true
		return nil, err
	}
	shortLength := binary.LittleEndian.Uint16(header2Byte)
	if shortLength > MAX_STD_HEADER_LEN {
		// use var_uint (extend header)
		uvarint, err := binary.ReadUvarint(&ByteReaderWrapper{reader: scw.reader})
		if err != nil {
			scw.isClosed = true
			return nil, err
		}
		length = uvarint
	} else {
		// ok
		length = uint64(shortLength)
	}
	// fmt.Println(length)
	fullData := make([]byte, length)
	offset := uint64(0)
	for offset < length {
		n, err := scw.reader.Read(fullData[offset:])
		if err != nil {
			scw.isClosed = true
			return nil, err

		}
		offset += uint64(n)
	}
	return fullData, nil
}

func (scw *StreamChannelWrapper) SendFrame(data []byte) error {
	scw.writeLock.Lock()
	defer scw.writeLock.Unlock()
	length := len(data)
	headerBytes := make([]byte, binary.MaxVarintLen64+2) // 2 is the length of short(std) head
	headerBytesLen := 0
	if length > MAX_STD_HEADER_LEN {
		// mark it is followed by an varint (extend header)
		binary.LittleEndian.PutUint16(headerBytes, uint16(MAX_STD_HEADER_LEN+1))
		n := binary.PutUvarint(headerBytes[2:], uint64(length))
		headerBytesLen = n + 2
	} else {
		binary.LittleEndian.PutUint16(headerBytes, uint16(length))
		headerBytesLen = 2
	}
	offset := 0
	for offset < headerBytesLen {
		n, err := scw.writer.Write(headerBytes[offset:headerBytesLen])
		if err != nil {
			return err
		}
		offset += n
	}
	offset = 0
	for offset < length {
		n, err := scw.writer.Write(data[offset:])
		if err != nil {
			return err
		}
		offset += n
	}
	return nil
}

// encryption channel
type EncryptedChannel struct {
	connection ReliableConnection
	isInitator bool
	encryptor  *EncryptionSession
	isClosed   bool
	closer     func()
}

func (i *EncryptedChannel) Close() {
	i.isClosed = true
	i.closer()
}

func (i *EncryptedChannel) initiateEncryptSession() error {
	initiatorPrivateKey, _ := ecdsa.GenerateKey(elliptic.P384(), rand.Reader)
	salt := make([]byte, 16)
	rand.Read(salt)
	encodedInitiatorPublicKey, _ := x509.MarshalPKIXPublicKey(&initiatorPrivateKey.PublicKey)
	initPacket := append(append([]byte{0x04}, salt...), encodedInitiatorPublicKey...)
	err := i.connection.SendFrame([]byte(initPacket))
	if err != nil {
		return err
	}
	data, err := i.connection.RecvFrame()
	if err != nil {
		return fmt.Errorf("cannot get public key from responder: %v", err)
	}
	if data[0] != 0x03 {
		return fmt.Errorf("Got unexpected command %d when establishing an encrypted session", data[0])
	}
	responderPubKeyData, err := x509.ParsePKIXPublicKey(data[1:])
	if err != nil {
		return fmt.Errorf("error parsing public key: %v", err)
	}
	responderPublicKey := new(ecdsa.PublicKey)
	ecdsaKey, ok := responderPubKeyData.(*ecdsa.PublicKey)
	if !ok {
		return fmt.Errorf("expected ECDSA public key, but got %v", responderPubKeyData)
	}
	*responderPublicKey = *ecdsaKey
	i.encryptor = &EncryptionSession{PublicKey: responderPublicKey, PrivateKey: initiatorPrivateKey, Salt: salt}
	return i.encryptor.Init()
}

func (r *EncryptedChannel) waitForEncryptSession() error {
	initiatorPubkeyAndSaltData, err := r.connection.RecvFrame()
	if err != nil {
		return fmt.Errorf("cannot read data from Initiator: %v", err)
	}
	if initiatorPubkeyAndSaltData[0] != 0x04 {
		return fmt.Errorf("Unexcepted Packet ID %d received", initiatorPubkeyAndSaltData[0])
	}
	responderPrivateKey, _ := ecdsa.GenerateKey(elliptic.P384(), rand.Reader)
	encodedResponderPublicKey, _ := x509.MarshalPKIXPublicKey(&responderPrivateKey.PublicKey)
	err = r.connection.SendFrame(append([]byte{0x03}, encodedResponderPublicKey...))
	if err != nil {
		return err
	}
	peerSalt := initiatorPubkeyAndSaltData[1:17]
	peerPublicKey := initiatorPubkeyAndSaltData[17:]
	initiatorPublicKeyData, err := x509.ParsePKIXPublicKey(peerPublicKey)
	if err != nil {
		return fmt.Errorf("error parsing public key: %v", err)
	}
	initiatorPublicKey := new(ecdsa.PublicKey)
	ecdsaKey, ok := initiatorPublicKeyData.(*ecdsa.PublicKey)
	if !ok {
		return fmt.Errorf("expected ECDSA public key, but got %v", initiatorPublicKeyData)
	}
	*initiatorPublicKey = *ecdsaKey
	r.encryptor = &EncryptionSession{PublicKey: initiatorPublicKey, PrivateKey: responderPrivateKey, Salt: peerSalt}
	return r.encryptor.Init()
}

func (e *EncryptedChannel) Init() error {
	if e.isInitator {
		return e.initiateEncryptSession()
	} else {
		return e.waitForEncryptSession()
	}
}

func (e *EncryptedChannel) SendFrame(data []byte) error {
	encyptedData := data[:]
	e.encryptor.Encrypt(encyptedData)
	return e.connection.SendFrame(append([]byte{0x06}, encyptedData...))
}

func (e *EncryptedChannel) RecvFrame() ([]byte, error) {
	encryptedData, err := e.connection.RecvFrame()
	if err != nil {
		e.isClosed = true
		return nil, err
	}
	if encryptedData[0] != 0x06 {
		e.Close()
		return nil, fmt.Errorf("Data with unknown type %d incorrectly handled by EncryptedChannel.", encryptedData[0])
	}
	e.encryptor.Decrypt(encryptedData[1:])
	return encryptedData[1:], nil
}
