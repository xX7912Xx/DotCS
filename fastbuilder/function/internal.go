package function

import (
	"fmt"
	"os"
	"path/filepath"
	"phoenixbuilder/bridge/bridge_fmt"
	"phoenixbuilder/fastbuilder/builder"
	"phoenixbuilder/fastbuilder/configuration"
	"phoenixbuilder/fastbuilder/environment"
	I18n "phoenixbuilder/fastbuilder/i18n"
	fbtask "phoenixbuilder/fastbuilder/task"
	"phoenixbuilder/fastbuilder/types"
	"phoenixbuilder/io/special_tasks"
	"phoenixbuilder/minecraft"
)

func InitInternalFunctions(fh *FunctionHolder) {
	delayEnumId := fh.RegisterEnum("continuous, discrete, none", types.ParseDelayMode, types.DelayModeInvalid)
	fh.RegisterFunction(&Function{
		Name:          "exit",
		OwnedKeywords: []string{"exit", "fbexit"},
		FunctionType:  FunctionTypeSimple,
		SFMinSliceLen: 1,
		FunctionContent: func(env *environment.PBEnvironment, _ []interface{}) {
			env.CommandSender.Output(I18n.T(I18n.QuitCorrectly))
			bridge_fmt.Printf("%s\n", I18n.T(I18n.QuitCorrectly))
			env.Connection.(*minecraft.Conn).Close()
			os.Exit(0)
		},
	})
	fh.RegisterFunction(&Function{
		Name:          "logout",
		OwnedKeywords: []string{"logout"},
		FunctionType:  FunctionTypeSimple,
		SFMinSliceLen: 1,
		FunctionContent: func(env *environment.PBEnvironment, _ []interface{}) {
			conn := env.Connection.(*minecraft.Conn)
			commandSender := env.CommandSender
			homedir, err := os.UserHomeDir()
			if err != nil {
				bridge_fmt.Println(I18n.T(I18n.Warning_UserHomeDir))
				homedir = "."
			}
			fbconfigdir := filepath.Join(homedir, ".config/dotcs")
			os.MkdirAll(fbconfigdir, 0755)
			token := filepath.Join(fbconfigdir, "dotcstoken")
			err = os.Remove(token)
			if err != nil {
				commandSender.Output(fmt.Sprintf(I18n.T(I18n.FBUC_Token_ErrOnRemove), err))
				return
			}
			commandSender.Output(I18n.T(I18n.Logout_Done))
			commandSender.Output(I18n.T(I18n.QuitCorrectly))
			bridge_fmt.Printf("%s\n", I18n.T(I18n.QuitCorrectly))
			conn.Close()
			os.Exit(0)
		},
	})
	fh.RegisterFunction(&Function{
		Name:          "reselect language",
		OwnedKeywords: []string{"lang"},
		FunctionType:  FunctionTypeSimple,
		SFMinSliceLen: 1,
		FunctionContent: func(env *environment.PBEnvironment, _ []interface{}) {
			env.CommandSender.Output(I18n.T(I18n.SelectLanguageOnConsole))
			I18n.SelectLanguage()
			I18n.UpdateLanguage()
		},
	})
	fh.RegisterFunction(&Function{
		Name:            "set",
		OwnedKeywords:   []string{"set"},
		FunctionType:    FunctionTypeSimple,
		SFMinSliceLen:   4,
		SFArgumentTypes: []byte{SimpleFunctionArgumentInt, SimpleFunctionArgumentInt, SimpleFunctionArgumentInt},
		FunctionContent: func(env *environment.PBEnvironment, args []interface{}) {
			X, _ := args[0].(int)
			Y, _ := args[1].(int)
			Z, _ := args[2].(int)
			configuration.GlobalFullConfig(env).Main().Position = types.Position{
				X: X,
				Y: Y,
				Z: Z,
			}
			env.CommandSender.Output(fmt.Sprintf("%s: %d, %d, %d.", I18n.T(I18n.PositionSet), X, Y, Z))
		},
	})
	fh.RegisterFunction(&Function{
		Name:            "setend",
		OwnedKeywords:   []string{"setend"},
		FunctionType:    FunctionTypeSimple,
		SFMinSliceLen:   4,
		SFArgumentTypes: []byte{SimpleFunctionArgumentInt, SimpleFunctionArgumentInt, SimpleFunctionArgumentInt},
		FunctionContent: func(env *environment.PBEnvironment, args []interface{}) {
			X, _ := args[0].(int)
			Y, _ := args[1].(int)
			Z, _ := args[2].(int)
			configuration.GlobalFullConfig(env).Main().End = types.Position{
				X: X,
				Y: Y,
				Z: Z,
			}
			env.CommandSender.Output(fmt.Sprintf("%s: %d, %d, %d.", I18n.T(I18n.PositionSet_End), X, Y, Z))
		},
	})
	fh.RegisterFunction(&Function{
		Name:          "delay",
		OwnedKeywords: []string{"delay"},
		FunctionType:  FunctionTypeContinue,
		SFMinSliceLen: 3,
		FunctionContent: map[string]*FunctionChainItem{
			"set": &FunctionChainItem{
				FunctionType:  FunctionTypeSimple,
				ArgumentTypes: []byte{SimpleFunctionArgumentInt},
				Content: func(env *environment.PBEnvironment, args []interface{}) {
					if configuration.GlobalFullConfig(env).Delay().DelayMode == types.DelayModeNone {
						env.CommandSender.Output(I18n.T(I18n.DelaySetUnavailableUnderNoneMode))
						return
					}
					ms, _ := args[0].(int)
					configuration.GlobalFullConfig(env).Delay().Delay = int64(ms)
					env.CommandSender.Output(fmt.Sprintf("%s: %d", I18n.T(I18n.DelaySet), ms))
				},
			},
			"mode": &FunctionChainItem{
				FunctionType: FunctionTypeContinue,
				Content: map[string]*FunctionChainItem{
					"get": &FunctionChainItem{
						FunctionType: FunctionTypeSimple,
						Content: func(env *environment.PBEnvironment, _ []interface{}) {
							env.CommandSender.Output(fmt.Sprintf("%s: %s.", I18n.T(I18n.CurrentDefaultDelayMode), types.StrDelayMode(configuration.GlobalFullConfig(env).Delay().DelayMode)))
						},
					},
					"set": &FunctionChainItem{
						FunctionType:  FunctionTypeSimple,
						ArgumentTypes: []byte{byte(delayEnumId)},
						Content: func(env *environment.PBEnvironment, args []interface{}) {
							delaymode, _ := args[0].(byte)
							configuration.GlobalFullConfig(env).Delay().DelayMode = delaymode
							env.CommandSender.Output(fmt.Sprintf("%s: %s", I18n.T(I18n.DelayModeSet), types.StrDelayMode(delaymode)))
							if delaymode != types.DelayModeNone {
								dl := decideDelay(delaymode)
								configuration.GlobalFullConfig(env).Delay().Delay = dl
								env.CommandSender.Output(fmt.Sprintf(I18n.T(I18n.DelayModeSet_DelayAuto), dl))
							}
							if delaymode == types.DelayModeDiscrete {
								configuration.GlobalFullConfig(env).Delay().DelayThreshold = decideDelayThreshold()
								env.CommandSender.Output(fmt.Sprintf(I18n.T(I18n.DelayModeSet_ThresholdAuto), configuration.GlobalFullConfig(env).Delay().DelayThreshold))
							}
						},
					},
				},
			},
			"threshold": &FunctionChainItem{
				FunctionType:  FunctionTypeSimple,
				ArgumentTypes: []byte{SimpleFunctionArgumentInt},
				Content: func(env *environment.PBEnvironment, args []interface{}) {
					if configuration.GlobalFullConfig(env).Delay().DelayMode != types.DelayModeDiscrete {
						env.CommandSender.Output(I18n.T(I18n.DelayThreshold_OnlyDiscrete))
						return
					}
					thr, _ := args[0].(int)
					configuration.GlobalFullConfig(env).Delay().DelayThreshold = thr
					env.CommandSender.Output(fmt.Sprintf(I18n.T(I18n.DelayThreshold_Set), thr))
				},
			},
		},
	})
	fh.RegisterFunction(&Function{
		Name:          "get-pos",
		OwnedKeywords: []string{"get"},
		FunctionType:  FunctionTypeContinue,
		SFMinSliceLen: 1,
		FunctionContent: map[string]*FunctionChainItem{
			"": &FunctionChainItem{
				FunctionType:  FunctionTypeSimple,
				ArgumentTypes: []byte{},
				Content: func(env *environment.PBEnvironment, _ []interface{}) {
					env.CommandSender.SendSizukanaCommand("gamerule sendcommandfeedback true")
					env.CommandSender.SendCommand(fmt.Sprintf("execute @a[name=\"%s\"] ~ ~ ~ testforblock ~ ~ ~ air", env.RespondUser), configuration.ZeroId)
				},
			},
			"begin": &FunctionChainItem{
				FunctionType: FunctionTypeSimple,
				Content: func(env *environment.PBEnvironment, _ []interface{}) {
					env.CommandSender.SendSizukanaCommand("gamerule sendcommandfeedback true")
					env.CommandSender.SendCommand(fmt.Sprintf("execute @a[name=\"%s\"] ~ ~ ~ testforblock ~ ~ ~ air", env.RespondUser), configuration.ZeroId)
				},
			},
			"end": &FunctionChainItem{
				FunctionType: FunctionTypeSimple,
				Content: func(env *environment.PBEnvironment, _ []interface{}) {
					env.CommandSender.SendSizukanaCommand("gamerule sendcommandfeedback true")
					env.CommandSender.SendCommand(fmt.Sprintf("execute @a[name=\"%s\"] ~ ~ ~ testforblock ~ ~ ~ air", env.RespondUser), configuration.OneId)
				},
			},
		},
	})
	fh.RegisterFunction(&Function{
		Name:          "task",
		OwnedKeywords: []string{"task"},
		FunctionType:  FunctionTypeContinue,
		SFMinSliceLen: 2,
		FunctionContent: map[string]*FunctionChainItem{
			"list": &FunctionChainItem{
				FunctionType: FunctionTypeSimple,
				Content: func(env *environment.PBEnvironment, _ []interface{}) {
					total := 0
					env.CommandSender.Output(I18n.T(I18n.CurrentTasks))
					taskholder := env.TaskHolder.(*fbtask.TaskHolder)
					taskholder.TaskMap.Range(func(_tid interface{}, _v interface{}) bool {
						tid, _ := _tid.(int64)
						v, _ := _v.(*fbtask.Task)
						dt := -1
						dv := int64(-1)
						if v.Config.Delay().DelayMode == types.DelayModeDiscrete {
							dt = v.Config.Delay().DelayThreshold
						}
						if v.Config.Delay().DelayMode != types.DelayModeNone {
							dv = v.Config.Delay().Delay
						}
						env.CommandSender.Output(fmt.Sprintf(I18n.T(I18n.TaskStateLine), tid, v.CommandLine, fbtask.GetStateDesc(v.State), dv, types.StrDelayMode(v.Config.Delay().DelayMode), dt))
						total++
						return true
					})
					env.CommandSender.Output(fmt.Sprintf(I18n.T(I18n.TaskTotalCount), total))
				},
			},
			"pause": &FunctionChainItem{
				FunctionType:  FunctionTypeSimple,
				ArgumentTypes: []byte{SimpleFunctionArgumentInt},
				Content: func(env *environment.PBEnvironment, args []interface{}) {
					tid, _ := args[0].(int)
					taskholder := env.TaskHolder.(*fbtask.TaskHolder)
					task := taskholder.FindTask(int64(tid))
					if task == nil {
						env.CommandSender.Output(I18n.T(I18n.TaskNotFoundMessage))
						return
					}
					task.Pause()
					env.CommandSender.Output(fmt.Sprintf(I18n.T(I18n.TaskPausedNotice), task.TaskId))
				},
			},
			"resume": &FunctionChainItem{
				FunctionType:  FunctionTypeSimple,
				ArgumentTypes: []byte{SimpleFunctionArgumentInt},
				Content: func(env *environment.PBEnvironment, args []interface{}) {
					tid, _ := args[0].(int)
					taskholder := env.TaskHolder.(*fbtask.TaskHolder)
					task := taskholder.FindTask(int64(tid))
					if task == nil {
						env.CommandSender.Output(I18n.T(I18n.TaskNotFoundMessage))
						return
					}
					task.Resume()
					env.CommandSender.Output(fmt.Sprintf(I18n.T(I18n.TaskResumedNotice), task.TaskId))
				},
			},
			"break": &FunctionChainItem{
				FunctionType:  FunctionTypeSimple,
				ArgumentTypes: []byte{SimpleFunctionArgumentInt},
				Content: func(env *environment.PBEnvironment, args []interface{}) {
					tid, _ := args[0].(int)
					taskholder := env.TaskHolder.(*fbtask.TaskHolder)
					task := taskholder.FindTask(int64(tid))
					if task == nil {
						env.CommandSender.Output(I18n.T(I18n.TaskNotFoundMessage))
						return
					}
					task.Break()
					env.CommandSender.Output(fmt.Sprintf(I18n.T(I18n.TaskStoppedNotice), task.TaskId))
				},
			},
			"setdelay": &FunctionChainItem{
				FunctionType:  FunctionTypeSimple,
				ArgumentTypes: []byte{SimpleFunctionArgumentInt, SimpleFunctionArgumentInt},
				Content: func(env *environment.PBEnvironment, args []interface{}) {
					tid, _ := args[0].(int)
					del, _ := args[1].(int)
					taskholder := env.TaskHolder.(*fbtask.TaskHolder)
					task := taskholder.FindTask(int64(tid))
					if task == nil {
						env.CommandSender.Output(I18n.T(I18n.TaskNotFoundMessage))
						return
					}
					if task.Config.Delay().DelayMode == types.DelayModeNone {
						env.CommandSender.Output(I18n.T(I18n.Task_SetDelay_Unavailable))
						return
					}
					env.CommandSender.Output(fmt.Sprintf(I18n.T(I18n.Task_DelaySet), task.TaskId, del))
					task.Config.Delay().Delay = int64(del)
				},
			},
			"setdelaymode": &FunctionChainItem{
				FunctionType:  FunctionTypeSimple,
				ArgumentTypes: []byte{SimpleFunctionArgumentInt, byte(delayEnumId)},
				Content: func(env *environment.PBEnvironment, args []interface{}) {
					tid, _ := args[0].(int)
					delaymode, _ := args[1].(byte)
					taskholder := env.TaskHolder.(*fbtask.TaskHolder)
					task := taskholder.FindTask(int64(tid))
					if task == nil {
						env.CommandSender.Output(I18n.T(I18n.TaskNotFoundMessage))
						return
					}
					task.Pause()
					task.Config.Delay().DelayMode = delaymode
					env.CommandSender.Output(fmt.Sprintf("[%s %d] - %s: %s", I18n.T(I18n.TaskTTeIuKoto), tid, I18n.T(I18n.DelayModeSet), types.StrDelayMode(delaymode)))
					if delaymode != types.DelayModeNone {
						task.Config.Delay().Delay = decideDelay(delaymode)
						env.CommandSender.Output(fmt.Sprintf("[%s %d] "+I18n.T(I18n.DelayModeSet_DelayAuto), I18n.T(I18n.TaskTTeIuKoto), task.TaskId, task.Config.Delay().Delay))
					}
					if delaymode == types.DelayModeDiscrete {
						task.Config.Delay().DelayThreshold = decideDelayThreshold()
						env.CommandSender.Output(fmt.Sprintf("[%s %d] "+I18n.T(I18n.DelayModeSet_ThresholdAuto), I18n.T(I18n.TaskTTeIuKoto), task.TaskId, task.Config.Delay().DelayThreshold))
					}
					task.Resume()
				},
			},
			"setdelaythreshold": &FunctionChainItem{
				FunctionType:  FunctionTypeSimple,
				ArgumentTypes: []byte{SimpleFunctionArgumentInt, SimpleFunctionArgumentInt},
				Content: func(env *environment.PBEnvironment, args []interface{}) {
					tid, _ := args[0].(int)
					delayt, _ := args[1].(int)
					taskholder := env.TaskHolder.(*fbtask.TaskHolder)
					task := taskholder.FindTask(int64(tid))
					if task == nil {
						env.CommandSender.Output(I18n.T(I18n.TaskNotFoundMessage))
						return
					}
					if task.Config.Delay().DelayMode != types.DelayModeDiscrete {
						env.CommandSender.Output(I18n.T(I18n.DelayThreshold_OnlyDiscrete))
						return
					}
					env.CommandSender.Output(fmt.Sprintf("[%s %d] - "+I18n.T(I18n.DelayThreshold_Set), I18n.T(I18n.TaskTTeIuKoto), tid, delayt))
					task.Config.Delay().DelayThreshold = delayt
				},
			},
		},
	})
	taskTypeEnumId := fh.RegisterEnum("async, sync", types.ParseTaskType, types.TaskTypeInvalid)
	fh.RegisterFunction(&Function{
		Name:            "set task type",
		OwnedKeywords:   []string{"tasktype"},
		FunctionType:    FunctionTypeSimple,
		SFMinSliceLen:   2,
		SFArgumentTypes: []byte{byte(taskTypeEnumId)},
		FunctionContent: func(env *environment.PBEnvironment, args []interface{}) {
			ev, _ := args[0].(byte)
			configuration.GlobalFullConfig(env).Global().TaskCreationType = ev
			env.CommandSender.Output(fmt.Sprintf(I18n.T(I18n.TaskTypeSwitchedTo), types.MakeTaskType(ev)))
		},
	})
	taskDMEnumId := fh.RegisterEnum("true, false", types.ParseTaskDisplayMode, types.TaskDisplayInvalid)
	fh.RegisterFunction(&Function{
		Name:            "set progress title display type",
		OwnedKeywords:   []string{"progress"},
		FunctionType:    FunctionTypeSimple,
		SFMinSliceLen:   2,
		SFArgumentTypes: []byte{byte(taskDMEnumId)},
		FunctionContent: func(env *environment.PBEnvironment, args []interface{}) {
			ev, _ := args[0].(byte)
			configuration.GlobalFullConfig(env).Global().TaskDisplayMode = ev
			env.CommandSender.Output(fmt.Sprintf(I18n.T(I18n.TaskDisplayModeSet), types.MakeTaskDisplayMode(ev)))
		},
	})
	var builderMethods []string
	for met, _ := range builder.Builder {
		builderMethods = append(builderMethods, met)
	}
	fh.RegisterFunction(&Function{
		Name:          "ippanbrd",
		OwnedKeywords: builderMethods,
		FunctionType:  FunctionTypeRegular,
		FunctionContent: func(env *environment.PBEnvironment, msg string) {
			task := fbtask.CreateTask(msg, env)
			if task == nil {
				return
			}
			env.CommandSender.Output(fmt.Sprintf("%s, ID=%d.", I18n.T(I18n.TaskCreated), task.TaskId))
		},
	})
	fh.RegisterFunction(&Function{
		Name:          "export",
		OwnedKeywords: []string{"export"},
		FunctionType:  FunctionTypeRegular,
		FunctionContent: func(env *environment.PBEnvironment, msg string) {
			task := special_tasks.CreateExportTask(msg, env)
			if task == nil {
				return
			}
			env.CommandSender.Output(fmt.Sprintf("%s, ID=%d.", I18n.T(I18n.TaskCreated), task.TaskId))
		},
	})
	fh.RegisterFunction(&Function{
		Name:          "export(legacy)",
		OwnedKeywords: []string{"lexport"},
		FunctionType:  FunctionTypeRegular,
		FunctionContent: func(env *environment.PBEnvironment, msg string) {
			task := special_tasks.CreateLegacyExportTask(msg, env)
			if task == nil {
				return
			}
			env.CommandSender.Output(fmt.Sprintf("%s, ID=%d.", I18n.T(I18n.TaskCreated), task.TaskId))
		},
	})
	fh.RegisterFunction(&Function{
		Name:            "say",
		OwnedKeywords:   []string{"say"},
		FunctionType:    FunctionTypeSimple,
		SFArgumentTypes: []byte{SimpleFunctionArgumentMessage},
		SFMinSliceLen:   1,
		FunctionContent: func(env *environment.PBEnvironment, args []interface{}) {
			str := args[0].(string)
			env.CommandSender.Output(str)
		},
	})
}

func decideDelay(delaytype byte) int64 {
	// Will add system check later,so don't merge into other functions.
	if delaytype == types.DelayModeContinuous {
		return 1000
	} else if delaytype == types.DelayModeDiscrete {
		return 15
	} else {
		return 0
	}
}

func decideDelayThreshold() int {
	// Will add system check later,so don't merge into other functions.
	return 20000
}
