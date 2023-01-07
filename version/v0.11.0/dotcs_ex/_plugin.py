# DotCS 社区版 0.11.0 之前旧版本插件
# 隔离隔离,免得插件污染程序环境
import os
import inspect
import shutil
import pathlib
import copy
from . import color as _color
from . import tool
from . import _error

# 初始化巫妖王化环境
print_Py                    = print
print                       = _color.color
color                       = _color.color
removeColorInText           = _color.removeColorInText
getTextColorInTheEnd        = _color.getTextColorInTheEnd
countdown                   = tool.countdown
is_port_used                = tool.is_port_used
strInList                   = tool.strInList
isfloat                     = tool.isfloat
getType                     = tool.getType
float2int                   = tool.float2int
floatPos2intPos             = tool.floatPos2intPos
second2minsec               = tool.second2minsec
QRcode                      = tool.QRcode
PluginSkip                  = _error.PluginSkip
setStatus                   = tool.path.setStatus
getStatus                   = tool.path.getStatus
removeColorMC               = _color.removeColorMC

pluginList                  = []

class plugin:
    def __init__(self,path,connect,cmd,config):
        """
        旧版本 DotCS 插件类初始化
        ---
        参数:
            path:str -> 插件文件夹的的路径
            connect  -> 与fb的连接
            cmd      -> 终端菜单函数
            config   -> 配置文件
        """
        self.path = path
        self.connect = connect
        self.cmd = cmd
        self.config = config
        self._mkdir_path()
        self.plugin_list = self._load_file_list()
        self.plugin_dict = []
        self._load_plugin_config()
        if self.config["debug"]:
            for i in self.plugin_dict:
                color("§7-----------------",info="§4 测试 ")
                color("插件名:",i["name"],"\n插件内容:",info="§4 测试 ")
                if len(i["text"])!=0:
                    color(*i["text"],color_mode=2,info="§4 测试 ")
                else:
                    color("啥都没写",info="§4 测试 ")
                color("\n\n\n\n\n",info="§4 测试 ")
    def _mkdir_path(self):
        if os.path.isdir(self.path)==False:
            os.makedirs(self.path)
            _color.color("§a初始化生成旧版本插件文件夹成功",info="§b 提示 ")
 
    def _load_file_list(self)->list:
        p = pathlib.Path(self.path)
        return list(p.glob('**/*.py'))

    def _load_plugin_config(self):
        for i in self.plugin_list:
            _load = {"name":os.path.splitext(os.path.split(i)[1])[0],"text":[]}
            with open(i,"r",encoding="utf-8") as f:
                for ie in f.readlines():
                    _load["text"].append(ie)
                self.plugin_dict.append(copy.deepcopy(_load))