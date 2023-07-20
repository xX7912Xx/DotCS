package environment

import (
	"dotcs/utils"
	"fmt"
	"path"
	"strings"

	"github.com/pterm/pterm"
)

func (d *PBEnvironment) BootstrapDirs() {
	d.Mkdir(pterm.Yellow("创建插件文件夹:"), d.GetPath("plugins"))
}
func (d *PBEnvironment) Mkdir(tip string, path string) {
	if !utils.IsDir(path) {
		pterm.Println(tip + pterm.Green(path))
		if err := utils.MakeDirP(path); err != nil {
			panic(err)
		}
	}
}
func (d *PBEnvironment) GetPath(elem ...string) string {
	for _, ele := range elem {
		if strings.HasPrefix(ele, "/") || strings.Contains(ele, "..") {
			panic(fmt.Errorf("为了安全考虑，路径开头不能为 / 且不能包含 .."))
		}
	}
	return path.Join(d.storageRoot, path.Join(elem...))
}
