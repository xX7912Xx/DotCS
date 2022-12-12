import __main__ # 这个是必须要在开头导入的,要不然导入会失效
function_cmd = __main__.function_cmd
@__main__.plugin_load # 必写,作用是导入插件
class __init__(__main__.plugin):
    __version__             = "1.0" # 版本号,默认值是 1.0
    __doc__                 = "检测到 .help 就返回信息" # 帮助文档,默认值 :""
    __author__              = "我不是Art" # 作者名,默认值: "未知的作者"
    __update_url__          = None # 更新链接,默认值是 None
    __license_agreement__   = "见帮助文档" # 许可协议,默认值: "见帮助文档" 
    
    def __init__(self,Name:str,Version:str,Mode:int):# 初始化操作函数!!!
        # 上述参数均是写死的模板!!!
        # Name:用户名
        # Version: DotCS 版本
        # Mode:启动模式(见文档)
        
        "初始化操作" # 这个文档帮助定义可以不写
        pass
    
    # 下面是监听 IDText 数据包的示范
    #async def IDText(self,packets:dict):#传递的是解析后的dump对象
    #    # 参数格式是固定的.
    #    # print("数据包:",packets)
    #    if packets['TextType'] !=8:
    #    await function_cmd.sendcmd("""tellraw %s {"rawtext":[{"text":"%s"}]}""" % ("@a",f"""§l§7[§b{packets['TextType']}§7] §7[§d{packets['SourceName']}§7]§r {packets["Message"]}"""))

    # async def player_say(self,player,msg,title):
    #     await function_cmd.sendcmd("""tellraw %s {"rawtext":[{"text":"%s"}]}""" % ("@a",f"""§l§7[§b{title.replace('"', '’’').replace("'", '’').replace('"', '’’').replace("'", '’')}§7] §7[§d{player}§7]§r {msg}"""))