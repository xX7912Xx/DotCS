package fatal_control

import (
	"dotcs/args"
	terminate "dotcs/terminate/get_input"
	"dotcs/version"
	"os"
	"runtime"
	"runtime/debug"

	"github.com/c-bata/go-prompt"
	"github.com/pterm/pterm"
)

var PassFatal bool = false

func Fatal() {
	if PassFatal {
		return
	}
	if err := recover(); err != nil {

		pterm.Error.Println("DotCS 在运行过程中出现了问题")
		pterm.Error.Println("错误信息如下:")
		pterm.Error.Println(err)
		pterm.Print("")
		if args.Debug {
			pterm.Error.Println("完整错误信息如下:\n" + string(debug.Stack()))
		}
		if runtime.GOOS == "windows" {
			terminate.Input(
				pterm.Yellow("按下 Enter 退出程序"),
				Code_completer, prompt.OptionTitle("DotCS 专业版 "+version.Version_Plain),
				prompt.OptionSelectedDescriptionTextColor(prompt.Turquoise),
				prompt.OptionInputTextColor(prompt.Green),
				prompt.OptionPrefixTextColor(prompt.Yellow))
		}
		os.Exit(1)
	}
	os.Exit(0)
}
func Code_completer(d prompt.Document) []prompt.Suggest {
	return []prompt.Suggest{
		{Text: d.Text, Description: "按下 Enter 退出程序"},
	}
}
