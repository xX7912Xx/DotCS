package components

import (
	"encoding/json"
	"fmt"
	"phoenixbuilder/minecraft/protocol/packet"
	"phoenixbuilder/mirror"
	"phoenixbuilder/mirror/chunk"
	"phoenixbuilder/mirror/define"
	"phoenixbuilder/omega/defines"
	"phoenixbuilder/omega/utils"
	"regexp"
	"strings"
	"sync"
	"time"

	"github.com/pterm/pterm"
)

type ContainerScan struct {
	*defines.BasicComponent
	EnableK32Detect    bool `json:"启用32容器检测"`
	K32Threshold       int  `json:"32k物品附魔等级阈值"`
	k32Response        []defines.Cmd
	K32ResponsIn       interface{}            `json:"32k容器反制"`
	RegexCheckers      []*ContainerRegexCheck `json:"使用以下正则表达式检查"`
	needFetchBlockName bool
	regexTaskQueue     []func()
	regexMu            sync.Mutex
	regexCheckerAwaked bool
}

type ContainerRegexCheck struct {
	Enabled                bool        `json:"启用"`
	Description            string      `json:"检测说明"`
	Debug                  bool        `json:"调试模式"`
	BlockName              string      `json:"匹配方块名"`
	Tag                    string      `json:"匹配标签名"`
	RegexString            string      `json:"使用正则表达式匹配标签值"`
	Allow                  bool        `json:"匹配标签值成功时true为放行false为作弊"`
	ExtraCommandIn         interface{} `json:"附加指令"`
	extraCommands          []defines.Cmd
	compiledBlockNameRegex regexp.Regexp
	compiledValueRegex     regexp.Regexp
}

func (o *ContainerScan) Init(cfg *defines.ComponentConfig, storage defines.StorageAndLogProvider) {
	m, _ := json.Marshal(cfg.Configs)
	err := json.Unmarshal(m, o)
	if err != nil {
		panic(err)
	}
	o.k32Response, err = utils.ParseAdaptiveCmd(o.K32ResponsIn)
	if err != nil {
		panic(err)
	}
	o.regexTaskQueue = make([]func(), 0)
	o.regexMu = sync.Mutex{}
	for _, rc := range o.RegexCheckers {
		rc.compiledValueRegex = *regexp.MustCompile(rc.RegexString)
		if rc.BlockName != "" && rc.Enabled {
			o.needFetchBlockName = true
		}
		rc.compiledBlockNameRegex = *regexp.MustCompile(rc.BlockName)
		if rc.ExtraCommandIn == nil {
			rc.extraCommands = make([]defines.Cmd, 0)
		} else {
			if rc.extraCommands, err = utils.ParseAdaptiveCmd(rc.ExtraCommandIn); err != nil {
				panic(err)
			}
		}
	}
}

func (o *ContainerScan) regexNbtDetect(blockName string, nbt map[string]interface{}, x, y, z int) (has32K bool, reason string) {
	for _, regexCheck := range o.RegexCheckers {
		if has32K {
			break
		}
		if !regexCheck.Enabled {
			continue
		}
		debug := regexCheck.Debug
		if debug {
			pterm.Info.Printfln("正在调试正则表达式检查器\"%v\":检测nbt方块 %v 中tag \"%v\" 对应值是否符合 \"%v\" (调试模式)",
				regexCheck.Description,
				blockName,
				regexCheck.Tag, regexCheck.RegexString)
			s, err := json.Marshal(nbt)
			if err == nil {
				pterm.Info.Println("完整nbt为" + string(s))
			} else {
				pterm.Info.Println("完整nbt获取失败" + err.Error())
			}
		}
		reason := ""
		if regexCheck.BlockName != "" {
			matchName := regexCheck.compiledBlockNameRegex.Find([]byte(blockName))
			if matchName == nil {
				if debug {
					pterm.Info.Printfln("方块名\"%v\"不匹配指定的正则表达式\"%v\"", blockName, regexCheck.BlockName)
				}
				continue
			} else {
				if debug {
					pterm.Warning.Printfln("方块名\"%v\"匹配指定的正则表达式\"%v\",匹配项为\"%v\"", blockName, regexCheck.BlockName, string(matchName))
					s, err := json.Marshal(nbt)
					if err == nil {
						pterm.Info.Println("完整nbt为" + string(s))
					} else {
						pterm.Info.Println("完整nbt获取失败" + err.Error())
					}
				}
				reason = fmt.Sprintf("方块名\"%v\"匹配指定的正则表达式\"%v\",匹配项为\"%v\" ", blockName, regexCheck.BlockName, string(matchName))
			}
		}
		tag := regexCheck.Tag
		doMatch := func(s string) (has32K bool) {
			if debug {
				pterm.Info.Printfln("key: \"%v\" value: \"%v\" => 检测是否匹配 \"%v\"", regexCheck.Tag, s, regexCheck.RegexString)
			}
			match := regexCheck.compiledValueRegex.Find([]byte(s))
			reason += ",且对于tag:\"" + tag + "\","
			if match == nil {
				if debug {
					pterm.Warning.Println("没有匹配项\n")
				}
				reason += "没有匹配项"
				if regexCheck.Allow == true {
					has32K = true
					reason += "，模式设置为匹配成功时放行，现在匹配不成功，因此认为作弊"
				}
			} else {
				if debug {
					pterm.Warning.Printfln("发现匹配项目:\"%v\"", string(match))
				}
				reason += fmt.Sprintf("中:\"%v\"命中正则匹配式:\"%v\"(\"%v\")", string(match), regexCheck.Description, regexCheck.RegexString)
				if regexCheck.Allow == false {
					has32K = true
					reason += "，模式设置为匹配成功时作弊，现在匹配成功了，因此认为作弊"
				}
			}
			if has32K {
				if debug {
					pterm.Error.Printfln("发现32k，具体判断理由为：%v，当前处于调试模式，因此不会实际执行反制指令", reason)
					return false
				} else {
					if len(regexCheck.extraCommands) > 0 {
						mapping := map[string]interface{}{
							"[x]": x,
							"[y]": y,
							"[z]": z,
						}
						for i := 0; i < 4; i++ {
							mapping[fmt.Sprintf("[x+%v]", i)] = x + i
							mapping[fmt.Sprintf("[y+%v]", i)] = y + i
							mapping[fmt.Sprintf("[z+%v]", i)] = z + i
						}
						for i := -3; i < 0; i++ {
							mapping[fmt.Sprintf("[x%v]", i)] = x + i
							mapping[fmt.Sprintf("[y%v]", i)] = y + i
							mapping[fmt.Sprintf("[z%v]", i)] = z + i
						}
						go utils.LaunchCmdsArray(o.Frame.GetGameControl(), regexCheck.extraCommands, mapping, o.Frame.GetBackendDisplay())
					}
					return true
				}
			} else {
				if debug {
					pterm.Success.Printfln("该方块不是作弊方块")
				}
				return false
			}

		}
		if tag == "" {
			s, err := json.Marshal(nbt)
			if err == nil {
				if doMatch(string(s)) {
					return true, reason
				}
			} else {
				fmt.Println(err)
			}
		} else {
			findAndPrintK(regexCheck.Tag, nbt, debug, func(s string) {
				if !has32K {
					has32K = doMatch(string(s))
				}
			})
		}
	}
	return has32K, reason
}

func (o *ContainerScan) doCheckNbt(x, y, z int, nbt map[string]interface{}, getStr func() string) {
	has32K := false
	reason := ""
	if o.EnableK32Detect {
		findK("lvl", nbt, func(v interface{}) {
			if level, success := v.(int16); success {
				if int(level) > o.K32Threshold {
					has32K = true
					reason = fmt.Sprintf("32k 方块：%v > %v", int(level), o.K32Threshold)
				} else if int(level) < 0 {
					has32K = true
					reason = fmt.Sprintf("32k 方块：%v < 0", int(level))
				}
			}
		})
	}
	if !has32K {
		flag := true
		if o.needFetchBlockName {
			if rtid, success := o.Frame.GetWorld().Block(define.CubePos{x, y, z}); success {
				if block, found := chunk.RuntimeIDToBlock(rtid); found {
					flag = false
					has32K, reason = o.regexNbtDetect(strings.ReplaceAll(block.Name, "minecraft:", ""), nbt, x, y, z)
				}
			}
			// has32K, reason = o.regexNbtDetect(s, nbt, x, y, z)
			// utils.QueryBlockName(o.Frame.GetGameControl(), x, y, z, func(s string) {
			// 	has32K, reason = o.regexNbtDetect(s, nbt, x, y, z)
			// })
		}
		if flag {
			has32K, reason = o.regexNbtDetect("unknow_error", nbt, x, y, z)
		}
	}
	if has32K {
		o.Frame.GetBackendDisplay().Write(fmt.Sprintf("位于 %v %v %v 的方块:"+reason, x, y, z))
		go utils.LaunchCmdsArray(o.Frame.GetGameControl(), o.k32Response, map[string]interface{}{
			"[x]": x,
			"[y]": y,
			"[z]": z,
		}, o.Frame.GetBackendDisplay())
	}
}

func (o *ContainerScan) onLevelChunk(cd *mirror.ChunkData) {
	for _, nbt := range cd.BlockNbts {
		if x, y, z, success := define.GetPosFromNBT(nbt); success {
			o.checkNbt(int(x), int(y), int(z), nbt, func() string {
				marshal, _ := json.Marshal(nbt)
				return string(marshal)
			})
		}
	}
}

func (o *ContainerScan) checkNbt(x, y, z int, nbt map[string]interface{}, getStr func() string) {
	// if !o.needFetchBlockName {
	o.doCheckNbt(x, y, z, nbt, getStr)
	// } else {
	// 	o.regexMu.Lock()
	// 	o.regexTaskQueue = append(o.regexTaskQueue, func() {
	// 		o.doCheckNbt(x, y, z, nbt, getStr)
	// 	})
	// 	o.regexMu.Unlock()
	// 	go o.awakeChecker()
	// }
}

func (o *ContainerScan) onBlockActorData(pk *packet.BlockActorData) {
	nbt := pk.NBTData
	x, y, z := pk.Position.X(), pk.Position.Y(), pk.Position.Z()
	o.checkNbt(int(x), int(y), int(z), nbt, func() string {
		marshal, _ := json.Marshal(nbt)
		return string(marshal)
	})
}

func (o *ContainerScan) Inject(frame defines.MainFrame) {
	o.Frame = frame
	o.Frame.GetGameListener().SetOnTypedPacketCallBack(packet.IDBlockActorData, func(p packet.Packet) {
		o.onBlockActorData(p.(*packet.BlockActorData))
	})
	o.Frame.GetGameListener().SetOnLevelChunkCallBack(o.onLevelChunk)
}

func (o *ContainerScan) awakeChecker() {
	if o.regexCheckerAwaked {
		return
	}
	o.regexCheckerAwaked = true
	t := time.NewTicker(51 * time.Millisecond)
	for {
		if len(o.regexTaskQueue) == 0 {
			o.regexCheckerAwaked = false
			return
		} else {
			// fmt.Println(len(o.regexTaskQueue))
		}
		<-t.C
		o.regexMu.Lock()
		t := o.regexTaskQueue[0]
		o.regexTaskQueue = o.regexTaskQueue[1:]
		o.regexMu.Unlock()
		t()
	}
}
