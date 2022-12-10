import __main__ # 这个是必须要在开头导入的,要不然导入会失效
import json
import os
try:
    import numpy
except:
    import pip
    pip.main(["install","numpy","-i","https://pypi.tuna.tsinghua.edu.cn/simple/","--target={}".format(os.path.join(os.getcwd(),"Lib","site-packages"))])
    import numpy
function_cmd = __main__.function_cmd
@__main__.plugin_load # 必写,作用是导入插件
class __init__(__main__.plugin):
    __version__             = "1.0" # 版本号,默认值是 1.0
    __doc__                 = "检测到 .help 就返回信息" # 帮助文档,默认值 :""
    __author__              = "我不是Art" # 作者名,默认值: "未知的作者"
    __update_url__          = None # 更新链接,默认值是 None
    __license_agreement__   = "见帮助文档" # 许可协议,默认值: "见帮助文档" 

    __doc__date__           = [
        [
            "readme.txt",
            f"""主菜单 
本插件是 DotCS Go 的示范插件以及核心依赖插件,大部分涉及到菜单的均要安装此插件并统一管理
本插件的文档分为 用户文档.txt 以及 开发者api文档.txt
普通用户请阅读 用户文档.txt
对于插件开发者来说，请阅读 开发者api文档.txt
"""
        ],
        [
            "用户文档.txt",
            r"""主菜单 - 用户文档 
本插件是 DotCS Go 的示范插件以及核心依赖插件,大部分涉及到菜单的均要安装此插件并统一管理

# 如何编辑插件
您可以直接使用记事本打开并编辑插件配置文件,
这里推荐使用 Visual Studio Code(简称 vscode)
如果您是 Linux 用户(没有桌面),请使用 vim 编辑文件(我估计这句话我都不用说,因为你都打开这个文件了)

# 这个插件难搞吗
不难搞,如果只是改主菜单,那对于用户来说还是人类可搞的

# 此插件配置文件的位置在哪里?
配置文件/主菜单 文件夹里

# 我不懂 json,我应该怎么编辑
请前往 https://www.runoob.com/json/json-tutorial.html 网站自学,这里不再详细介绍 json 语法


# 插件的命令冲突
例如:
A插件: .ban 杀人
B插件: .ban 清除命令方块

一般会根据加载顺序,后加载的覆盖掉前一个.
如果是下面的这种情况:
.ban 杀人
.ban 清除命令方块

出现了多条 .ban,这种情况是配置文件不同名,但是效果是一样的。
请检查您的配置文件或者插件是否有冲突

# 纯数字用户无法使用菜单
这种情况就是配置文件的问题了,请使用 \"{{player}}\" 代替 {{player}}

# 配置规则
配置文件中的 命令,不支持高级函数!!!
例如:
.help
如需执行python函数的功能,请在 主菜单.py 的 __init__ 类里面的 __menu__ 中注册

# 主文件配置规则
以下述文件为例:

{
 "server": "§a服务器",// 服务器名
 "every_paper_cmd": 10,// 每一页显示的命令数
 "template": "默认模板.json",// 使用的模板名,对应 配置文件/主菜单/模板 路径
 "date": { // 自定义指令，"date"是可进行扩展的
  "kill": { // "kill" 这只是这个命令的id
   "cmd": ".kill", // "cmd" 是菜单以及实际检测中的命令
   "sendcmd": "/kill \"{{player}}\"", // 如果玩家执行了 "cmd"所指定的命令(此处为.kill) ,则运行 sendcmd 所指定的指令
   "top": "重生" // 命令的短说明
  },
  "hub": {// 自定义指令
   "cmd": ".hub",// "kill" 这只是这个命令的id
   "sendcmd": "/tp \"{{player}}\" 0 0 0", // 如果玩家执行了 "cmd"所指定的命令(此处为.hub) ,则运行 sendcmd 所指定的指令
   "top": "回到主城" //命令的短说明
  },

 }
}

"""
        ]
    ]
    

     # 主菜单初始
    def __init__(self,Name:str,Version:str,Mode:int):# 初始化操作函数!!!
        if self.isdir(os.path.join("配置文件","主菜单"))==False:
            self.mkdir(os.path.join("配置文件","主菜单"))
        
        if self.is_json(os.path.join("配置文件","主菜单","主文件.json"))[0]==False:
            self.color("§4组件配置文件丢失")
            self.color("§e正在重新创建")
            self.color("§a配置文件已创建至 §d{}".format(os.path.join(os.getcwd(),"配置文件","主菜单","主文件.json")))
            self.write_json(os.path.join("配置文件","主菜单","主文件.json"),{
    "server":"§a服务器",
    "every_paper_cmd":10,
    "template":"默认模板.json",
    "date":
        {
            "kill":
                {
                    "cmd":".kill",
                    "sendcmd":"/kill \"{{player}}\"",
                    "top":"重生"
                },
            "hub":
                {
                    "cmd":".hub",
                    "sendcmd":"/tp \"{{player}}\" 0 0 0",
                    "top":"回到主城"
                },
            "sc":
                {
                    "cmd":".生存",
                    "sendcmd":"/gamemode 0 \"{{player}}\"",
                    "top":"切换到生存模式"
                }
        }
})

        if self.isdir(os.path.join("文档","主菜单"))==False:
            self.mkdir(os.path.join("文档","主菜单"))

        if self.isdir(os.path.join("配置文件","主菜单","模板"))==False:
            self.mkdir(os.path.join("配置文件","主菜单","模板"))
            self.color("§4组件模板配置文件丢失,已重新创建文件夹")
            
        termux = [
            ["默认模板.json","""{"header":"§a{{服务器名}} 帮助菜单","cmd":"§b{{命令}} §e{{说明}}","end":"§b第{{当前页}}页-§b第{{最大页}}页","error":{"cmd_is_not_find":"未找到对应的命令!","cmd_help_is_not_find":"§4指令帮助缺失","page_is_not_find":"该页码不存在! ({{当前页}})","help_error_not_cmd_and_page":"帮助命令错误！{{命令}} 参数非指令或页码","help_not_Detailed_cmd_help":"该命令详细的帮助信息,原始命令说明:{{说明}}","help_is_zero":"§e暂无命令"}}"""],
            ["仿help命令.json","""{"header":"§2--- 显示帮助手册总 {{最大页}} 页中的第 {{当前页}} 页 (.help <页码>) ---","cmd":"{{命令}} {{说明}}","end":"§2小提示: 在输入.命令时不可以使用  <tab>  键来自动补全命令或参数","error":{"cmd_is_not_find":"§c未知的命令:{{命令}}。请检查命令是否存在,以及您对它是否拥有使用权限","cmd_help_is_not_find":"§4指令帮助缺失","help_error_not_cmd_and_page":"帮助命令错误！{{命令}} 参数非指令或页码","help_is_zero":"§c未知的命令:{{命令}}。请检查命令是否存在,以及您对它是否拥有使用权限","help_not_Detailed_cmd_help":"语法错误:意外的“{{命令}}”:出现在“.help >>{{命令}}<<”"}}"""]
            ]
        for i in termux:
            if os.path.isfile(os.path.join("配置文件","主菜单","模板",i[0]))==False:
                self.color("§4组件模板配置文件 §a{} §4丢失,已重新创建".format(i[0]))
                self.write_json(os.path.join("配置文件","主菜单","模板",i[0]),json.loads(i[1]))
                

        # 初始化文档检测
        for i in self.__doc__date__:
            if os.path.isfile(os.path.join("文档","主菜单",i[0]))==False:
                
                try:
                    with open(os.path.join(os.getcwd(),"文档","主菜单",i[0]),"w",encoding="utf-8") as f:
                        f.write(i[1])
                        self.color("§4帮助文档文件 §e{}§4 已丢失,现已重新创建至 §a{}".format(i[0],os.path.join(os.getcwd(),"文档","主菜单",i[0])))
                except:
                    self.color("§4帮助文档文件 §e{}§4 已丢失,我们已经对指定目录进行了重建文件尝试,但是失败了,请检查目标路径 §a{} §4是否有对应的读写权限".format(i[0],os.path.join(os.getcwd(),"文档","主菜单",i[0])))
        self.__menu__ = {
            "help":{
                "cmd":".help",
                "top":"获取帮助",
                "function":self.get_help
                }
            }
        # 读取配置文件,将 配置文件转换为 api 模式
        self.__主菜单__ = self.load_json(os.path.join("配置文件","主菜单","主文件.json"))

        for i in self.__主菜单__["date"]:
            self.__menu__[i]={
                "cmd":self.__主菜单__["date"][i]["cmd"],
                "top":self.__主菜单__["date"][i]["top"],
                "sendcmd":self.__主菜单__["date"][i]["sendcmd"],
            }

        # 根据配置文件读取模板
        if self.is_json(os.path.join("配置文件","主菜单","模板",self.__主菜单__["template"])):
            self.__模板__  = self.load_json(os.path.join("配置文件","主菜单","模板",self.__主菜单__["template"]))
            self.color("§a已读取模板配置文件 §b{}".format(self.__主菜单__["template"]))
        else:
            self.__模板__  = self.load_json(os.path.join("配置文件","主菜单","模板","默认模板.json"))
            self.color("§4配置文件 §b{} §4丢失,已读取 §b默认模板.json".format(self.__主菜单__["template"]))

        
    async def get_help(self,player,*args):
        if player.isdigit():
            player = f"{player}"
        cmd_len = len(self.__menu__)
        every_papaer_cmd = self.__主菜单__["every_paper_cmd"]
        
        paper_max = cmd_len // self.__主菜单__["every_paper_cmd"]
        if cmd_len % self.__主菜单__["every_paper_cmd"] !=0:
            paper_max +=1
        if cmd_len !=0:
            # 输出帮助页码
            if len(args[0]) == 0:
                now_page = 1
            elif args[0][0].isdigit():
                if int(args[0][0]) <=1:
                    now_page=1
                elif int(args[0][0]) >= paper_max:
                    now_page = paper_max
                else:
                    now_page = int(args[0])

            # 输出模板: 文件头
            await function_cmd.sendcmd(r"""/tellraw %s {"rawtext":[{"text":"%s"}]}""" % (player,self.__模板__["header"]\
            .replace("{{最大页}}",str(paper_max)).replace("{{当前页}}",str(now_page)).replace("{{服务器名}}",self.__主菜单__["server"])))
            now_cmd =1
            for it in self.__menu__:
                # 判断页码机制:(单位4)
                # 12
                # 34
                if now_cmd <= self.__主菜单__["every_paper_cmd"]*(now_page-1):
                    now_cmd +=1
                elif now_cmd <= self.__主菜单__["every_paper_cmd"]*(now_page):
                    await function_cmd.sendcmd(r"""/tellraw %s {"rawtext":[{"text":"%s"}]}""" % (player,self.__模板__["cmd"].replace("{{命令}}" ,self.__menu__[it]["cmd"]).replace("{{说明}}",self.__menu__[it]["top"])))
                        # await function_cmd.sendcmd(r"""/tellraw %s {"rawtext":[{"text":"%s"}]}""" % (player,i))
                    now_cmd +=1
                else:
                    break
            await function_cmd.sendcmd(r"""/tellraw %s {"rawtext":[{"text":"%s"}]}""" % (player,self.__模板__["end"]\
            .replace("{{最大页}}",str(paper_max)).replace("{{当前页}}",str(now_page)).replace("{{服务器名}}",self.__主菜单__["server"])))
        else:
            await function_cmd.sendcmd(r"""/tellraw %s {"rawtext":[{"text":"%s"}]}""" % (player,self.__模板__["header"]\
            .replace("{{最大页}}",str(1)).replace("{{当前页}}",str(1)).replace("{{服务器名}}",self.__主菜单__["server"])))
            await function_cmd.sendcmd(r"""/tellraw %s {"rawtext":[{"text":"%s"}]}""" % (player,self.__模板__["error"]["help_is_zero"]\
            .replace("{{最大页}}",str(1)).replace("{{当前页}}",str(1)).replace("{{服务器名}}",self.__主菜单__["server"])))
            await function_cmd.sendcmd(r"""/tellraw %s {"rawtext":[{"text":"%s"}]}""" % (player,self.__模板__["end"]\
            .replace("{{最大页}}",str(1)).replace("{{当前页}}",str(1)).replace("{{服务器名}}",self.__主菜单__["server"])))



        

        
    
    async def player_say(self,player,msg:str,title):
        msg = msg.split(" ")
        # 针对插件api的
        for i in self.__menu__:
            if msg[0] == self.__menu__[i]["cmd"]:
                if "sendcmd" in self.__menu__[i]:
                    await function_cmd.sendcmd(self.__menu__[i]["sendcmd"].replace("{{player}}",player))
                elif "function" in self.__menu__[i]:
                    await self.__menu__[i]["function"](player,msg[1:])
                break
                    

    # 初始化以及日常操作所用库
    def isdir(self,path):
        import os
        return os.path.isdir(path)
    def mkdir(self,path):
        "创建目录"
        import os
        os.makedirs(path)

    def is_json(self,path):
        import os
        if os.path.isfile(path)==False:
            return False,"文件未找到"
        else:
            try:
                with open(path,"r",encoding="utf-8") as f:
                    json.load(f)
                    return True,""
            except:
                return False,"文件已损坏"

    def load_json(self,path):
        import json
        import os
        with open(path,"r",encoding="utf-8") as f:
            return json.load(f)

    def write_json(self,path,dict):
        try:
            with open(path,"w",encoding="utf-8") as f:
                json.dump(dict,f,ensure_ascii=False,indent=True)
                return True
        except:
            return False

    def colorf(self,text):
        "MC规则 彩色字"
        __main__.color(text)

    def color(self,text):
        self.colorf("§e组件§7-§b主菜单 §6> "+text)
    
    def doc(self):
        "有关文档的自动创建以及管理"

    def mk_cmd(self,name):
        "注册主菜单"
