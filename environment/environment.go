package environment

// This package imports only external packages to avoid import cycle.
import (
	"dotcs/environment/interfaces"
	"dotcs/utils"
	"fmt"
	"plugin"
)

type LoginInfo struct {
	Token          string
	ServerCode     string
	ServerPasscode string
	Username       string
	Password       string
}

type PBEnvironment struct {
	LoginInfo
	IsDebug                   bool
	ScriptBridge              interface{}
	ScriptHolder              interface{}
	FunctionHolder            interfaces.FunctionHolder
	FBUCUsername              string
	WorldChatChannel          chan []string
	FBAuthClient              interface{}
	GlobalFullConfig          interface{}
	RespondUser               string
	Connection                interface{}
	UQHolder                  interface{}
	Resources                 interface{}
	ResourcesUpdater          interface{}
	GameInterface             interfaces.GameInterface
	ActivateTaskStatus        chan bool
	Uid                       string
	ExternalConnectionHandler interface{}
	Destructors               []func()
	isStopping                bool
	stoppedWaiter             chan struct{}
	CertSigning               bool
	LocalKey                  string
	LocalCert                 string
	LRUMemoryChunkCacher      interface{}
	ChunkFeeder               interface{}
	storageRoot               string
	PythonPath                string
	JavaPath                  string
	Plugins                   map[string]*plugin.Plugin
}

func (env *PBEnvironment) Init() {

}
func (d *PBEnvironment) bootstrapRootDir() string {
	d.storageRoot = "dotcs_engine"
	// android
	if utils.IsDir("/sdcard/Download/dotcs_engine") {
		d.storageRoot = "/sdcard/Download/dotcs_engine"
	} else {
		if utils.IsDir("/sdcard") {
			if err := utils.MakeDirP("/sdcard/Download/dotcs_engine"); err == nil {
				d.storageRoot = "/sdcard/Download/dotcs_engine"
			}
		}
	}
	if d.storageRoot == "/sdcard/Download/dotcs_engine" {
		fmt.Println("检测到当前环境疑似为安卓手机,数据将保存在/sdcard/Download/dotcs_engine中")
	}
	if !utils.IsDir(d.storageRoot) {
		fmt.Println("创建数据文件夹 " + d.storageRoot)
		if err := utils.MakeDirP(d.storageRoot); err != nil {
			panic(err)
		}
	}
	return d.storageRoot
}
func (env *PBEnvironment) Stop() {
	if env.isStopping {
		return
	}
	//fmt.Println("stopping")
	env.GameInterface.SendCommand("kick @s")
	env.stoppedWaiter = make(chan struct{})
	env.isStopping = true
	for _, fn := range env.Destructors {
		fn()
	}
	//fmt.Println("stopped")
	close(env.stoppedWaiter)
}

func (env *PBEnvironment) WaitStopped() {
	//fmt.Println("waitting stopped")
	<-env.stoppedWaiter
}
