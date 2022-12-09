import __main__ # 这个是必须要在开头导入的,要不然导入会失效
import json
import os
function_cmd = __main__.function_cmd
@__main__.plugin_load # 必写,作用是导入插件
class __init__(__main__.plugin):
    __version__             = "1.0" # 版本号,默认值是 1.0
    __doc__                 = "检测到 .help 就返回信息" # 帮助文档,默认值 :""
    __author__              = "我不是Art" # 作者名,默认值: "未知的作者"
    __update_url__          = None # 更新链接,默认值是 None
    __license_agreement__   = "见帮助文档" # 许可协议,默认值: "见帮助文档" 

    __doc__date             = [
        [
            "readme.txt",
            f"""主菜单 {__version__}
作者:{__author__}
本插件是 DotCS Go 的示范插件以及核心依赖插件,大部分涉及到菜单的均要安装此插件并统一管理
本插件的文档分为 用户文档.txt 以及 开发者api文档.txt
普通用户请阅读 用户文档.txt
对于插件开发者来说，请阅读 开发者api文档.txt
"""
        ],
        [
            "用户文档.txt",
            f"""主菜单 - 用户文档 {__version__}
作者:{__author__}
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

# 配置规则
"""
        ]
    ]
    
    def __init__(self,Name:str,Version:str,Mode:int):# 初始化操作函数!!!
        if self.isdir(os.path.join("配置文件","主菜单"))==False:
            self.mkdir(os.path.join("配置文件","主菜单"))
        
        if self.is_json(os.path.join("配置文件","主菜单","主文件.json"))[0]==False:
            self.color("§4组件配置文件丢失")
            self.color("§e正在重新创建")
            self.color("§a配置文件已创建至 §d{}".format(os.path.join(os.getcwd(),"配置文件","主菜单","主文件.json")))

        if self.isdir(os.path.join("文档","主菜单"))==False:
            self.mkdir(os.path.join("文档","主菜单"))

        
    
    
    async def player_say(self,player,msg,title):
        if msg==".help":
            await function_cmd.sendcmd("""tellraw %s {"rawtext":[{"text":"%s"}]}""" % (player,"htp帮助菜单"))

    async def tellrawText(who: str, dispname: None | str = None, text: str = None, mode = function_cmd.sendcmd) -> None:
        """
        便捷执行tellraw的函数
        参数:
            who: str.MinecraftTargetSelector -> 给谁显示
            dispname: None | str -> 模拟玩家说话格式, 不传则直接tellraw
            text: str -> 要显示的信息
        返回: 无返回值
        """
        if dispname is None:
            mode(r"""/tellraw %s {"rawtext":[{"text":"%s"}]}""" % (who, text.replace('"', '’’').replace("'", '’')))
        else:
            mode(r"""/tellraw %s {"rawtext":[{"text":"<%s> %s"}]}""" % (who, dispname.replace('"', '’’').replace("'", '’'), text.replace('"', '’’').replace("'", '’')))
    
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

    def write_json(self,path):
        try:
            with open(path,"w",encoding="utf-8") as f:
                json.dump(f,ensure_ascii=False)
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
