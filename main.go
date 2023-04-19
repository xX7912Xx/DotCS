package main

import (
	"bufio"
	"encoding/json"
	"fmt"
	"io/ioutil"
	"os"
	"os/exec"
	"path/filepath"
	"phoenixbuilder/fastbuilder/args"
	"phoenixbuilder/fastbuilder/core"
	I18n "phoenixbuilder/fastbuilder/i18n"
	script_bridge "phoenixbuilder/fastbuilder/script_engine/bridge"
	"phoenixbuilder/fastbuilder/utils"
	"strings"
	"syscall"

	"github.com/pterm/pterm"
	"golang.org/x/term"

	"phoenixbuilder/fastbuilder/readline"
	_ "phoenixbuilder/io"
	_ "phoenixbuilder/plantform_specific/fix_timer"
)

func main() {
	args.ParseArgs()
	if len(args.PackScripts()) != 0 {
		os.Exit(script_bridge.MakePackage(args.PackScripts(), args.PackScriptsOut()))
	}
	pterm.Error.Prefix = pterm.Prefix{
		Text:  "ERROR",
		Style: pterm.NewStyle(pterm.BgBlack, pterm.FgRed),
	}

	I18n.Init()
	pterm.Println("_______   ______   .___________.  ______     _______.")
	pterm.Println("|       \\ /  __  \\  |           | /      |   /       |")
	pterm.Println("|  .--.  |  |  |  | `---|  |----`|  ,----'  |   (----`")
	pterm.Println("|  |  |  |  |  |  |     |  |     |  |        \\   \\    ")
	pterm.Println("|  '--'  |  `--'  |     |  |     |  `----.----)   |   ")
	pterm.Println("|_______/ \\______/      |__|      \\______|_______/    ")
	pterm.Println("													  \n")
	pterm.DefaultBox.Println(pterm.LightCyan("https://dotcs.mcppl.cn"))
	pterm.Println(pterm.Yellow("DotCS Pro " + args.GetFBVersion()))
	pterm.Println("DotCS 基于 PhoenixBuilder 制作")
	pterm.Println("为确保兼容旧版 DotCS 插件,使用DotCS的同时将同时启用Omega,且默认启用与DotCS有关的组件,此版本为修改版的omega")
	// iSH.app specific, for foreground ability
	if _, err := os.Stat("/dev/location"); err == nil {
		// Call location service
		pterm.Println(pterm.Yellow(I18n.T(I18n.Notice_iSH_Location_Service)))
		cmd := exec.Command("ash", "-c", "cat /dev/location > /dev/null &")
		err := cmd.Start()
		if err != nil {
			fmt.Println(err)
		}
	}

	if !args.NoReadline() {
		readline.InitReadline()
	}

	if I18n.ShouldDisplaySpecial() {
		fmt.Printf("%s", I18n.T(I18n.Special_Startup))
	}

	defer core.Fatal()
	if args.DebugMode() {
		init_and_run_debug_client()
		return
	}
	if !args.ShouldDisableHashCheck() {
		fmt.Printf(I18n.T(I18n.Notice_CheckUpdate))
		hasUpdate, latestVersion := utils.CheckUpdate(args.GetFBVersion())
		fmt.Printf(I18n.T(I18n.Notice_OK))
		if hasUpdate {
			fmt.Printf(I18n.T(I18n.Notice_UpdateAvailable), latestVersion)
			fmt.Printf(I18n.T(I18n.Notice_UpdateNotice))
			// To ensure user won't ignore it directly, can be suppressed by command line argument.
			os.Exit(0)
		}
	}

	if !args.SpecifiedToken() {
		token := loadTokenPath()
		if _, err := os.Stat(token); os.IsNotExist(err) {
			fbusername, err := getInputUserName()
			if err != nil {
				panic(err)
			}
			fbuntrim := fmt.Sprintf("%s", strings.TrimSuffix(fbusername, "\n"))
			fbun := strings.TrimRight(fbuntrim, "\r\n")
			fmt.Printf(I18n.T(I18n.EnterPasswordForFBUC))
			fbpassword, err := term.ReadPassword(int(syscall.Stdin))
			fmt.Printf("\n")
			tokenstruct := &map[string]interface{}{
				"encrypt_token": true,
				"username":      fbun,
				"password":      string(fbpassword),
			}
			token, err := json.Marshal(tokenstruct)
			if err != nil {
				fmt.Println(I18n.T(I18n.FBUC_Token_ErrOnGen))
				fmt.Println(err)
				return
			}
			runInteractiveClient(string(token))

		} else {
			token, err := readToken(token)
			if err != nil {
				fmt.Println(err)
				return
			}
			runInteractiveClient(token)
		}
	} else {
		runInteractiveClient(args.CustomTokenContent())
	}
}

func runInteractiveClient(token string) {
	pterm.Println(pterm.Yellow("连接租赁服中,请稍后"))
	var code, serverPasswd string
	var err error
	if !args.SpecifiedServer() {
		code, serverPasswd, err = getRentalServerCode()
	} else {
		code = args.ServerCode()
		serverPasswd = args.ServerPassword()
	}

	if err != nil {
		fmt.Println(err)
		return
	}
	env := core.InitRealEnvironment(token, code, serverPasswd)
	ptoken_succ := core.ProcessTokenDefault(env)
	//init_and_run_client(token, code, serverPasswd)
	if !ptoken_succ {
		panic("Failed to load token")
	}
	core.InitClient(env)
	go core.EnterReadlineThread(env, nil)
	defer core.DestroyClient(env)
	core.EnterWorkerThread(env, nil)
}

func init_and_run_debug_client() {
	env := core.InitDebugEnvironment()
	core.InitClient(env)
	go core.EnterReadlineThread(env, nil)
	defer core.DestroyClient(env)
	core.EnterWorkerThread(env, nil)
}

func getInput() (string, error) {
	reader := bufio.NewReader(os.Stdin)
	inp, err := reader.ReadString('\n')
	inpl := strings.TrimRight(inp, "\r\n")
	return inpl, err
}

func getInputUserName() (string, error) {
	reader := bufio.NewReader(os.Stdin)
	pterm.Printf(I18n.T(I18n.Enter_FBUC_Username))
	fbusername, err := reader.ReadString('\n')
	return fbusername, err
}

func getRentalServerCode() (string, string, error) {
	reader := bufio.NewReader(os.Stdin)
	fmt.Printf(I18n.T(I18n.Enter_Rental_Server_Code))
	code, err := reader.ReadString('\n')
	if err != nil {
		return "", "", err
	}
	fmt.Printf(I18n.T(I18n.Enter_Rental_Server_Password))
	bytePassword, err := term.ReadPassword(int(syscall.Stdin))
	fmt.Printf("\n")
	return strings.TrimRight(code, "\r\n"), string(bytePassword), err
}

func readToken(path string) (string, error) {
	content, err := ioutil.ReadFile(path)
	if err != nil {
		return "", err
	}
	return string(content), nil
}

func loadTokenPath() string {
	homedir, err := os.UserHomeDir()
	if err != nil {
		fmt.Println(I18n.T(I18n.Warning_UserHomeDir))
		homedir = "."
	}
	fbconfigdir := filepath.Join(homedir, ".config/dotcs")
	os.MkdirAll(fbconfigdir, 0700)
	token := filepath.Join(fbconfigdir, "dotcstoken")
	return token
}
