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
        # 在加载阶段,您直接判定 库是不明智的,您应当在下面的 initialize 事件中进行管理
    async def initialize(self):
        # 检测是否篡改改名了
        if "plugin.DotCS_pip" not in __main__.PLUGIN_CLASS:
            # 检测是否有此插件
            self.color("§4Mysql_api插件依赖 §eDotCS_pip §4插件(如果您已经安装了,请勿改名)!请前往 §bhttps://github.com/xX7912Xx/DotCS/tree/main/plugin §4进行下载")
            del __main__.PLUGIN_CLASS["plugin.Mysql_api"]
        else:
            try:
                import pymysql
            except:
                self.color("§e正在安装依赖库§7:§b pymysql")
                __main__.PLUGIN_CLASS["plugin.DotCS_pip"].install("pymysql")
                self.color("§a安装依赖库完成§7:§b pymysql")
                import pymysql
        
    def colorf(self,text):
        "MC规则 彩色字"
        __main__.color(text)

    def color(self,text):
        self.colorf("§e组件§7-§bMysql_api §6> "+text)

