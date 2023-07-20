package environment

import (
	"dotcs/environment/interfaces"
	"fmt"
	"io/ioutil"
	"plugin"
	"strings"

	"github.com/pterm/pterm"
)

type Plugins struct {
	IsDebug                   bool
	ScriptBridge              interface{}
	ScriptHolder              interface{}
	FunctionHolder            interfaces.FunctionHolder
	WorldChatChannel          chan []string
	GlobalFullConfig          interface{}
	RespondUser               string
	Connection                interface{}
	GameInterface             interfaces.GameInterface
	ActivateTaskStatus        chan bool
	Uid                       string
	ExternalConnectionHandler interface{}
	Destructors               []func()
	LRUMemoryChunkCacher      interface{}
	ChunkFeeder               interface{}
	PythonPath                string
	JavaPath                  string
}

func (env *PBEnvironment) Load_plugin() {
	rd, err := ioutil.ReadDir("plugins")
	if err != nil {
		fmt.Println("read dir fail:", err)
	}
	all := len(rd)
	for i, fi := range rd {
		pterm.Success.Println(fmt.Sprintf("[%d/%d] 正在加载组件:", i+1, all), fi.Name())
		if !fi.IsDir() {
			fullName := "plugins" + "/" + fi.Name()
			p, err := plugin.Open(fullName)
			if err != nil {
				if find := strings.Contains(err.Error(), ": plugin already loaded"); find {
					pterm.Error.Println("组件:", fi.Name(), "已有相同的组件加载,请检查组件是否存在名字不一样的相同组件")
					continue
				}
				pterm.Error.Println("加载组件失败:", err)
				continue
			}
			title, err := p.Lookup("Title")
			if err != nil {
				pterm.Error.Println("组件名不存在,请删除组件", fullName)
			}
			env.Plugins[*title.(*string)] = p
		} else {
			pterm.Warning.Println(fmt.Sprintf("[%d/%d] 这个组件是个文件夹:", i, all), fi.Name())
		}
	}
}
func (env *PBEnvironment) Init_plugin() {
	for plugin_name, p := range env.Plugins {
		// 获取初始化函数
		Game_Init, err := p.Lookup("Game_Init")
		if err != nil {
			pterm.Error.Println("[" + plugin_name + "]" + "组件初始化失败,您可能需要删除本组件")
		}
		version, err := p.Lookup("Version")
		if err != nil {
			pterm.Println(pterm.Yellow(pterm.Sprintf("[%s] %s", pterm.Green(plugin_name)), fmt.Sprint("组件版本获取失败,你必须删除本组件")))
			panic("[" + plugin_name + "]" + "组件版本获取失败,你必须删除本组件")
		}
		if !Game_Init.(func(*Plugins) bool)(&Plugins{
			IsDebug:                   env.IsDebug,
			ScriptBridge:              env.ScriptBridge,
			ScriptHolder:              env.ScriptHolder,
			FunctionHolder:            env.FunctionHolder,
			WorldChatChannel:          env.WorldChatChannel,
			GlobalFullConfig:          env.GlobalFullConfig,
			RespondUser:               env.RespondUser,
			Connection:                env.Connection,
			GameInterface:             env.GameInterface,
			ActivateTaskStatus:        env.ActivateTaskStatus,
			Uid:                       env.Uid,
			ExternalConnectionHandler: env.ExternalConnectionHandler,
			Destructors:               env.Destructors,
			LRUMemoryChunkCacher:      env.LRUMemoryChunkCacher,
			ChunkFeeder:               env.ChunkFeeder,
			PythonPath:                env.PythonPath,
			JavaPath:                  env.JavaPath,
		}) {
			panic("[" + plugin_name + "]" + "组件初始化失败,请移除组件或联系组件开发者修复本组件,组件版本:" + version.(string))
		}
		pterm.Success.Println(pterm.Yellow(pterm.Sprintf("[%s] %s", pterm.Green(plugin_name)), fmt.Sprint("初始化完成")))
		//func Game_Init(game interface{}) bool
	}
}
