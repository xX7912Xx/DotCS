from . import color
import time
import sys
import psutil
from typing import IO, Any
import os
import json
import rich
import qrcode
import re
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
def is_port_used(port: int) -> bool:
    """
    检测端口是否被占用的函数
    参数:
        port: int -> 要检测的端口
    返回:
        端口未占用: bool -> False
        端口被占用: bool -> True
    """
    portUsed = False
    for proc in psutil.process_iter():
        try:
            if "phoenixbuilder" in proc.name():
                if strInList(str(port), proc.cmdline()):
                    portUsed = True
        except:
            pass
    return portUsed
def strInList(string: str, list: list) -> bool:
    """
    检测字符串是否在列表里的函数
    参数:
        str: str -> 要检测的字符串
        list: list -> 要检测的列表
    返回:
        若str在list里: bool -> True
        若str不在list里: bool -> False
    """
    string = str(string)
    for i in list:
        if string in i:
            return True
    return False

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

    @classmethod
    def getStatus(self,statusName: str) -> str:
        """
        获取状态数据的函数
        读取文件: status\statusName.txt

        参数:
            statusName: str -> 数据名称
        返回: str -> 文件读取结果
        """
        if not os.path.isfile("status/%s.txt" % statusName):
            return None
        with open("status/%s.txt" % statusName, "r", encoding = "utf-8") as file:
            status = file.read()
        return status

    @classmethod
    def setStatus(self,statusName: str, status):
        """
        设置状态数据的函数
        设置文件: status\statusName.txt

        参数:
            statusName: str -> 数据名称
            status: Any -> 要写入的信息, 写入前会转化为str
        返回: Any -> 设置结果
        """
        with open("status/%s.txt" % statusName, "w", encoding = "utf-8") as file:
            file.write(str(status))
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
    def input_re(self,*objects: Any, sep: str = " ", end: str = "\n", file: IO[str] | None = None, flush: bool = False,pattern="", flags=0) -> tuple[bool,str]:
        self.print(*objects,sep=sep,end="",file=file,flush=flush)
        float_input_mybe = input()
        
        return re.match(pattern,float_input_mybe,flags),float_input_mybe

    @classmethod
    def input_int(self,*objects: Any, sep: str = " ", end: str = "\n", file: IO[str] | None = None, flush: bool = False) -> tuple[bool,str]:
        self.print(*objects,sep=sep,end="",file=file,flush=flush)
        int_input_mybe = input()
        
        return int_input_mybe.isdigit(),int_input_mybe




def isfloat(str:str)->bool:
    """
    判定 str 是否是 float 类型数值
    ---
    参数:
        str:str -> 变量
    返回:
        bool -> 判定结果
    """
    try:
        float(str)
        return True
    except ValueError:
        return False

def getType(sth:Any)->str:
    """
    获取变量类型,是基础类型的 objects.__class__.__name__ 的封装
    ---
    参数:
        sth : Any -> 任意类型
    返回:
        str -> 类的名字"""
    return sth.__class__.__name__
    
def float2int(number: float, way: int = 1) -> int:
    """
    小数转整数的函数
    参数:
        number: float -> 要转换的小数
        way: 1 | 2 | 3 -> 转换方式
            1: 四舍五入
            2: 舍去小数部分
            3: 若有小数部分, 则入
    返回: int -> 转换结果
    """
    if way == 1:
        return round(number)
    elif way == 2:
        return int(number)
    elif way == 3:
        if int(number) == number:
            return int(number)
        else:
            return int(number)+1
def floatPos2intPos(number: float | str) -> int | float:
    """
    将 float / str 转换成 int / float 类型
    ---
    参数:
        number: float | str 
    返回:
        int | float
        (
            当 number 是 float类型时,返回 int 类型变量
            当 number 是 str 类型是,返回 float 类型变量
        )"""
    if type(number) == str:
        number = float(number)
        return number
    if type(number) == int:
        return number
    if int(number) == number:
        return int(number)
    if number > 0:
        return int(number)
    if number < 0:
        return int(number)-1
    raise ValueError("居然能运行到这里, 我也不知道出什么bug了...")
def second2minsec(sec: int) -> str:
    """
    秒数转正常时间显示的函数
    比如将 79 转换为 00:01:19
    参数:
        sec: int -> 要转换的秒数
    返回: str -> 转换结果
    """
    min, sec = divmod(sec, 60)
    hour, min = divmod(min, 60)
    hour, min, sec = str(int(hour)), str(int(min)), str(int(sec))
    if len(hour) == 1:
        hour = "0" + hour
    if len(min) == 1:
        min = "0" + min
    if len(sec) == 1:
        sec = "0" + sec
    return "%s:%s:%s" % (hour, min, sec)
        

def QRcode(text: str, where: str = "return", who: str | None = None) -> None:
    """
    在控制台输出二维码的函数
    参数:
        text: str -> 要转换的信息
        where: "console" | "server" -> 输出地点
            return: 返回结果
            console: 控制台
            server: 租赁服
        who: str.MinecraftTargetSelector -> 如果发到租赁服, 发送的对象
    返回: None
    """
    if where != "return" and where != "console" and where != "chatbar" and where != "actionbar":
        raise Exception("invalid argument")
    if (where != "return" and where != "console") and (who is None):
        raise Exception("invalid argument")
    qr = qrcode.QRCode()
    qr.add_data(text)
    QRstring = ""
    for line in qr.get_matrix():
        [(QRstring := (QRstring + "1") if pixel else (QRstring + "0")) for pixel in line]
        QRstring += "\n"
    QRstring = QRstring[:-1]
    if where == "return":
        return QRstring
    if where == "console":
        color(QRstring.replace("0", "\033[0;37;7m  ").replace("1", "\033[0m  ")+"§r")
    # if where == "chatbar":
    #     for line in QRstring.split("\n"):
    #         tellrawText(who, text = "§l"+line.replace("0", "§f▓").replace("1", "§0▓"))
    # if where == "actionbar":
    #     sendwocmd("/title %s actionbar §l" % who + QRstring.replace("0", "§f█").replace("1", "§0█") + "\n" * 15)
    #"\033[0m  " "\033[0;37;7m  "
    #"§0█" "§f█"
    #"▓"