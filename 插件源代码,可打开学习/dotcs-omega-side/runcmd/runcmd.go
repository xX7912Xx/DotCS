package runcmd

import (
	"dotcs_mod/utils"
	"fmt"
	"io"
	"os"
	"os/exec"
	"path"
	"runtime"
	"strings"

	"github.com/pterm/pterm"
	"golang.org/x/text/encoding/simplifiedchinese"
)

func RunCmd(subProcessName string, cmdStr string, remapping map[string]string, execDir string) (err error) {
	for k, v := range remapping {
		cmdStr = strings.ReplaceAll(cmdStr, k, v)
	}

	cmds := strings.Split(cmdStr, " ")
	execName := ""
	args := []string{}
	i := 0
	for _, frag := range cmds {
		if frag == "" {
			continue
		}
		i++
		if i == 1 {
			execName = frag
		} else {
			args = append(args, frag)
		}
	}
	cmd := exec.Command(execName, args...)
	if !path.IsAbs(execDir) {
		wd, _ := os.Getwd()
		execDir = path.Join(wd, execDir)
	}
	if runtime.GOOS == "windows" {
		execDir = strings.ReplaceAll(execDir, "\\", "/")
	}
	cmd.Dir = execDir
	// cmd.Env = append(cmd.Env,
	// 	"PATH="+execDir,
	// )
	pterm.Info.Println("工作目录 " + execDir)

	// cmd Stdout
	var cmdOut io.Reader
	cmdOut, err = cmd.StdoutPipe()
	if err != nil {
		return fmt.Errorf("get std out pipe of %v fail, error %v", subProcessName, err)
	}
	if runtime.GOOS == "windows" {
		cmdOut = simplifiedchinese.GBK.NewDecoder().Reader(cmdOut)
	}
	go io.Copy(utils.GenerateMCColorReplacerWriter(os.Stdout), cmdOut)

	// cmd Std err
	cmdErr, err := cmd.StderrPipe()
	if err != nil {
		return fmt.Errorf("get std err pipe of %v fail, error %v", subProcessName, err)
	}
	go io.Copy(os.Stderr, cmdErr)
	err = cmd.Start()
	if err != nil {
		return err
	}
	go cmd.Wait()
	return nil
}
func RunCmd_no_title(subProcessName string, cmdStr string, remapping map[string]string, execDir string) (text string, err error) {
	for k, v := range remapping {
		cmdStr = strings.ReplaceAll(cmdStr, k, v)
	}

	cmds := strings.Split(cmdStr, " ")
	execName := ""
	args := []string{}
	i := 0
	for _, frag := range cmds {
		if frag == "" {
			continue
		}
		i++
		if i == 1 {
			execName = frag
		} else {
			args = append(args, frag)
		}
	}
	cmd := exec.Command(execName, args...)
	out, err := cmd.CombinedOutput()
	return string(out), err
}
