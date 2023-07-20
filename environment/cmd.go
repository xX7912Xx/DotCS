package environment

import (
	"dotcs/utils"
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

func (o *PBEnvironment) RunCmd(subProcessName string, cmdStr string, remapping map[string]string, execDir string) (err error) {
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
	if execName == "" {
		pterm.Info.Println("启动子进程[" + subProcessName + "]: " + cmdStr + " 失败: 未指定 程序名")
		return
	} else {
		// pterm.Info.Println("启动子进程["+subProcessName+"]: "+cmdStr+" => 标准化为", strings.Join([]string{pterm.Yellow(execName), pterm.Blue(strings.Join(args, " "))}, " "))
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
func (o *PBEnvironment) RunPip(cmdStr string, remapping map[string]string) (err error) {
	execDir := "."
	cmdStr = fmt.Sprintf("%s -m %s", o.PythonPath, cmdStr)
	if find := strings.Contains(cmdStr, "install "); find {
		if find := strings.Contains(cmdStr, "-i"); !find {
			cmdStr = fmt.Sprintf("%s -i https://pypi.tuna.tsinghua.edu.cn/simple", cmdStr)
		}
	}
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
	if execName == "" {
		pterm.Info.Println("执行命令: " + cmdStr + " 失败: 未指定 程序名")
		return
	} else {
		// pterm.Info.Println("启动子进程["+subProcessName+"]: "+cmdStr+" => 标准化为", strings.Join([]string{pterm.Yellow(execName), pterm.Blue(strings.Join(args, " "))}, " "))
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

	// cmd Stdout
	var cmdOut io.Reader
	cmdOut, err = cmd.StdoutPipe()
	if err != nil {
		return fmt.Errorf("get std out pipe of %v fail, error %v", cmdStr, err)
	}
	if runtime.GOOS == "windows" {
		cmdOut = simplifiedchinese.GBK.NewDecoder().Reader(cmdOut)
	}
	go io.Copy(utils.GenerateMCColorReplacerWriter(os.Stdout), cmdOut)

	// cmd Std err
	cmdErr, err := cmd.StderrPipe()
	if err != nil {
		return fmt.Errorf("get std err pipe of %v fail, error %v", cmdStr, err)
	}
	go io.Copy(os.Stderr, cmdErr)
	err = cmd.Start()
	if err != nil {
		return err
	}
	cmd.Wait()
	return nil
}
func (o *PBEnvironment) RunPython(cmdStr string, remapping map[string]string) (err error) {
	execDir := "."
	cmdStr = fmt.Sprintf("%s %s", o.PythonPath, cmdStr)
	if find := strings.Contains(cmdStr, "install "); find {
		if find := strings.Contains(cmdStr, "-i"); !find {
			cmdStr = fmt.Sprintf("%s -i https://pypi.tuna.tsinghua.edu.cn/simple", cmdStr)
		}
	}
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
	if execName == "" {
		pterm.Info.Println("执行命令: " + cmdStr + " 失败: 未指定 程序名")
		return
	} else {
		// pterm.Info.Println("启动子进程["+subProcessName+"]: "+cmdStr+" => 标准化为", strings.Join([]string{pterm.Yellow(execName), pterm.Blue(strings.Join(args, " "))}, " "))
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

	// cmd Stdout
	var cmdOut io.Reader
	cmdOut, err = cmd.StdoutPipe()
	if err != nil {
		return fmt.Errorf("get std out pipe of %v fail, error %v", cmdStr, err)
	}
	if runtime.GOOS == "windows" {
		cmdOut = simplifiedchinese.GBK.NewDecoder().Reader(cmdOut)
	}
	go io.Copy(utils.GenerateMCColorReplacerWriter(os.Stdout), cmdOut)

	// cmd Std err
	cmdErr, err := cmd.StderrPipe()
	if err != nil {
		return fmt.Errorf("get std err pipe of %v fail, error %v", cmdStr, err)
	}
	go io.Copy(os.Stderr, cmdErr)
	err = cmd.Start()
	if err != nil {
		return err
	}
	go cmd.Wait()
	return nil
}
