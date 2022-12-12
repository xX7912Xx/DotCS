import __main__ # 这个是必须要在开头导入的,要不然导入会失效

import socket
import threading
import time
import os
import json
import asyncio

function_cmd = __main__.function_cmd
@__main__.plugin_load # 必写,作用是导入插件
class __init__(__main__.plugin):
    __version__             = "1.0" # 版本号,默认值是 1.0
    __doc__                 = "检测到 .help 就返回信息" # 帮助文档,默认值 :""
    __author__              = "我不是Art" # 作者名,默认值: "未知的作者"
    __update_url__          = None # 更新链接,默认值是 None
    __license_agreement__   = "见帮助文档" # 许可协议,默认值: "见帮助文档" 
    

    DESCRIPTION = "RentalServerLink made by 2401 & SuperScript"
    online = False
    
    channel = "默认大区"

    def __init__(self,Name:str,Version:str,Mode:int):# 初始化操作函数!!!
        # 上述参数均是写死的模板!!!
        # Name:用户名
        # Version: DotCS 版本
        # Mode:启动模式(见文档)
        
        "初始化操作" # 这个文档帮助定义可以不写
        # 在加载阶段,您直接判定 库是不明智的,您应当在下面的 initialize 事件中进行管理
        if "plugin.主菜单" not in __main__.PLUGIN_CLASS:
            self.color("§4服服互通插件依赖 §e主菜单 §4插件(如果您已经安装了,请勿改名)!请前往 §bhttps://github.com/xX7912Xx/DotCS/tree/main/plugin §4进行下载")
            del __main__.PLUGIN_CLASS["plugin.服服互通"]

        if "plugin.DotCS_pip" not in __main__.PLUGIN_CLASS:
            # 检测是否有此插件
            self.color("§4服服互通插件依赖 §eDotCS_pip §4插件(如果您已经安装了,请勿改名)!请前往 §bhttps://github.com/xX7912Xx/DotCS/tree/main/plugin §4进行下载")
            try:
                del __main__.PLUGIN_CLASS["plugin.服服互通"]
            except:
                pass
        else:
            try:
                import traceback
            except:
                self.color("§e正在安装依赖库§7:§b traceback")
                __main__.PLUGIN_CLASS["plugin.DotCS_pip"].install("traceback")
                self.color("§a安装依赖库完成§7:§b traceback")
                import traceback
            
    async def initialize(self):
        # 检测是否篡改改名了
        self.connToWsLink = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.addr = ("222.187.232.63", 24013)
        self.color(f"§b您所在的频道大区: {self.channel}")
        self.serverName = self.load_json(os.path.join("配置文件","主菜单","主文件.json"))["server"]
        self.color("§6正在连接到服服互通服务端...") 
        try:  
            self.conn()
            threading.Thread(target = self.recvThread).start()
        except:
            pass
        await asyncio.sleep(6)         
        self.sendmsg(f"§a尊敬的各位朋友,您好")
        await asyncio.sleep(1)         
        self.sendmsg("§a如果您看到此消息,即代表 DotCS Go 正在测试")
        await asyncio.sleep(1) 
        self.sendmsg("§a期间可能会不断的进退")
        await asyncio.sleep(1) 
        self.sendmsg("§a还请谅解")
    async def player_say(self,player,msg:str,title):
        self.sendmsg(f"§r<§b{player}§r> §r{msg}")
    def multiJSONHandle(self,__json: str):
        charIndex = __json.find("}") + 1
        try:
            if __json[charIndex] == "{":
                return __json[:charIndex]
            elif __json[charIndex] == " ":
                return __json[:charIndex]
        except IndexError:
            return __json

    def conn(this):
        try:
            this.connToWsLink.connect(this.addr)
            try:
                _recv = this.multiJSONHandle(this.connToWsLink.recv(1024).decode("utf-8"))
                loginData = json.loads(_recv)
            except json.JSONDecodeError:
                this.color(_recv)
                # raise Exception()
            getToken = None
            if loginData["needToken"]:
                
                if not os.path.isdir(os.path.join("配置文件","服服互通",f"server {this.addr[0]}")):
                    os.mkdir(os.path.join("配置文件","服服互通",f"server {this.addr[0]}"))
                _tokenPath = os.path.join("配置文件","服服互通",f"server {this.addr[0]}","token.txt")
                if not os.path.isfile(_tokenPath):
                    open(_tokenPath, "w").close()
                    this.color("§6您连接上了一个需要Token登录的互通服务端, 您还没有设置Token")
                    this.color(f"§6请在{_tokenPath}内输入您的Token并保存, 然后重新启动")
                    time.sleep(3)
                    # raise Exception()
                else:
                    try:
                        with open(_tokenPath, "r", encoding='utf-8') as _tokenFile:
                            getToken = _tokenFile.read()
                    except UnicodeDecodeError:
                        this.color("§c哎呀! Token保存的时候编码一定没选utf-8吧？请改正并重启")
                        time.sleep(2)
                        # raise Exception()
      
            this.connToWsLink.send(bytes(
                json.dumps(
                    {
                    "KeyCode": this.DESCRIPTION, 
                    "server": "41224221", 
                    "serverName": this.serverName, 
                    "token": getToken, 
                    "channel": this.channel,
                    "robotType": "DotCS"
                    }, 
                    ensure_ascii=False
                    ),
                'utf-8')
            )
        
            this.color("§a成功建立WS-Link连接")
            this.online = True
        except __main__.PluginSkip():
            pass
        except Exception as err:
            this.color("§c无法连接至服服互通, 将忽略")
            raise __main__.PluginSkip()
        
    def sendToWS(this, sendTo: bytes):
        this.connToWsLink.send(sendTo)

    def recvThread(this):
        import traceback
        try:
            this.color("§a已成功连接上服服互通")
            
            while 1:
                msgToGetLink = this.multiJSONHandle(this.connToWsLink.recv(2048).decode("utf-8"))
                if not len(msgToGetLink):
                    this.color("§c互通服务端关闭了与您的连接")
                    raise ConnectionResetError()
                try:
                    getJsonFrom = json.loads(msgToGetLink)
                except json.JSONDecodeError:
                    this.color(msgToGetLink)
                    raise __main__.PluginSkip()
                match getJsonFrom["data_type"]:
                    case"msg":
                        this.color(f"§7{getJsonFrom['serverName']} {getJsonFrom['data']}".replace('"', '’’').replace("'", '’'))
                        asyncio.run(function_cmd.sendcmd(r"""/tellraw %s {"rawtext":[{"text":"%s"}]}""" % ("@a", f"§7{getJsonFrom['serverName']} {getJsonFrom['data']}".replace('"', '’’').replace("'", '’'))))
                    case "connected":
                        this.color(f"{getJsonFrom['serverName']}服 加入了互通".replace('"', '’’').replace("'", '’'))
                        asyncio.run(function_cmd.sendcmd(r"""/tellraw %s {"rawtext":[{"text":"%s"}]}""" % ("@a", f"{getJsonFrom['serverName']}服 加入了互通".replace('"', '’’').replace("'", '’'))))
                    case "disconnected":
                        this.color(f"{getJsonFrom['serverName']}服 离开了互通".replace('"', '’’').replace("'", '’'))
                        asyncio.run(function_cmd.sendcmd(r"""/tellraw %s {"rawtext":[{"text":"%s"}]}""" % ("@a", f"{getJsonFrom['serverName']}服 离开了互通".replace('"', '’’').replace("'", '’'))))
                    case "consolemsg":
                        this.color(getJsonFrom['msgColor'])
                    case "player.join":
                        this.color(f"{getJsonFrom['serverName']} §g{getJsonFrom['data']} 加入了游戏".replace('"', '’’').replace("'", '’'))
                        asyncio.run(function_cmd.sendcmd(r"""/tellraw %s {"rawtext":[{"text":"%s"}]}""" % ("@a", f"{getJsonFrom['serverName']} §g{getJsonFrom['data']} 加入了游戏".replace('"', '’’').replace("'", '’'))))
                    case "player.left":
                        this.color(f"{getJsonFrom['serverName']} §g{getJsonFrom['data']} 退出了游戏".replace('"', '’’').replace("'", '’'))
                        asyncio.run(function_cmd.sendcmd(r"""/tellraw %s {"rawtext":[{"text":"%s"}]}""" % ("@a", f"{getJsonFrom['serverName']} §g{getJsonFrom['data']} 退出了游戏".replace('"', '’’').replace("'", '’'))))
                    case "get_data_serverlist":
                        
                        serverInList = getJsonFrom["data"]
                        this.color("§a目前与您互通的服务器:".replace('"', '’’').replace("'", '’'))
                        asyncio.run(function_cmd.sendcmd(r"""/tellraw %s {"rawtext":[{"text":"%s"}]}""" % ("@a", "§a目前与您互通的服务器:".replace('"', '’’').replace("'", '’'))))
                        for i in serverInList:
                            this.color(f"  {i} : {serverInList[i]}".replace('"', '’’').replace("'", '’'))
                            asyncio.run(function_cmd.sendcmd(r"""/tellraw %s {"rawtext":[{"text":"%s"}]}""" % ("@a", f"  {i} : {serverInList[i]}".replace('"', '’’').replace("'", '’'))))

        except ConnectionResetError:
            this.color("§c互通服务端连接中止")
            # rawText("@a", f"§c与互通服务端断开连接")
            this.online = False
            
        except Exception as err:
            this.color("§c互通服务端连接出错")
            print(err)
            this.color("§c" + traceback.format_exc())
            # rawText("@a", f"§c与互通服断开连接 3分钟后尝试重连")
            this.online = False
            this.connToWsLink.close()
            time.sleep(180)
            this.connToWsLink = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            this.conn()
            # threading.Thread(target = .recvThread).start()

    def sendmsg(this, msg):
        msgJsonToSend = json.dumps({"data_type": "msg", "data": msg, "server": this.serverName}, ensure_ascii=False)
        this.sendToWS(bytes(msgJsonToSend, "utf-8"))
        
    def sendJSON(this, __dict: dict):
        this.sendToWS(bytes(json.dumps(__dict, ensure_ascii=False), 'utf-8'))
        
    def disconnect(this):
        this.stop_mode = 1




    def colorf(self,text):
        "MC规则 彩色字"
        __main__.color(text)

    def color(self,text):
        self.colorf("§e组件§7-§b服服互通 §6> "+text)

    def load_json(self,path):
        import json
        import os
        with open(path,"r",encoding="utf-8") as f:
            return json.load(f)