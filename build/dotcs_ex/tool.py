from . import color
import time
import sys
def countdown(delay: int | float, msg: str = None,delay_color="§e") -> None:
    """
    控制台显示倒计时的函数
    参数:
        delay: int | float -> 倒计时时间(秒)
        msg: str -> 倒计时运行时显示的说明
        delay_color : str -> 倒计时的时间的颜色
    返回: 无返回值
    """
    if msg is None:
        msg = "Countdown"
    delayStart = time.time()
    delayStop = delayStart+delay
    # 这里需要考虑 初始值的长度,避免 print 时的错误
    while delay >= 0.01:
        delay = delayStop-time.time()
        color.color("%s§7:%s§r %.2fs          " % (msg,delay_color, delay), end="\r", info = "§e 等待 ")
        time.sleep(0.01)
    color.color("%s§7:§r %s          " % (msg, "§a0.00s"), info = "§e 等待 ")
def exitChatbarMenu(killFB: bool = True, delay: int | float = 3, reason: str = None, force = False,delay_color="§e") -> None:
    """
    退出命令系统的函数
    参数:
        delay: int | float -> 倒计时时间(秒)
        reason: str -> 退出时显示的说明
        delay_color : str -> 倒计时的时间的颜色
    返回: 无返回值
    """
    if force:
        try:
            pass
        except:
            pass
        finally:
            color("§e正在清空globals变量.", info = "§e 加载 ")
            globals().clear()
    countdown(delay=delay,msg="正在退出",delay_color=delay_color)
    sys.exit()

from typing import IO, Any
import os
import json
import rich
class path:
    
    @classmethod
    def isfile(self,path):
        "返回是否是文件"
        return os.path.isfile(path)
    
    @classmethod
    def isdir(self,path):
        return os.path.isdir(path)

    @classmethod
    def mkdir(self,path, mode=0o777,dir_fd: int | None =None):
        return os.mkdir(path,mode=mode,dir_fd=dir_fd)
    @classmethod
    def makedirs(self,name,mode=0o777, exist_ok=False):
        return os.makedirs(name,mode,exist_ok)
    

    class json:
        @classmethod
        def isjson(self,path):
            return json.path.is_json(path)
        @classmethod
        def load(self,path):
            return json.path.load(path)
class input_output:
    @classmethod
    def print(self,*objects: Any, sep: str = " ", end: str = "\n", file: IO[str] | None = None, flush: bool = False) -> None:
        rich.print(*objects,sep=sep,end=end,file=file,flush=flush)
    @classmethod
    def input(self,*objects: Any, sep: str = " ", end: str = "\n", file: IO[str] | None = None, flush: bool = False) -> None:
        self.print(*objects,sep=sep,end="",file=file,flush=flush)
        return input()

    @classmethod
    def is_bool(self,*objects: Any, sep: str = " ", end: str = "\n", file: IO[str] | None = None, flush: bool = False) -> None:
        self.print(*objects,sep=sep,end="",file=file,flush=flush)
        if input() in ["y","Y"]:
            return True
        else:
            return False

    @classmethod
    def input_float(self,*objects: Any, sep: str = " ", end: str = "\n", file: IO[str] | None = None, flush: bool = False) -> tuple[bool,str]:
        self.print(*objects,sep=sep,end="",file=file,flush=flush)
        float_input_mybe = input()
        
        return isfloat(float_input_mybe),float_input_mybe

    @classmethod
    def input_int(self,*objects: Any, sep: str = " ", end: str = "\n", file: IO[str] | None = None, flush: bool = False) -> tuple[bool,str]:
        self.print(*objects,sep=sep,end="",file=file,flush=flush)
        int_input_mybe = input()
        
        return int_input_mybe.isdigit(),int_input_mybe


def isfloat(str):
    try:
        float(str)
        return True
    except ValueError:
        return False
        
        