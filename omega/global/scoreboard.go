package global

import (
	"fmt"
	"phoenixbuilder/minecraft/protocol/packet"
	"phoenixbuilder/omega/defines"
	"strconv"
	"sync"
	"time"
)

var rankingLastFetchTime time.Time
var rankingLastFetchResult map[string]map[string]int
var rankingWaiter []func(map[string]map[string]int)
var rankingWaiterLock sync.Mutex

func UpdateScore(ctrl defines.GameControl, allowDuration time.Duration, onUpdateDone func(map[string]map[string]int)) {
	rankingWaiterLock.Lock()
	if rankingLastFetchResult != nil {
		if time.Since(rankingLastFetchTime) < allowDuration+time.Second {
			onUpdateDone(rankingLastFetchResult)
		}
	}
	rankingWaiterLock.Unlock()
	rankingWaiterLock.Lock()
	if rankingWaiter != nil {
		rankingWaiter = append(rankingWaiter, onUpdateDone)
		rankingWaiterLock.Unlock()
		return
	} else {
		rankingWaiter = make([]func(map[string]map[string]int), 0)
		rankingWaiterLock.Unlock()
	}
	ctrl.SendCmdAndInvokeOnResponse("scoreboard players list @a", func(output *packet.CommandOutput) {
		// fmt.Println(output)
		fetch := func(output *packet.CommandOutput) (result map[string]map[string]int) {
			currentPlayer := ""
			fetchResult := map[string]map[string]int{}

			for _, msg := range output.OutputMessages {
				if !msg.Success {
					continue
				}
				if len(msg.Parameters) == 2 {
					_currentPlayer := msg.Parameters[1]
					if len(_currentPlayer) > 1 {
						currentPlayer = _currentPlayer[1:]
					} else {
						return
					}
				} else if len(msg.Parameters) == 3 {
					valStr, scoreboardName := msg.Parameters[0], msg.Parameters[2]
					val, err := strconv.Atoi(valStr)
					if err != nil {
						return
					}
					if players, hasK := fetchResult[scoreboardName]; !hasK {
						fetchResult[scoreboardName] = map[string]int{currentPlayer: val}
					} else {
						players[currentPlayer] = val
					}
				} else {
					continue
				}
			}
			return fetchResult
		}
		if result := fetch(output); result == nil {
			fmt.Println("cannot get scoreboard result")
		} else {
			rankingLastFetchResult = result
			rankingLastFetchTime = time.Now()
			onUpdateDone(rankingLastFetchResult)
			rankingWaiterLock.Lock()
			for _, cb := range rankingWaiter {
				cb(rankingLastFetchResult)
			}
			rankingWaiter = nil
			rankingWaiterLock.Unlock()
		}
	})
}
