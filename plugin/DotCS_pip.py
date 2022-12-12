import os
import subprocess
import platform
import __main__ # 这个是必须要在开头导入的,要不然导入会失效
function_cmd = __main__.function_cmd
@__main__.plugin_load # 必写,作用是导入插件
class __init__(__main__.plugin): 
    def __init__(self,Name:str,Version:str,Mode:int):# 初始化操作函数!!!
        # 上述参数均是写死的模板!!!
        # Name:用户名
        # Version: DotCS 版本
        # Mode:启动模式(见文档)
        "初始化操作" # 这个文档帮助定义可以不写
        pass

    # 旧版本 install 函数已发现明显bug!暂不可使用!2333
    def install(self,packets):
        "安装 python 库"
        if platform.system() =="Windows":
            subprocess.run(["pip.exe","install",packets,"-i","https://pypi.tuna.tsinghua.edu.cn/simple/","--target={}".format(os.path.join(os.getcwd(),"Lib","site-packages"))])
        else:
            subprocess.run(["pip","install",packets,"-i","https://pypi.tuna.tsinghua.edu.cn/simple/","--target={}".format(os.path.join(os.getcwd(),"Lib","site-packages"))])
    async def initialize(self):
        self.color("§e温馨提示§7: §2DotCS_pip 插件 并不是万能的!出现了vs依赖问题时,请下载 vs2022 解决此问题!!!")
    def colorf(self,text):
        "MC规则 彩色字"
        __main__.color(text)
    def color(self,text):
        self.colorf("§e组件§7-§bDotCS_pip §6> "+text)