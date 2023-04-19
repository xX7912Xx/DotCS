// Example minecraft 1.15.2 server
package main

import (
	"github.com/Tnze/go-mc/net"
	pk "github.com/Tnze/go-mc/net/packet"
	"github.com/Tnze/go-mc/offline"
	"github.com/google/uuid"
	"log"
)

const ProtocolVersion = 578
const MaxPlayer = 200

// Packet IDs
const (
	PlayerPositionAndLookClientbound = 0x36
	JoinGame                         = 0x26
)

func main() {
	l, err := net.ListenMC(":25565")
	if err != nil {
		log.Fatalf("Listen error: %v", err)
	}

	for {
		conn, err := l.Accept()
		if err != nil {
			log.Fatalf("Accept error: %v", err)
		}
		go acceptConn(conn)
	}
}

func acceptConn(conn net.Conn) {
	defer conn.Close()
	// handshake
	protocol, intention, err := handshake(conn)
	if err != nil {
		log.Printf("Handshake error: %v", err)
		return
	}

	switch intention {
	default: //unknown error
		log.Printf("Unknown handshake intention: %v", intention)
	case 1: //for status
		acceptListPing(conn)
	case 2: //for login
		handlePlaying(conn, protocol)
	}
}

func handlePlaying(conn net.Conn, protocol int32) {
	// login, get player info
	info, err := acceptLogin(conn)
	if err != nil {
		log.Print("Login failed")
		return
	}

	// Write LoginSuccess packet

	if err = loginSuccess(conn, info.Name, info.UUID); err != nil {
		log.Print("Login failed on success")
		return
	}

	if err := joinGame(conn); err != nil {
		log.Print("Login failed on joinGame")
		return
	}
	if err := conn.WritePacket(pk.Marshal(PlayerPositionAndLookClientbound,
		// https://wiki.vg/index.php?title=Protocol&oldid=16067#Player_Position_And_Look_.28clientbound.29
		pk.Double(0), pk.Double(0), pk.Double(0), // XYZ
		pk.Float(0), pk.Float(0), // Yaw Pitch
		pk.Byte(0),   // flag
		pk.VarInt(0), // TP ID
	)); err != nil {
		log.Print("Login failed on sending PlayerPositionAndLookClientbound")
		return
	}
	// Just for block this goroutine. Keep the connection
	for {
		var p pk.Packet
		if err := conn.ReadPacket(&p); err != nil {
			log.Printf("ReadPacket error: %v", err)
			break
		}
		// KeepAlive packet is not handled, so client might
		// exit because of "time out".
	}
}

type PlayerInfo struct {
	Name    string
	UUID    uuid.UUID
	OPLevel int
}

// acceptLogin check player's account
func acceptLogin(conn net.Conn) (info PlayerInfo, err error) {
	//login start
	var p pk.Packet
	err = conn.ReadPacket(&p)
	if err != nil {
		return
	}

	err = p.Scan((*pk.String)(&info.Name)) //decode username as pk.String
	if err != nil {
		return
	}

	//auth
	const OnlineMode = false
	if OnlineMode {
		log.Panic("Not Implement")
	} else {
		// offline-mode UUID
		info.UUID = offline.NameToUUID(info.Name)
	}

	return
}

// handshake receive and parse Handshake packet
func handshake(conn net.Conn) (protocol, intention int32, err error) {
	var (
		p                   pk.Packet
		Protocol, Intention pk.VarInt
		ServerAddress       pk.String        // ignored
		ServerPort          pk.UnsignedShort // ignored
	)
	// receive handshake packet
	if err = conn.ReadPacket(&p); err != nil {
		return
	}
	err = p.Scan(&Protocol, &ServerAddress, &ServerPort, &Intention)
	return int32(Protocol), int32(Intention), err
}

// loginSuccess send LoginSuccess packet to client
func loginSuccess(conn net.Conn, name string, uuid uuid.UUID) error {
	return conn.WritePacket(pk.Marshal(0x02,
		pk.String(uuid.String()), //uuid as string with hyphens
		pk.String(name),
	))
}

func joinGame(conn net.Conn) error {
	return conn.WritePacket(pk.Marshal(JoinGame,
		pk.Int(0),                  // EntityID
		pk.UnsignedByte(1),         // Gamemode
		pk.Int(0),                  // Dimension
		pk.Long(0),                 // HashedSeed
		pk.UnsignedByte(MaxPlayer), // MaxPlayer
		pk.String("default"),       // LevelType
		pk.VarInt(15),              // View Distance
		pk.Boolean(false),          // Reduced Debug Info
		pk.Boolean(true),           // Enable respawn screen
	))
}
