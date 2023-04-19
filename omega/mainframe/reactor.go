package mainframe

import (
	"fmt"
	"os"
	"path"
	"phoenixbuilder/minecraft/protocol"
	"phoenixbuilder/minecraft/protocol/packet"
	"phoenixbuilder/mirror"
	"phoenixbuilder/mirror/chunk"
	"phoenixbuilder/mirror/define"
	"phoenixbuilder/mirror/io/assembler"
	"phoenixbuilder/mirror/io/lru"
	"phoenixbuilder/mirror/io/mcdb"
	"phoenixbuilder/mirror/io/world"
	"phoenixbuilder/omega/defines"
	"phoenixbuilder/omega/utils"
	"strings"
	"sync"
	"time"

	"github.com/df-mc/goleveldb/leveldb/opt"
	"github.com/pterm/pterm"
)

func (o *Reactor) SetGameMenuEntry(entry *defines.GameMenuEntry) {
	o.GameMenuEntries = append(o.GameMenuEntries, entry)
	interceptor := o.gameMenuEntryToStdInterceptor(entry)
	o.SetGameChatInterceptor(interceptor)
	if entry.FinalTrigger {
		o.GameChatFinalInterceptors = append(o.GameChatFinalInterceptors,
			func(chat *defines.GameChat) (stop bool) {
				return entry.OptionalOnTriggerFn(chat)
			},
		)
	}
	o.freshMenu()
}

func (o *Reactor) gameMenuEntryToStdInterceptor(entry *defines.GameMenuEntry) func(chat *defines.GameChat) (stop bool) {
	return func(chat *defines.GameChat) (stop bool) {
		if !chat.FrameWorkTriggered {
			return false
		}
		if trig, reducedCmds := utils.CanTrigger(chat.Msg, entry.Triggers, o.o.OmegaConfig.Trigger.AllowNoSpace,
			o.o.OmegaConfig.Trigger.RemoveSuffixColor); trig {
			if entry.Verification != nil && entry.Verification.Enable {
				if entry.Verification.ByNameList != nil && len(entry.Verification.ByNameList) > 0 {
					found := false
					for _, n := range entry.Verification.ByNameList {
						if n == chat.Name {
							found = true
							break
						}
					}
					if !found {
						return false
					}
				}
				if entry.Verification.BySelector != "" {
					select {
					case r := <-utils.CheckPlayerMatchSelector(o.o.GameCtrl, chat.Name, entry.Verification.BySelector):
						if !r {
							return false
						}
					case <-time.NewTimer(100 * time.Millisecond).C:
						return false
					}

				}
			}
			_c := chat
			_c.Msg = reducedCmds
			return entry.OptionalOnTriggerFn(_c)
		}
		return false
	}
}

func (o *Reactor) SetGameChatInterceptor(f func(chat *defines.GameChat) (stop bool)) {
	o.GameChatInterceptors = append(o.GameChatInterceptors, f)
}

func (o *Reactor) SetOnAnyPacketCallBack(cb func(packet.Packet)) {
	o.OnAnyPacketCallBack = append(o.OnAnyPacketCallBack, cb)
}

func (o *Reactor) SetOnAnyPacketBytesCallBack(cb func([]byte)) {
	o.OnPacketBytesCbs = append(o.OnPacketBytesCbs, cb)
}

func (o *Reactor) SetOnTypedPacketCallBack(pktID uint32, cb func(packet.Packet)) {
	if _, ok := o.OnTypedPacketCallBacks[pktID]; !ok {
		o.OnTypedPacketCallBacks[pktID] = make([]func(packet2 packet.Packet), 0, 1)
	}
	o.OnTypedPacketCallBacks[pktID] = append(o.OnTypedPacketCallBacks[pktID], cb)
}

func (o *Reactor) SetOnLevelChunkCallBack(fn func(cd *mirror.ChunkData)) {
	o.OnLevelChunkData = append(o.OnLevelChunkData, fn)
}

func (o *Reactor) AppendLoginInfoCallback(cb func(entry protocol.PlayerListEntry)) {
	o.SetOnTypedPacketCallBack(packet.IDPlayerList, func(p packet.Packet) {
		pk := p.(*packet.PlayerList)
		if pk.ActionType == packet.PlayerListActionRemove {
			return
		}
		for _, player := range pk.Entries {
			cb(player)
		}
	})
}

func (o *Reactor) AppendOnBlockUpdateInfoCallBack(cb func(pos define.CubePos, origRTID uint32, currentRTID uint32)) {
	o.BlockUpdateListeners = append(o.BlockUpdateListeners, cb)
}

func (o *Reactor) AppendLogoutInfoCallback(cb func(entry protocol.PlayerListEntry)) {
	o.SetOnTypedPacketCallBack(packet.IDPlayerList, func(p packet.Packet) {
		pk := p.(*packet.PlayerList)
		if pk.ActionType == packet.PlayerListActionAdd {
			return
		}
		for _, player := range pk.Entries {
			cb(player)
		}
	})
}

func (o *Omega) convertTextPacket(p *packet.Text) *defines.GameChat {
	rawName := p.SourceName
	name := utils.ToPlainName(rawName)
	msg := ""
	specialTriggered := false
	if p.TextType == packet.TextTypeWhisper {
		if strings.HasPrefix(p.Message, "CBOMG:") {
			frags := strings.Split(p.Message, ":")
			if len(frags) > 2 {
				_name := strings.TrimSpace(frags[1])
				_msg := strings.TrimSpace(strings.Join(frags[2:], ":"))
				pterm.Warning.Println(_name, _msg)
				for _, p := range o.uqHolder.PlayersByEntityID {
					// pterm.Warning.Println(p.Username)
					if p.Username == _name {
						name = _name
						msg = _msg
						specialTriggered = true
						break
					}
				}
			}
		}

	}
	if !specialTriggered {
		msg = strings.TrimSpace(p.Message)
	}

	msgs := utils.GetStringContents(msg)
	c := &defines.GameChat{
		Name:          name,
		Msg:           msgs,
		Type:          p.TextType,
		RawMsg:        p.Message,
		RawName:       rawName,
		RawParameters: p.Parameters,
	}
	c.FrameWorkTriggered, c.Msg = utils.CanTrigger(
		msgs,
		o.OmegaConfig.Trigger.TriggerWords,
		o.OmegaConfig.Trigger.AllowNoSpace,
		o.OmegaConfig.Trigger.RemoveSuffixColor,
	)
	if specialTriggered {
		c.Type = packet.TextTypeChat
	}
	return c
}
func (o *Reactor) GetTriggerWord() string {
	return o.o.OmegaConfig.Trigger.DefaultTigger
}

func (o *Omega) GetGameListener() defines.GameListener {
	return o.Reactor
}

func (r *Reactor) Throw(chat *defines.GameChat) {
	o := r.o
	flag := true
	catchForParams := false
	if r.o.uqHolder.GetBotName() == chat.Name {
		// fmt.Println("bot ")
	} else {
		if player := o.GetGameControl().GetPlayerKit(chat.Name); player != nil {
			if paramCb := player.GetOnParamMsg(); paramCb != nil {
				if !chat.FrameWorkTriggered {
					catchForParams = paramCb(chat)
				}
			}
		}
	}

	if catchForParams {
		return
	}
	for _, interceptor := range r.GameChatInterceptors {
		if stop := interceptor(chat); stop {
			flag = false
			return
		}
	}
	chat.FallBack = true
	if flag && chat.FrameWorkTriggered {
		for _, interceptor := range r.GameChatFinalInterceptors {
			if stop := interceptor(chat); stop {
				return
			}
		}
	}
}

func (r *Reactor) React(cbPacket *defines.CombinedPacket) {
	pkt := cbPacket.P
	for _, cb := range r.OnPacketBytesCbs {
		cb(cbPacket.D)
	}
	r.analyzer.Update(pkt)
	// if pkt.ID() == packet.IDSubChunk || pkt.ID() == packet.IDLevelChunk {

	// } else {
	// 	M, _ := json.Marshal(pkt)
	// 	m := string(M)
	// 	if strings.Contains(m, "Skin") || strings.Contains(m, "skin") {
	// 		fmt.Println("PacketID ", utils.PktIDInvMapping[int(pkt.ID())], m)
	// 	}
	// }

	choked := make(chan struct{})
	defer func() {
		// fmt.Println("Handled ")
		close(choked)
	}()
	o := r.o
	if pkt == nil {
		return
	}
	pktID := pkt.ID()
	go func() {
		select {
		case <-time.NewTimer(time.Second).C:
			pterm.Error.Println("警告，您的配置文件似乎被您改错了，现在的配置文件使 omega 运行效率低下，甚至可能卡死\n请试着逐个关闭配置文件，以确认具体错误\n如果你很确定自己的配置没有错误，并且这段话出现了很多次 omega 却没有崩溃，那么原因是您的 CPU 性能不足")
			pterm.Error.Printfln("数据包类型为: %v", utils.PktIDInvMapping[int(pktID)])
		case <-choked:
		}
	}()
	switch p := pkt.(type) {
	case *packet.SetDisplayObjective:
		r.scoreboardHolder.UpdateFromSetDisplayPacket(p)
	case *packet.SetScore:
		r.scoreboardHolder.UpdateFromScorePacket(p)
	case *packet.Text:
		// o.backendLogger.Write(fmt.Sprintf("%v(%v):%v", p.SourceName, p.TextType, p.Message))
		chat := o.convertTextPacket(p)
		if chat.Type == packet.TextTypeWhisper && (!o.OmegaConfig.Trigger.AllowWisper) {
			break
		} else {
			r.Throw(chat)
		}

	case *packet.GameRulesChanged:
		for _, rule := range p.GameRules {
			// o.backendLogger.Write(fmt.Sprintf("game rule update %v => %v", rule.Name, rule.Value))
			if rule.Name == "sendcommandfeedback" {
				if rule.Value == true {
					o.GameCtrl.onCommandFeedbackOn()
				} else {
					o.GameCtrl.onCommandFeedBackOff()
				}
			}
		}
		// fmt.Println(p)
	case *packet.PlayerList:
		if p.ActionType == packet.PlayerListActionAdd {
			for _, e := range p.Entries {
				for _, cb := range r.OnKnownPlayerExistCallback {
					cb(e.Username)
				}
			}
		}
	case *packet.CommandOutput:
		o.GameCtrl.onNewCommandFeedBack(p)
	case *packet.UpdateBlock:
		// TODO WIP cannot decide which block are air and which are not
		// TODO remove this line after runtime id mapping update
		// fmt.Println(p.Position, " -> ", p.NewBlockRuntimeID)
		// return
		MCRTID := chunk.NEMCRuntimeIDToStandardRuntimeID(p.NewBlockRuntimeID)
		p.Flags &= 0xf
		if (p.Flags != packet.BlockUpdateNetwork && p.Flags != (packet.BlockUpdateNetwork|packet.BlockUpdateNeighbours)) || p.Layer != 0 {
			// fmt.Println(p, chunk.RuntimeIDToLegacyBlock(MCRTID))
			// break
		}
		// fmt.Println(p, chunk.RuntimeIDToLegacyBlock(MCRTID))
		cubePos := define.CubePos{int(p.Position[0]), int(p.Position[1]), int(p.Position[2])}
		if origBlockRTID, success := r.CurrentWorld.UpdateBlock(cubePos, MCRTID); success {
			for _, cb := range r.BlockUpdateListeners {
				cb(cubePos, origBlockRTID, MCRTID)
			}
		} else {
			for _, cb := range r.BlockUpdateListeners {
				cb(cubePos, chunk.AirRID, MCRTID)
			}
		}
	case *packet.BlockActorData:
		o.GameCtrl.onBlockActor(p)
		cubePos := define.CubePos{int(p.Position[0]), int(p.Position[1]), int(p.Position[2])}
		r.CurrentWorld.SetBlockNbt(cubePos, p.NBTData)
	case *packet.LevelChunk:
		// fmt.Println("packet packet.LevelChunk")
		// TODO Check if level chunk decode is affected by 0 -> -64
		// TODO remove this line after runtime id mapping update
		if exist := r.chunkAssembler.AddPendingTask(p); !exist {
			requests := r.chunkAssembler.GenRequestFromLevelChunk(p)
			r.chunkAssembler.ScheduleRequest(requests)
		}
		// if err := r.CurrentWorldProvider.Write(chunkData); err != nil {
		// 	o.GetBackendDisplay().Write("Decode Chunk Error " + err.Error())
		// } else {
		// 	//fmt.Println("saving chunk @ ", p.ChunkX<<4, p.ChunkZ<<4)
		// }
		// for _, cb := range o.Reactor.OnLevelChunkData {
		// 	cb(chunkData)
		// }
	case *packet.SubChunk:
		// fmt.Println(p.SubChunkX, p.SubChunkY, p.SubChunkZ)
		// fmt.Println("packet packet.SubChunk")
		chunkData := r.chunkAssembler.OnNewSubChunk(p)
		if chunkData != nil {
			if err := r.CurrentWorldProvider.Write(chunkData); err != nil {
				o.GetBackendDisplay().Write("Decode Chunk Error " + err.Error())
			} else {
				// fmt.Println("saving chunk @ ", chunkData.ChunkPos.X()<<4, chunkData.ChunkPos.Z()<<4)
			}
			for _, cb := range o.Reactor.OnLevelChunkData {
				cb(chunkData)
			}
		}
	case *packet.NetworkChunkPublisherUpdate:
		r.chunkAssembler.CancelQueueByPublishUpdate(p)
		// fmt.Println("packet.NetworkChunkPublisherUpdate", p)
	}
	for _, cb := range r.OnAnyPacketCallBack {
		cb(pkt)
	}
	if cbs, ok := r.OnTypedPacketCallBacks[pktID]; ok {
		for _, cb := range cbs {
			cb(pkt)
		}
	}
}

type Reactor struct {
	o                          *Omega
	analyzer                   *PacketInAnalyzer
	OnPacketBytesCbs           []func([]byte)
	OnAnyPacketCallBack        []func(packet.Packet)
	OnTypedPacketCallBacks     map[uint32][]func(packet.Packet)
	OnLevelChunkData           []func(cd *mirror.ChunkData)
	GameMenuEntries            []*defines.GameMenuEntry
	BlockUpdateListeners       []func(pos define.CubePos, origRTID uint32, currentRTID uint32)
	GameChatInterceptors       []func(chat *defines.GameChat) (stop bool)
	GameChatFinalInterceptors  []func(chat *defines.GameChat) (stop bool)
	OnKnownPlayerExistCallback []func(string)
	CurrentWorldProvider       mirror.ChunkProvider
	CurrentWorld               *world.World
	MirrorAvailable            bool
	freshMenu                  func()
	chunkAssembler             *assembler.Assembler
	scoreboardHolder           *defines.ScoreBoardHolder
}

func (o *Reactor) AppendOnKnownPlayerExistCallback(cb func(string)) {
	o.OnKnownPlayerExistCallback = append(o.OnKnownPlayerExistCallback, cb)
}

func (o *Reactor) GetChunkAssembler() *assembler.Assembler {
	return o.chunkAssembler
}

func (o *Reactor) onBootstrap() {
	o.chunkAssembler = assembler.NewAssembler(assembler.REQUEST_NORMAL, time.Minute*5)
	o.chunkAssembler.CreateRequestScheduler(func(pk *packet.SubChunkRequest) {
		o.o.adaptor.Write(pk)
	})
	memoryProvider := lru.NewLRUMemoryChunkCacher(9, true)
	worldDir := path.Join(o.o.GetWorldsDir(), "current")
	fileProvider, err := mcdb.New(worldDir, opt.FlateCompression)
	if err != nil {
		fileProvider = nil
		pterm.Error.Println("创建镜像存档(" + worldDir + ")时出现错误,正在尝试移除文件夹, 错误为" + err.Error())
		if err = os.Rename(worldDir, path.Join(o.o.GetWorldsDir(), "损坏的存档")); err != nil {
			pterm.Error.Println("移除失败，错误为" + err.Error())
			//panic(err)
		}
		if fileProvider, err = mcdb.New(worldDir, opt.FlateCompression); err != nil {
			pterm.Error.Println("修复也失败了，错误为" + err.Error())
			//panic(err)
			fileProvider = nil
		}
		if fileProvider == nil {
			for i := 0; i < 10; i++ {
				pterm.Error.Println("将在没有存档相关功能的情况下运行!")
			}
		}
	} else {
		o.o.GetBackendDisplay().Write(pterm.Success.Sprint("镜像存档@" + worldDir))
		fileProvider.D.LevelName = "MirrorWorld"
	}
	if fileProvider != nil {
		memoryProvider.OverFlowHolder = fileProvider
		memoryProvider.FallBackProvider = fileProvider
	}
	o.CurrentWorldProvider = memoryProvider
	o.CurrentWorld = world.NewWorld(o.CurrentWorldProvider)
	o.o.CloseFns = append(o.o.CloseFns, func() error {
		fmt.Println("正在将世界缓存写入文件")
		memoryProvider.Close()
		if fileProvider != nil {
			fmt.Println("正在关闭反射世界")
			return fileProvider.Close()
		}
		return nil
	})
}

func (o *Omega) GetWorld() *world.World {
	return o.Reactor.CurrentWorld
}

func (o *Omega) GetWorldProvider() mirror.ChunkProvider {
	return o.Reactor.CurrentWorldProvider
}

func (o *Omega) GetScoreboardHolder() *defines.ScoreBoardHolder {
	return o.Reactor.scoreboardHolder
}

type PacketInAnalyzer struct {
	packetSendStats          map[time.Time]map[uint32]int
	packetSendStatsTimeStamp []time.Time
	mu                       sync.Mutex
	currentFiveSecondStats   map[uint32]int
}

func NewPacketInAnalyzer() *PacketInAnalyzer {
	p := &PacketInAnalyzer{
		packetSendStats:          make(map[time.Time]map[uint32]int),
		packetSendStatsTimeStamp: make([]time.Time, 0),
		mu:                       sync.Mutex{},
		currentFiveSecondStats:   make(map[uint32]int),
	}
	go func() {
		t := time.NewTicker(time.Second * 5)
		cmdInfoCounter := 0
		for _ = range t.C {
			cmdInfoCounter++
			t := time.Now()
			p.mu.Lock()
			p.packetSendStatsTimeStamp = append(p.packetSendStatsTimeStamp, t)
			p.packetSendStats[t] = p.currentFiveSecondStats
			p.currentFiveSecondStats = make(map[uint32]int)
			if len(p.packetSendStats) > (600 / 5) {
				timeStampToDrop := p.packetSendStatsTimeStamp[0]
				p.packetSendStatsTimeStamp = p.packetSendStatsTimeStamp[1:]
				delete(p.packetSendStats, timeStampToDrop)
			}
			p.mu.Unlock()
		}
	}()
	return p
}

func (o *PacketInAnalyzer) PrintAnalysis() string {
	o.mu.Lock()
	defer o.mu.Unlock()
	infoStr := "最近十分钟机器人收到数据包的统计信息:\n"
	perStripInfoStrAll := ""
	allPacketsStats := make(map[uint32]int)
	for _, t := range o.packetSendStatsTimeStamp {
		count := 0
		secondsBefore := time.Since(t).Seconds()
		perStripInfoStr := fmt.Sprintf("%.2f ~ %.2f 秒前发送数据包的统计信息:\n", secondsBefore-5, secondsBefore)
		for pkName, pkCount := range o.packetSendStats[t] {
			pktName := utils.PktIDInvMapping[int(pkName)]
			if pktName == "" {
				pktName = fmt.Sprintf("type_%v", pktName)
			}
			perStripInfoStr += fmt.Sprintf("\t%v: %v\n", pktName, pkCount)
			allPacketsStats[pkName] += pkCount
			count += pkCount
		}
		perStripInfoStrAll += perStripInfoStr + fmt.Sprintf("共计 %v 个数据包\n", count)
	}
	count := 0
	for pkName, pkCount := range allPacketsStats {
		infoStr += fmt.Sprintf("\t%v: %v\n", utils.PktIDInvMapping[int(pkName)], pkCount)
		count += pkCount
	}
	infoStr += fmt.Sprintf("共计 %v 个数据包\n", count) + perStripInfoStrAll
	return infoStr
}

func (o *PacketInAnalyzer) Update(p packet.Packet) {
	o.mu.Lock()
	o.currentFiveSecondStats[p.ID()]++
	o.mu.Unlock()
}

func newReactor(o *Omega) *Reactor {
	return &Reactor{
		o:                          o,
		analyzer:                   NewPacketInAnalyzer(),
		GameMenuEntries:            make([]*defines.GameMenuEntry, 0),
		GameChatInterceptors:       make([]func(chat *defines.GameChat) (stop bool), 0),
		GameChatFinalInterceptors:  make([]func(chat *defines.GameChat) (stop bool), 0),
		OnAnyPacketCallBack:        make([]func(packet2 packet.Packet), 0),
		OnTypedPacketCallBacks:     make(map[uint32][]func(packet.Packet), 0),
		OnKnownPlayerExistCallback: make([]func(string), 0),
		OnLevelChunkData:           make([]func(cd *mirror.ChunkData), 0),
		freshMenu:                  func() {},
		scoreboardHolder:           nil,
	}
}

// /scoreboard objectives setdisplay sidebar time
// /scoreboard objectives setdisplay sidebar time2
