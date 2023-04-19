// +build !is_tweak

package commands

import (
	"fmt"
	"phoenixbuilder/fastbuilder/types"
	"encoding/json"
	"strings"
)

func TitleRequest(target types.Target, lines ...string) string {
	var items []TellrawItem
	for _, text := range lines {
		items=append(items,TellrawItem{Text:strings.Replace(text, "schematic", "sc***atic", -1)})
	}
	final := &TellrawStruct {
		RawText: items,
	}
	content, _ := json.Marshal(final)
	cmd := fmt.Sprintf("titleraw %v actionbar %s", target, content)
	return cmd
}

func (sender *CommandSender) Title(message string) error {
	return sender.SendSizukanaCommand(TitleRequest(types.AllPlayers, message))
}