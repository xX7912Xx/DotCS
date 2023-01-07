from . import welcome
from . import color
from . import date
from . import tool
from . import color_input
from . import mc_color
from . import warning
from . import error
from . import config
from . import system
from . import _error
from . import game
from . import plugin
from . import _plugin
def input_bool(text:str)-> bool:
    "获取输入并自动判断,输入值为 Y 或 y 时 返回 True"
    return color_input(text) in ["Y","y"]

def input_parameter(text:str,selfs:list or None = None,error:str = "该数值不存在,请填写正确值!",help="")-> str:
    while(1):
        code = color_input(text)
        if selfs!=None:
            if code != "help":
                if code in selfs:
                    return code
                else:
                    color._color(error)
            else:
                color._color(help)
        else:
            return code