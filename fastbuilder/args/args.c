#include <stdio.h>
#include <stdlib.h>
#include <getopt.h>
#include <string.h>
#include <dirent.h>
#include <errno.h>
#ifndef PATH_MAX
#include <limits.h>
#endif
#include <sys/types.h>

#ifndef FB_VERSION
#define FB_VERSION "(CUSTOM)"
#define FB_COMMIT "???"
#define FB_COMMIT_LONG "???"
#warning "It seems that you're building PhoenixBuilder with plain `go build` command, it is highly recommended to use `make current` instead."
#endif

char args_isDebugMode=0;
char args_disableHashCheck=0;
char replaced_auth_server=0;
char *newAuthServer;
char args_muteWorldChat=0;
char args_noPyRpc=1;
char use_startup_script=0;
char *startup_script;
char specified_server=0;
char *server_code;
char *server_password="";
char custom_token=0;
char *token_content;
char *externalListenAddr="";
char *capture_output_file="";
char args_no_readline=0;
char *pack_scripts="";
char *pack_scripts_out="";
char enable_omega_system=0;
char *custom_gamename="";
char ingame_response=0;

extern void custom_script_engine_const(const char *key, const char *val);
extern void do_suppress_se_const(const char *key);

void print_help(const char *self_name) {
	printf("%s [options]\n",self_name);
	printf("\t--debug: Run in debug mode.\n");
	printf("\t-A <url>, --auth-server=<url>: Use the specified authentication server, instead of the default one.\n");
	printf("\t--no-update-check: Suppress update notifications.\n");
	printf("\t-M, --no-world-chat: Ignore world chat on client side.\n");
	printf("\t--force-pyrpc: Enable the PyRpcPacket interaction, client will be kicked automatically by netease's rental server.\n");
#ifdef WITH_V8
	printf("\t-S, --script=<*.js>: run a .js script at start\n");
	printf("\t--script-engine-const key=value: Define a const value for script engine's \"consts\" const. Can be used to replace the default value. Specify multiple items by using this argument for multiple times.\n");
	printf("\t--script-engine-suppress-const <key>: Undefine a const value for script engine's \"consts\" const. Specify multiple items by using this argument for multiple times.\n");
#endif
	printf("\t-c, --code=<server code>: Specify a server code.\n");
	printf("\t-p, --password=<server password>: Specify the password of the server specified by -c.\n");
	printf("\t-t, --token=<path of DotCSToken>: Specify the path of DotCSToken, and quit if the file is unaccessible.\n");
	printf("\t-T, --plain-token=<token>: Specify the token content.\n");
	printf("\t-E, --listen-external: Listen on the specified address and wait for external controlling connection.\n\t\tExample: -E 0.0.0.0:5768 - listen on port 5768 and accept connections from anywhere,\n\t\t\t-E 127.0.0.1:5769 - listen on port 5769 and accept connections from localhost only.\n");
	printf("\t--capture=<*.bin>: Capture minecraft packet and dump to target file\n");
	printf("\t--no-readline: Suppress user input.\n");
	printf("\t--pack-scripts <manifest path>: Create a script package.\n");
	printf("\t--pack-scripts-to <path>: Specify the path for the output script package.\n");
	printf("\t-N, --gamename <name>: Specify the game name to use interactive commands (e.g. get), instead of using the server provided one.\n");
	printf("\t--ingame-response: Turn on the feature to listen to commands or give output in game.\n");
	printf("\t--del-userdata: Remove user data and exit.\n");
	printf("\t-h, --help: Show this help context.\n");
	printf("\t-v, --version: Show the version information of this program.\n");
	printf("\t\t--version-plain: Show the version of this program.\n");
}

char *get_fb_version() {
#ifdef FBGUI_VERSION
	return FB_VERSION "@" FBGUI_VERSION " (" FB_COMMIT ")";
#else
	return FB_VERSION " (" FB_COMMIT ")";
#endif
}

char *get_fb_plain_version() {
#ifdef FBGUI_VERSION
	return FBGUI_VERSION;
#else
	return FB_VERSION;
#endif
}

char *commit_hash() {
	return FB_COMMIT_LONG;
}

void print_version(int detailed) {
	if(!detailed) {
		printf(FB_VERSION "\n");
		return;
	}
	printf("PhoenixBuilder " FB_VERSION "\n");
#ifdef FBGUI_VERSION
	printf("With GUI " FBGUI_VERSION "\n");
#endif
#ifdef WITH_V8
	printf("With V8 linked.\n");
#endif
	printf("COMMIT " FB_COMMIT_LONG "\n");
	printf("\n");
}

void read_token(char *token_path) {
	FILE *file=fopen(token_path,"rb");
	if(!file) {
		fprintf(stderr, "Failed to read token at %s.\n",token_path);
		exit(21);
	}
	fseek(file,0,SEEK_END);
	size_t flen=ftell(file);
	fseek(file,0,SEEK_SET);
	token_content=malloc(flen+1);
	token_content[flen]=0;
	fread(token_content, 1, flen, file);
	fclose(file);
}

void quickcopy(char **target_ptr) {
	size_t length=strlen(optarg)+1;
	*target_ptr=malloc(length);
	memcpy(*target_ptr, optarg, length);
}

#ifdef DT_UNKNOWN

void rmdir_recursive(char *path) {
	char *pathend=path+strlen(path);
	DIR *fbdir=opendir(path);
	if(!fbdir) {
		if(errno==ENOENT) {
			return;
		}
		fprintf(stderr, "Failed to open directory [%s]: %s\n", path, strerror(errno));
		exit(1);
	}
	struct dirent *dir_ent;
	while((dir_ent=readdir(fbdir))!=NULL) {
		if(dir_ent->d_type==DT_UNKNOWN) {
			fprintf(stderr, "Found file with unknown type: %s\n", path);
			exit(2);
		}
		if(dir_ent->d_type!=DT_DIR) {
			sprintf(pathend,"%s",dir_ent->d_name);
			remove(path);
		}else{
			if((dir_ent->d_name[0]=='.'&&dir_ent->d_name[1]==0)||(dir_ent->d_name[0]=='.'&&dir_ent->d_name[1]=='.'&&dir_ent->d_name[2]==0)){
				continue;
			}
			sprintf(pathend,"%s/",dir_ent->d_name);
			rmdir_recursive(path);
			remove(path);
		}
	}
	closedir(fbdir);
	*pathend=0;
}

#else

void go_rmdir_recursive(char *path);
void rmdir_recursive(char *path) {
	go_rmdir_recursive(path);
}

#endif

void config_cleanup() {
	char *home_dir=getenv("HOME");
	if(home_dir==NULL) {
		fprintf(stderr, "Failed to obtain user's home directory, using \".\" instead.\n");
		home_dir=".";
	}
	char *buf=malloc(PATH_MAX);
	sprintf(buf, "%s", home_dir);
	char *concat_start=buf+strlen(buf);
	sprintf(concat_start,"/.config/dotcs/");
	rmdir_recursive(buf);
	remove(buf);
	free(buf);
	exit(0);
}

int _parse_args(int argc, char **argv) {
	while(1) {
		static struct option opts[]={
			{"debug", no_argument, 0, 0}, // 0
			{"help", no_argument, 0, 'h'}, // 1
			{"auth-server", required_argument, 0, 'A'}, //2
			{"no-update-check", no_argument, 0, 0}, //3
			{"no-world-chat", no_argument, 0, 'M'}, //4
			{"force-pyrpc", no_argument, 0, 0}, //5
			{"no-nbt", no_argument, 0, 0}, //6
			{"script", required_argument, 0, 'S'}, //7
			{"version", no_argument, 0, 'v'}, //8
			{"version-plain", no_argument, 0, 0}, //9
			{"code", required_argument, 0, 'c'}, //10
			{"password", required_argument, 0, 'p'}, //11
			{"token", required_argument, 0, 't'}, //12
			{"plain-token", required_argument, 0, 'T'}, //13
			{"script-engine-const", required_argument, 0, 0}, //14
			{"script-engine-suppress-const", required_argument, 0, 0}, //15
			{"listen-external", required_argument, 0, 'E'}, // 16
			{"no-readline", no_argument, 0, 0}, //17
			{"pack-scripts", required_argument, 0, 0}, //18
			{"pack-scripts-to", required_argument, 0, 0}, //19
			{"capture", required_argument, 0, 0}, // 20
			{"gamename", required_argument, 0, 'N'}, // 21
			{"ingame-response", no_argument, 0, 0}, // 22
			{"del-userdata", no_argument, 0, 0}, // 23
			{0, 0, 0, 0}
		};
		int option_index;
		int c=getopt_long(argc,argv,"hA:MvS:c:p:t:T:ON:", opts, &option_index);
		if(c==-1)
			break;
		switch(c) {
		case 0:
			switch(option_index) {
			case 0:
				args_isDebugMode=1;
				break;
			case 3:
				args_disableHashCheck=1;
				break;
			case 5:
				args_noPyRpc=0;
				break;
			case 6:
				fprintf(stderr, "--no-nbt option is no longer available.\n");
				return 10;
				break;
			case 9:
				print_version(0);
				return 0;
			case 14:
#ifndef WITH_V8
				fprintf(stderr,"--script-engine-const argument isn't available: Non-v8-linked version.\n");
				return 10;
#endif
				{
					int break_switch_14=0;
					for(char *ptr=optarg;*ptr!=0;ptr++) {
						if(*ptr=='=') {
							*ptr=0;
							ptr++;
							custom_script_engine_const(optarg, ptr);
							break_switch_14=1;
							break;
						}
					}
					if(break_switch_14)break;
					fprintf(stderr, "--script-engine-const: Format: key=val\n");
					print_help(argv[0]);
					return 1;
				}
			case 15:
#ifndef WITH_V8
				fprintf(stderr,"--script-engine-suppress-const argument isn't available: Non-v8-linked version.\n");
				return 10;
#endif
				do_suppress_se_const(optarg);
				break;
			case 17:
				args_no_readline=1;
				break;
			case 18:
				quickcopy(&pack_scripts);
				break;
			case 19:
				quickcopy(&pack_scripts_out);
				break;
			case 20:
				quickcopy(&capture_output_file);
				break;
			case 22:
				ingame_response=1;
				break;
			case 23:
				config_cleanup();
				break;
			};
			break;
		case 'h':
			print_help(argv[0]);
			return 0;
		case 'A':
			replaced_auth_server=1;
			quickcopy(&newAuthServer);
			break;
		case 'M':
			args_muteWorldChat=1;
			break;
		case 'S':
#ifndef WITH_V8
			fprintf(stderr,"-S, --script option isn't available: No V8 linked for this version.\n");
			return 10;
#endif
			use_startup_script=1;
			quickcopy(&startup_script);
			break;
		case 'c':
			specified_server=1;
			quickcopy(&server_code);
			break;
		case 'p':
			specified_server=1;
			quickcopy(&server_password);
			break;
		case 't':
			custom_token=1;
			read_token(optarg);
			break;
		case 'T':
			custom_token=1;
			quickcopy(&token_content);
			break;
		case 'E':
			quickcopy(&externalListenAddr);
			break;
		case 'v':
			print_version(1);
			return 0;
		case 'N':
			quickcopy(&custom_gamename);
			break;
		default:
			print_help(argv[0]);
			return 1;
		};
	};
	return -1;
}

void parse_args(int argc, char **argv) {
	int ec;
	if((ec=_parse_args(argc,argv))!=-1) {
		exit(ec);
	}
	return;
}
