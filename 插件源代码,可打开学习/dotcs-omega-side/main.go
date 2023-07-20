package main

import (
	"dotcs/environment"
	"dotcs/minecraft"
	"dotcs/minecraft/protocol/packet"
	"dotcs_mod/runcmd"
	"dotcs_mod/utils"
	_ "embed"
	"encoding/json"
	"fmt"
	"io"
	"io/ioutil"
	"log"
	"net"
	"net/http"
	"os"
	"strings"
	"sync"

	"github.com/gorilla/websocket"
	"github.com/pterm/pterm"
)

// 配置文件
var Title string = "dotcs-omega-side" // 插件名
var Version string = "0.1.0"          // 版本号
var Author string = "art,2401pt"      // 作者名,
var Sid string = "123123123"          // 组件id
var Aes_code string = ""              // 如果依然冒充了作者和版本号,那么这个数值就是特别重要的了。DotCS会进行双向加密,以正确验证版本号,作者,组件
var is_run bool = true                // 是否启动组件
//go:embed config.json
var ConfigBytes []byte

var Game_Function = &environment.Plugins{}

type OmegaSideProcessStartCmd struct {
	Name     string            `json:"旁加载功能名"`
	Cmd      string            `json:"启动指令"`
	Remapper map[string]string `json:"变更选项"`
}
type OmegaSide struct {
	PreferPort               string                     `json:"如果可以则使用这个http端口"`
	DebugServerOnly          bool                       `json:"只打开用于开发的Websocket端口而不启动任何插件"`
	EnableOmegaPythonRuntime bool                       `json:"使用Omega标准Python插件框架"`
	EnableDotCSSimulator     bool                       `json:"使用DotCS社区版插件运行模拟器"`
	PossiblePythonExecPath   []string                   `json:"python解释器搜索路径"`
	StartUpCmds              []OmegaSideProcessStartCmd `json:"启动其他旁加载程序的指令"`
	pythonPath               string
	closeCtx                 chan struct{}
	fileChange               bool
	FileName                 string `json:"玩家数据文件"`
	PlayerData               map[string]map[string]interface{}
	pushController           *pushController
}

var plugin_data OmegaSide

// 初始化
// golang 语言的初始化函数,DotCS 不会对其做任何处理
func init() {

}
func run_tip() {
	Println("OmegaSide旁加载兼容系统启动中")
	Println("OmegaSide原作者:2401pt")
	Println("本组件需要使用 DotCS Exp 或 DotCS Pro 才可运行,如果您的版本不是探索版或专业版,DotCS 有权封禁您的账户")
}

// 输出
func Println(a ...any) {
	pterm.Println(pterm.Yellow(pterm.Sprintf("[%s] %s", pterm.Green(Title)), fmt.Sprint(a)))
}

// 游戏内函数初始化
func Game_Init(game *environment.Plugins) bool {
	run_tip()
	bootstrapDirs()
	Game_Function = game

	err := json.Unmarshal(Load_profile(), &plugin_data)

	if err != nil {
		log.Fatal("解析组件配置文件错误: ", err)
	}
	if plugin_data.EnableOmegaPythonRuntime {
		plugin_data.StartUpCmds = append(plugin_data.StartUpCmds, OmegaSideProcessStartCmd{
			Name:     "Python",
			Cmd:      "[python] python_plugin_starter.py --server ws://[addr]/omega_side",
			Remapper: map[string]string{},
		})
	}
	if plugin_data.EnableDotCSSimulator {
		plugin_data.StartUpCmds = append(plugin_data.StartUpCmds, OmegaSideProcessStartCmd{
			Name:     "DotCS",
			Cmd:      "[python] dotcs_emulator.py --server ws://[addr]/omega_side",
			Remapper: map[string]string{},
		})
	}
	plugin_data.SideUp()
	return true
}
func (o *OmegaSide) SideUp() {
	handler := http.NewServeMux()
	handler.HandleFunc("/omega_side", o.handle)
	server := http.Server{Handler: handler}
	ln, err := net.Listen("tcp", o.PreferPort)
	if err != nil {
		pterm.Warning.Println("无法使用偏好端口 " + o.PreferPort)
		ln, err = net.Listen("tcp", "localhost:0")
		if err != nil {
			panic("无法打开一个有效端口供 Omega Side 使用")
		}
	}
	addr := ln.Addr().String()
	pterm.Success.Printfln("成功打开了位于 %v 的端口供 Omega Side 使用 (ws://%v/omega_side)", addr, addr)
	o.closeCtx = make(chan struct{})
	o.pushController = newPushController(o)
	go func() {
		err := server.Serve(ln)
		if err != nil {
			pterm.Error.Println("Omega Side 服务端关闭 " + err.Error())
		}
		close(o.closeCtx)
	}()
	if o.DebugServerOnly {
		pterm.Success.Printfln("根据你的设置，Omega Side 将不会启动任何插件，而仅会打开一个用于开发和调试插件的WebSocket端口 ws://%v/omega_side", addr)
		return
	}
	for _, cmd := range o.StartUpCmds {
		remapper := cmd.Remapper
		remapper["[addr]"] = addr
		remapper["[name]"] = cmd.Name
		remapper["[python]"] = o.pythonPath
		runcmd.RunCmd(cmd.Name, cmd.Cmd, remapper, "组件/OmegaSide/")
	}
}
func (o *OmegaSide) handle(w http.ResponseWriter, r *http.Request) {
	upgrader := websocket.Upgrader{
		ReadBufferSize:    4096,
		WriteBufferSize:   4096,
		EnableCompression: true,
		CheckOrigin: func(r *http.Request) bool {
			return true
		},
	}
	conn, err := upgrader.Upgrade(w, r, nil)
	if err != nil {
		pterm.Error.Println("Omega side WS error:", err)
		return
	}
	defer conn.Close()
	transportor := newTransporter(o.pushController, conn)
	defer func() {
		o.pushController.deRegTransportor(transportor.subClinetId)
	}()
	for {
		_, data, err := conn.ReadMessage()
		if err != nil {
			if err != io.EOF {
				pterm.Error.Println("An omega side client terminated")
			}
			return
		}
		fmt.Println(data)
		transportor.response(data, transportor.writeToConn)
	}
}

// 创建配置文件
// 读取组件的配置文件,data是json文本,返回的也应当是json文本
func Load_profile() []byte {

	if !FileExist("配置/OmegaSide旁加载组件系统/组件-OmegaSide旁加载组件系统-1.json") {
		return ConfigBytes
	} else {

	}
	content, err := ioutil.ReadFile("配置/OmegaSide旁加载组件系统/组件-OmegaSide旁加载组件系统-1.json") // 文件名兼容,正常情况下组件都不叫这个名字的
	if err != nil {
		log.Fatal("无法打开配置文件 ", err)
	}
	return content
}

// 文件夹的创建
func bootstrapDirs() {

	Mkdir(pterm.Yellow("创建OmegaSide文件夹:"), "组件/OmegaSide/")
	Mkdir(pterm.Yellow("创建配置文件夹:"), "配置/OmegaSide旁加载组件系统")
}

// 创建文件夹,然鹅不是给用户使用的。
func Mkdir(tip string, path string) {
	if !utils.IsDir(path) {
		Println(tip + pterm.Green(path))
		if err := utils.MakeDirP(path); err != nil {
			panic(err)
		}
	}
}

// 组件的版本更新检查
// 通常情况下,版本一致时即最新版本,这里的模板是插件的名字,你可以替换一下
// 如果你是开发者调试时,请暂时屏蔽本函数并直接返回当前版本
func Update_cheak() (bool, string) {
	resp, err := http.Get("https://apip.mcppl.cn/dotcs-omega-side/version")
	if err != nil {
		fmt.Printf("Failed to check update!\nPlease check your network status.\n")
		return false, ""
	}
	content, err := io.ReadAll(resp.Body)
	if err != nil {
		panic("自动更新检查失败")
	}
	_version := strings.ReplaceAll(string(content), "\n", "")
	return _version == Version, _version
}
func FileExist(path string) bool {
	_, err := os.Lstat(path)
	return !os.IsNotExist(err)
}

// DotCS 引擎开始首次加载组件了,请自行将数据缓存到本地。
// DotCS 会在引擎启动后调用本函数,函数会传递一个结构体的变量
// 返回 true 是初始化成功
func Run_Plugin(data interface{}) bool {
	return true
}

// 监听数据包,所有的数据包都会运行本函数
func Listen_Packet(data packet.Packet) bool {
	go plugin_data.pushController.pushMCPkt(int(data.ID()), data)
	return true
}

var (
	wsmu sync.Mutex
)

type pushController struct {
	side              *OmegaSide
	subClientCount    int
	anyPacketWaitor   map[int]*websocket.Conn
	typedPacketWaitor map[int]map[int]*websocket.Conn
	regInfoRemapper   map[int]map[int]bool
	mu                sync.RWMutex
}

func newPushController(s *OmegaSide) *pushController {
	p := &pushController{}
	p.anyPacketWaitor = map[int]*websocket.Conn{}
	p.typedPacketWaitor = map[int]map[int]*websocket.Conn{}
	p.regInfoRemapper = map[int]map[int]bool{}
	p.side = s
	return p
}

func (p *pushController) nextSubClientID() int {
	p.subClientCount++
	return p.subClientCount
}

func (p *pushController) deRegTransportor(id int) {
	p.mu.Lock()
	defer p.mu.Unlock()
	if pkts, hasK := p.regInfoRemapper[id]; hasK {
		for pktID, _ := range pkts {
			if pktID == 0 {
				delete(p.anyPacketWaitor, id)
			} else {
				delete(p.typedPacketWaitor, id)
			}
		}
	}
}

func (p *pushController) regPushType(clientID, pktID int, conn *websocket.Conn) {
	p.mu.Lock()
	defer p.mu.Unlock()
	if pktID == 0 {
		if pkts, hasK := p.regInfoRemapper[clientID]; hasK {
			// fmt.Println(pkts)
			for pktID, _ := range pkts {
				if pktID != 0 {
					delete(p.typedPacketWaitor[pktID], clientID)
				}
			}
		} else {
			p.regInfoRemapper[clientID] = map[int]bool{}
		}
		p.anyPacketWaitor[clientID] = conn
		p.regInfoRemapper[clientID] = map[int]bool{0: true}
	} else {
		if clients, hasK := p.typedPacketWaitor[pktID]; hasK {
			clients[clientID] = conn
		} else {
			p.typedPacketWaitor[pktID] = map[int]*websocket.Conn{clientID: conn}
		}
		if mapper, hasK := p.regInfoRemapper[clientID]; hasK {
			mapper[pktID] = true
		} else {
			p.regInfoRemapper[clientID] = map[int]bool{pktID: true}
		}
	}
}

func (p *pushController) pushMCPkt(pktID int, data interface{}) {
	p.mu.RLock()
	defer p.mu.RUnlock()
	name := utils.PktIDInvMapping[pktID]
	if waitors, hasK := p.typedPacketWaitor[pktID]; hasK {
		for _, w := range waitors {
			wsmu.Lock()
			w.WriteJSON(ServerPush{ID0: 0, Type: "mcPkt", SubType: name, Data: data})
			wsmu.Unlock()
		}
	}
	for _, w := range p.anyPacketWaitor {
		wsmu.Lock()
		w.WriteJSON(ServerPush{ID0: 0, Type: "mcPkt", SubType: name, Data: data})
		wsmu.Unlock()
	}
}

type omegaSideTransporter struct {
	side        *OmegaSide
	controller  *pushController
	conn        *websocket.Conn
	subClinetId int
	funcMapping map[string]func(args map[string]interface{}, writer func(interface{}))
}

func newTransporter(p *pushController, conn *websocket.Conn) *omegaSideTransporter {
	clientID := p.nextSubClientID()
	transporter := omegaSideTransporter{
		side:        p.side,
		controller:  p,
		subClinetId: clientID,
		conn:        conn,
	}
	transporter.initMapping()
	return &transporter
}

func (t *omegaSideTransporter) regPkt(pktId int) {
	t.controller.regPushType(t.subClinetId, pktId, t.conn)
}

func (t *omegaSideTransporter) writeToConn(data interface{}) error {
	wsmu.Lock()
	defer wsmu.Unlock()
	err := t.conn.WriteJSON(data)
	return err
}

func (t *omegaSideTransporter) response(data []byte, writeFn func(interface{}) error) {
	msg := &clientMsg{}
	if err := json.Unmarshal(data, &msg); err != nil {
		writeFn(serverResp{ID: 0, Violate: true, Data: RespViolatePkt{Err: fmt.Sprintf("cannot decode msg %v", err)}})
		return
	}
	if doFunc, hasK := t.funcMapping[msg.Action]; hasK {
		defer func() {
			r := recover()
			if r != nil {
				writeFn(serverResp{ID: msg.ID, Violate: true, Data: RespViolatePkt{Err: fmt.Sprintf("%v", r)}})
			}
		}()
		doFunc(msg.Args, wrapWriteFn(msg.ID, writeFn))
	} else {
		writeFn(serverResp{ID: msg.ID, Violate: true, Data: RespViolatePkt{Err: fmt.Sprintf("action %v not found", msg.Action)}})
	}
}
func wrapWriteFn(msgID int, writeFn func(interface{}) error) func(interface{}) {
	return func(resp interface{}) {
		writeFn(serverResp{ID: msgID, Violate: false, Data: resp})
	}
}

type clientMsg struct {
	ID     int                    `json:"client"`
	Action string                 `json:"function"`
	Args   map[string]interface{} `json:"args"`
}

type serverResp struct {
	ID      int         `json:"client"`
	Violate bool        `json:"violate"`
	Data    interface{} `json:"data"`
}

type ServerPush struct {
	ID0     int         `json:"client"`
	Type    string      `json:"type"`
	SubType string      `json:"sub"`
	Data    interface{} `json:"data"`
}

//   - 错误数据包 (仅在插件发来的数据包不符合协议的时候由omega框架发送，
//     收到这个数据包代表程序设计存在问题，因此，不收到这个数据包并不代表执行成功)
//     {"client":c,"violate":true,"data":{"err":reason}}
type RespViolatePkt struct {
	Err string `json:"err"`
}

type SimplifiedPlayerInfo struct {
	Name      string `json:"name"`
	RuntimeID uint64 `json:"runtimeID"`
	UUID      string `json:"uuid"`
	UniqueID  int64  `json:"uniqueID"`
}

func (t *omegaSideTransporter) initMapping() {
	t.funcMapping = map[string]func(args map[string]interface{}, writer func(interface{})){
		"echo": func(args map[string]interface{}, writer func(interface{})) {
			writer(args)
		},
		"regMCPkt": func(args map[string]interface{}, writer func(interface{})) {
			pktID := args["pktID"].(string)
			if pktID == "all" {
				t.regPkt(0)
				writer(map[string]interface{}{"succ": true, "err": nil})
			} else if pktIDCode, hasK := utils.PktIDMapping[pktID]; hasK {
				t.regPkt(pktIDCode)
				writer(map[string]interface{}{"succ": true, "err": nil})
			} else {
				writer(map[string]interface{}{"succ": false, "err": fmt.Sprintf("pktID %v not found, all possible ids are %v", pktID, utils.PktIDNames)})
			}
		},
		"reg_mc_packet": func(args map[string]interface{}, writer func(interface{})) {
			pktID := args["pktID"].(string)
			if pktID == "all" {
				t.regPkt(0)
				writer(map[string]interface{}{"succ": true, "err": nil})
			} else if pktIDCode, hasK := utils.PktIDMapping[pktID]; hasK {
				t.regPkt(pktIDCode)
				writer(map[string]interface{}{"succ": true, "err": nil})
			} else {
				writer(map[string]interface{}{"succ": false, "err": fmt.Sprintf("pktID %v not found, all possible ids are %v", pktID, utils.PktIDNames)})
			}
		},
		"query_packet_name": func(args map[string]interface{}, writer func(interface{})) {
			pktID := int(args["pktID"].(float64))
			pktName := utils.PktIDInvMapping[pktID]
			writer(map[string]interface{}{"name": pktName})
		},
		"send_packet": func(args map[string]interface{}, writer func(interface{})) {
			_pk, ok := packet.NewPool()[uint32(args["packetID"].(float64))]
			if ok {
				pk := _pk()
				_err := json.Unmarshal([]byte(args["jsonStr"].(string)), &pk)
				if _err != nil {
					writer(map[string]interface{}{"succ": false, "err": string(_err.Error())})
				} else {
					// WritePacket
					Game_Function.Connection.(*minecraft.Conn).WritePacket(pk)
					writer(map[string]interface{}{"succ": true, "err": nil})
				}
			} else {
				writer(map[string]interface{}{"succ": false, "err": "packetID is not in pool"})
			}
		},
		"send_ws_cmd": func(args map[string]interface{}, writer func(interface{})) {
			cmd := args["cmd"].(string)
			run_packet, err := Game_Function.GameInterface.SendWSCommandWithResponse(cmd)
			if err != nil {

			} else {
				writer(map[string]interface{}{"result": run_packet})
			}

		},
		"send_player_cmd": func(args map[string]interface{}, writer func(interface{})) {
			cmd := args["cmd"].(string)
			run_packet, err := Game_Function.GameInterface.SendCommandWithResponse(cmd)
			if err != nil {

			} else {
				writer(map[string]interface{}{"result": run_packet})
			}
		},
		"send_wo_cmd": func(args map[string]interface{}, writer func(interface{})) {

			cmd := args["cmd"].(string)
			Game_Function.Connection.(*minecraft.Conn).WritePacket(&packet.SettingsCommand{
				CommandLine:    cmd,
				SuppressOutput: true,
			})
			writer(map[string]interface{}{"ack": true})
		},
	}
}
