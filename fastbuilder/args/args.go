package args

import (
	"os"
	"unsafe"
)

/*
extern void free(void *);

extern char args_isDebugMode;
extern char replaced_auth_server;
extern char *newAuthServer;
extern char args_disableHashCheck;
extern char args_muteWorldChat;
extern char args_noPyRpc;
extern char *startup_script;

extern void parse_args(int argc, char **argv);

extern char use_startup_script;
extern char *get_fb_version(void);
extern char *get_fb_plain_version(void);
extern char *commit_hash(void);

extern char specified_server;
extern char *server_code;
extern char *server_password;
extern char custom_token;
extern char *token_content;
extern char *externalListenAddr;
extern char *capture_output_file;
extern char args_no_readline;
extern char *pack_scripts;
extern char *pack_scripts_out;
extern char *custom_gamename;

extern char enable_omega_system;
extern char ingame_response;
*/
import "C"

func charify(val bool) C.char {
	if val {
		return C.char(1)
	} else {
		return C.char(0)
	}
}

func Set_args_isDebugMode(val bool) {
	C.args_isDebugMode = charify(val)
}

func Do_replace_authserver(val string) {
	if boolify(C.replaced_auth_server) {
		C.free(unsafe.Pointer(C.newAuthServer))
	} else {
		C.replaced_auth_server = C.char(1)
	}
	C.newAuthServer = C.CString(val)
}

func Set_disableHashCheck(val bool) {
	C.args_disableHashCheck = charify(val)
}

func Set_muteWorldChat(val bool) {
	C.args_muteWorldChat = charify(val)
}

func Set_noPyRpc(val bool) {
	C.args_noPyRpc = charify(val)
}

func GetFBVersion() string {
	return C.GoString(C.get_fb_version())
}

func GetFBPlainVersion() string {
	return C.GoString(C.get_fb_plain_version())
}

func GetFBCommitHash() string {
	return C.GoString(C.commit_hash())
}

var ParsedArgs []string=[]string{}

func ParseArgs() {
	argv := make([]*C.char, len(os.Args))
	for i, v := range os.Args {
		cstr := C.CString(v)
		defer C.free(unsafe.Pointer(cstr))
		argv[i] = cstr
	}
	C.parse_args(C.int(len(os.Args)), &argv[0])
	ParsedArgs=append([]string{}, os.Args...)
}

func ParseCustomArgs(customArgs []string) {
	argv := make([]*C.char, len(customArgs))
	for i, v := range customArgs {
		cstr := C.CString(v)
		defer C.free(unsafe.Pointer(cstr))
		argv[i] = cstr
	}
	C.parse_args(C.int(len(customArgs)), &argv[0])
	ParsedArgs=append([]string{}, customArgs...)
}

func boolify(v C.char) bool {
	if int(v) == 0 {
		return false
	}
	return true
}

func DebugMode() bool {
	if int(C.args_isDebugMode) == 0 {
		return false
	}
	return true
}

func AuthServer() string {
	if int(C.replaced_auth_server) == 0 {
		return "wss://api.fastbuilder.pro:2053/"
	}
	return C.GoString(C.newAuthServer)
}

func ShouldDisableHashCheck() bool {
	return boolify(C.args_disableHashCheck)
}

func ShouldEnableOmegaSystem() bool {
	return boolify(C.enable_omega_system)
}

func SetShouldDisableHashCheck() {
	C.args_disableHashCheck = C.char(1)
}

func ShouldMuteWorldChat() bool {
	return boolify(C.args_muteWorldChat)
}

func NoPyRpc() bool {
	return boolify(C.args_noPyRpc)
}

func StartupScript() string {
	if int(C.use_startup_script) == 0 {
		return ""
	}
	return C.GoString(C.startup_script)
}

func SpecifiedServer() bool {
	return boolify(C.specified_server)
}

func ServerCode() string {
	if int(C.specified_server) == 0 {
		return ""
	}
	return C.GoString(C.server_code)
}

func ServerPassword() string {
	// No need to check as its default value is "".
	return C.GoString(C.server_password)
}

func SpecifiedToken() bool {
	return boolify(C.custom_token)
}

func CustomTokenContent() string {
	if int(C.custom_token) == 0 {
		return ""
	}
	return C.GoString(C.token_content)
}

var CustomSEConsts map[string]string = map[string]string{}
var CustomSEUndefineConsts []string = []string{}

//export custom_script_engine_const
func custom_script_engine_const(key, val *C.char) {
	CustomSEConsts[C.GoString(key)] = C.GoString(val)
}

//export do_suppress_se_const
func do_suppress_se_const(key *C.char) {
	CustomSEUndefineConsts = append(CustomSEUndefineConsts, C.GoString(key))
}

func ExternalListenAddress() string {
	return C.GoString(C.externalListenAddr)
}

func CaptureOutputFile() string {
	return C.GoString(C.capture_output_file)
}

func NoReadline() bool {
	return boolify(C.args_no_readline)
}

func PackScripts() string {
	return C.GoString(C.pack_scripts)
}

func PackScriptsOut() string {
	return C.GoString(C.pack_scripts_out)
}

func GetCustomGameName() string {
	return C.GoString(C.custom_gamename)
}

func InGameResponse() bool {
	return boolify(C.ingame_response)
}

//export cexporttestfunc
func cexporttestfunc() string {
	return "test succ"
}

//export go_rmdir_recursive
func go_rmdir_recursive(path *C.char) {
	err:=os.RemoveAll(C.GoString(path))
	if err!=nil {
		panic(err)
	}
}
