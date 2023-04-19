package components

import (
	"encoding/json"
	"fmt"
	"phoenixbuilder/minecraft/protocol"
	"phoenixbuilder/omega/collaborate"
	"phoenixbuilder/omega/defines"
	"phoenixbuilder/omega/utils"
	"strings"
	"time"
)

type Memo struct {
	*defines.BasicComponent
	logger            defines.LineDst
	HintOnEmptyPlayer string `json:"没有指定玩家时提示"`
	HintOnEmptyMsg    string `json:"没有输入信息时提示"`
	Response          string `json:"留言成功时提示"`
	fileChange        bool
	FileName          string   `json:"留言记录文件"`
	LogFile           string   `json:"日志文件"`
	Triggers          []string `json:"触发词"`
	LoginDelay        int      `json:"登录时延迟发送"`
	Memos             map[string][]string
	Usage             string `json:"提示信息"`
	PlayerSearcher    collaborate.FUNCTYPE_GET_POSSIBLE_NAME
}

func (me *Memo) send(playerName string) {
	if msgs, hasK := me.Memos[playerName]; hasK {
		if len(msgs) > 0 {
			if player := me.Frame.GetGameControl().GetPlayerKit(playerName); player != nil {
				player.Title("有新留言")
				player.SubTitle("查看聊天栏")
				for _, m := range msgs {
					player.Say(m)
					me.logger.Write("send to " + playerName + " " + m)
				}
				delete(me.Memos, playerName)
				me.fileChange = true
			}
		} else {
			delete(me.Memos, playerName)
			me.fileChange = true
		}
	}
}

func (me *Memo) save(srcPlayer, dstPlayer, msg string) bool {
	//dstPlayer := chat.Msg[0]
	//msg := strings.Join(chat.Msg[1:], " ")
	me.logger.Write(fmt.Sprintf("[%v]->[%v]:%v ", srcPlayer, dstPlayer, msg))
	m := utils.FormatByReplacingOccurrences(me.Response, map[string]interface{}{
		"[src_player]": "\"" + srcPlayer + "\"",
		"[dst_player]": "\"" + dstPlayer + "\"",
		"[msg]":        msg,
	})

	me.Frame.GetGameControl().SendCmd(m)
	if _, hasK := me.Memos[dstPlayer]; !hasK {
		me.Memos[dstPlayer] = make([]string, 0)
	}
	me.Memos[dstPlayer] = append(me.Memos[dstPlayer],
		fmt.Sprintf("你有一条来自 %v 的留言: %v", srcPlayer, msg),
	)
	for _, p := range me.Frame.GetUQHolder().PlayersByEntityID {
		if p.Username == dstPlayer {
			me.send(dstPlayer)
		}
	}
	me.fileChange = true
	return true
}

func (me *Memo) askForMsg(srcPlayer, dstPlayer string) {
	//dstPlayer := chat.Msg[0]
	if player := me.Frame.GetGameControl().GetPlayerKit(srcPlayer); player != nil {
		if player.SetOnParamMsg(func(c *defines.GameChat) bool {
			//c.Msg = utils.InsertHead[string](dstPlayer, c.Msg)
			me.save(srcPlayer, dstPlayer, strings.Join(c.Msg, " "))
			return true
		}) == nil {
			me.Frame.GetGameControl().SayTo(srcPlayer, me.HintOnEmptyMsg)
		}
	}
}

//func (me *Memo) askForPlayer(chat *defines.GameChat) {
//	if player := me.Frame.GetGameControl().GetPlayerKit(chat.Name); player != nil {
//		if player.SetOnParamMsg(func(c *defines.GameChat) bool {
//			me.record(c)
//			return true
//		}) == nil {
//			me.Frame.GetGameControl().SayTo(chat.Name, me.HintOnEmptyPlayer)
//		}
//	}
//}

func (o *Memo) BeforeActivate() (err error) {
	possibleNames, hasK := o.Frame.GetContext(collaborate.INTERFACE_POSSIBLE_NAME)
	if !hasK {
		panic(fmt.Errorf("collaborate interface %v not found", collaborate.INTERFACE_POSSIBLE_NAME))
	}
	o.PlayerSearcher = possibleNames.(collaborate.FUNCTYPE_GET_POSSIBLE_NAME)
	return nil
}

func (me *Memo) askForPlayer(chat *defines.GameChat) {
	go func() {
		if collaborate_func, hasK := me.Frame.GetContext(collaborate.INTERFACE_QUERY_FOR_PLAYER_NAME); hasK {
			if name, cancel := collaborate_func.(collaborate.QUERY_FOR_PLAYER_NAME)(
				chat.Name,
				"",
				me.PlayerSearcher); !cancel {
				me.askForMsg(chat.Name, name)
			} else {
				me.Frame.GetGameControl().SayTo(chat.Name, "已取消")
			}
		}
	}()

	//if player := me.Frame.GetGameControl().GetPlayerKit(chat.Name); player != nil {
	//	if player.SetOnParamMsg(func(c *defines.GameChat) bool {
	//		me.record(c)
	//		return true
	//	}) == nil {
	//		me.Frame.GetGameControl().SayTo(chat.Name, me.HintOnEmptyPlayer)
	//	}
	//}
}

func (me *Memo) record(chat *defines.GameChat) bool {
	me.askForPlayer(chat)
	return true
}

func (me *Memo) Init(cfg *defines.ComponentConfig, storage defines.StorageAndLogProvider) {
	m, _ := json.Marshal(cfg.Configs)
	if err := json.Unmarshal(m, me); err != nil {
		panic(err)
	}
}

func (me *Memo) Inject(frame defines.MainFrame) {
	me.Frame = frame
	me.logger = &utils.MultipleLogger{Loggers: []defines.LineDst{
		me.Frame.GetLogger(me.LogFile),
		me.Frame.GetBackendDisplay(),
	}}
	me.Frame.GetGameListener().AppendLoginInfoCallback(func(entry protocol.PlayerListEntry) {
		name := utils.ToPlainName(entry.Username)
		if _, hasK := me.Memos[name]; hasK {
			timer := time.NewTimer(time.Duration(me.LoginDelay) * time.Second)
			go func() {
				<-timer.C
				for _, p := range me.Frame.GetUQHolder().PlayersByEntityID {
					if p.Username == name {
						me.send(name)
					}
				}
			}()
		}
	})
	if me.Usage == "" {
		me.Usage = "给某个玩家留言，将在上线时转达留言"
	}
	me.Frame.GetGameListener().SetGameMenuEntry(&defines.GameMenuEntry{
		MenuEntry: defines.MenuEntry{
			Triggers:     me.Triggers,
			ArgumentHint: "[玩家] [消息]",
			Usage:        me.Usage,
			FinalTrigger: false,
		},
		OptionalOnTriggerFn: me.record,
	})
	me.Memos = map[string][]string{}
	err := frame.GetJsonData(me.FileName, &me.Memos)
	if err != nil {
		panic(err)
	}
}
func (o *Memo) Signal(signal int) error {
	switch signal {
	case defines.SIGNAL_DATA_CHECKPOINT:
		if o.fileChange {
			o.fileChange = false
			return o.Frame.WriteJsonDataWithTMP(o.FileName, ".ckpt", o.Memos)
		}
	}
	return nil
}
func (me *Memo) Stop() error {
	fmt.Printf("正在保存 %v\n", me.FileName)
	return me.Frame.WriteJsonDataWithTMP(me.FileName, ".final", me.Memos)
}
