from typing import Literal, TextIO
import datetime
import sys
import re
from . import mc_color
from . import warning
from . import error
from . import color_input
import sys
def _color(text: str, output: bool = True, end: str = "\n", replace: bool = False, replaceByNext: bool = False, info = " 信息 "):
        """
    在控制台输出彩色文本的函数
    参数:
        text: str -> 要输出的信息
        end: str -> 结尾字符串,默认\\n
    返回: str -> 输出
    """
        try:
            mc_color.color(text=text, output=output, end=end, replace=replace, replaceByNext=replaceByNext, info=info)
        except Warning as err:
            warning(err)
        except Exception as err:
            error(err)

def removeColorInText(text):
    return text.replace("\033[0;37;34m", "").replace("\033[0;37;32m", "").replace("\033[0;37;36m", "").replace("\033[0;37;31m", "").replace("\033[0;37;35m", "").replace("\033[0;37;33m", "").replace("\033[0;37;90m", "").replace("\033[0;37;2m", "").replace("\033[0;37;94m", "").replace("\033[0;37;92m", "").replace("\033[0;37;96m", "").replace("\033[0;37;91m", "").replace("\033[0;37;95m", "").replace("\033[0;37;93m", "").replace("\033[0;37;1m", "").replace("\033[0m", "").replace("\033[7;37;34m", "").replace("\033[7;37;32m", "").replace("\033[7;37;36m", "").replace("\033[7;37;31m", "").replace("\033[7;37;35m", "").replace("\033[7;37;33m", "").replace("\033[7;37;90m", "").replace("\033[7;37;2m", "").replace("\033[7;37;94m", "").replace("\033[7;37;92m", "").replace("\033[7;37;96m", "").replace("\033[7;37;91m", "").replace("\033[7;37;95m", "").replace("\033[7;37;93m", "").replace("\033[7;37;1m", "")


def getTextColorInTheEnd(text):
    if "\033[" in text and "m" in text:
        return "\033[" + text.split("\033[")[-1].split("m")[0] + "m"
    else:
        return "\033[0m"


def color(*values, output: bool = True, end: str = '\n', replace: bool = False, replaceByNext: bool = False, info:str | bool=" 信息 ", sep=' ', file: TextIO = sys.stdout, flush=False,word_wrapping : bool = True,text=None, **date) -> None | str:
    """
    在命令系统控制台输出信息
    默认情况下，将值打印到流或 sys.stdout。可选关键字参数：
    ---

    参数:
        values: 要输出的内容.
        text: 要输出的内容(旧版),默认不使用,如果使用就当作 只有一个参数的 values 进行处理
        file: 类似文件的对象（流）;默认为 sys.stdout。
        sep: 在值之间插入字符串，默认为空格。
        end: 字符串追加在最后一个值之后，默认换行符。
        output: bool -> 是否输出.(返回的值是 values 拼接后的值)
        replace: bool -> 将 end 值修改为 "" 并返回行首(首个输出改成了 \\r )
            True: 若下次输出时 replace 还是为True, 则这次输出将被下次输出覆盖, 否则不会被覆盖.
            False: 普通的输出.
        replaceByNext: bool -> 是否一定被下次输出覆盖.(作用与 replace 相同,权限级别更高)
            True : 将 replace 的值改为 True
            False: 不做任何影响
        info: str -> 输出内容前的反色信息.(默认使用 文本的第一个彩色字符)
        flush: 是否强制冲刷流(如果output值为 True,则会在 end 输出后执行)
        word_wrapping : bool -> 是否自动换行输出(会将所有的\n进行处理)(默认为 True)
    返回: None | str
    """
    if text:
        return color(text,output=output,end=end,replace=replace,replaceByNext=replaceByNext,info=info,sep=sep,file=file,flush=flush,word_wrapping=word_wrapping,text=None,**date)
    if replaceByNext:
        replace = True
    _values = []
    if info:
        match str(values[0])[0:2]:
            case "§1":
                _info = "\033[7;37;34m"
            case "§2":
                _info = "\033[7;37;32m"
            case "§3":
                _info = "\033[7;37;36m"
            case "§4":
                _info = "\033[7;37;31m"
            case "§5":
                _info = "\033[7;37;35m"
            case "§6":
                _info = "\033[7;37;33m"
            case "§7":
                _info = "\033[7;37;90m"
            case "§8":
                _info = "\033[7;37;2m"
            case "§9":
                _info = "\033[7;37;94m"
            case "§a":
                _info = "\033[7;37;92m"
            case "§b":
                _info = "\033[7;37;96m"
            case "§c":
                _info = "\033[7;37;91m"
            case "§d":
                _info = "\033[7;37;95m"
            case "§e":
                _info = "\033[7;37;93m"
            case "§f":
                _info = "\033[7;37;1m"
            case "§r":
                _info = "\033[0m"
            case _:
                _info = "\033[7;37;1m"
        info = _info+info.replace("§1", "\033[7;37;34m").replace("§2", "\033[7;37;32m").replace("§3", "\033[7;37;36m").replace("§4", "\033[7;37;31m").replace("§5", "\033[7;37;35m").replace("§6", "\033[7;37;33m").replace("§7", "\033[7;37;90m").replace("§8", "\033[7;37;2m").replace(
            "§9", "\033[7;37;94m").replace("§a", "\033[7;37;92m").replace("§b", "\033[7;37;96m").replace("§c", "\033[7;37;91m").replace("§d", "\033[7;37;95m").replace("§e", "\033[7;37;93m").replace("§f", "\033[7;37;1m").replace("§r", "\033[0m")+"\033[0m "
        info +="\033[0m"
    else:
        info = ""
    next_print_first = ""
    for i in values:
        i = str(i)
        if word_wrapping:
            # 特殊处理
            if "\n" in i:
                all = i.split("\n")
                __values = []
                for v, f in enumerate(all):
                    f=str(f)
                    ret = re.findall('§[a-fr0-9]',f)
                    if len(ret)==0:
                        pass
                    else:
                        next_print_first = ret[-1]
                    if v==0:
                        __values.append((next_print_first+f+"\n").replace("§1", "\033[0;37;34m").replace("§2", "\033[0;37;32m").replace("§3", "\033[0;37;36m").replace("§4", "\033[0;37;31m").replace("§5", "\033[0;37;35m").replace("§6", "\033[0;37;33m").replace("§7", "\033[0;37;90m").replace("§8", "\033[0;37;2m").replace(
                        "§9", "\033[0;37;94m").replace("§a", "\033[0;37;92m").replace("§b", "\033[0;37;96m").replace("§c", "\033[0;37;91m").replace("§d", "\033[0;37;95m").replace("§e", "\033[0;37;93m").replace("§f", "\033[0;37;1m").replace("§r", "\033[0m")+"\033[0m")
                    elif v == len(all)-1:
                        __values.append((info+next_print_first+f).replace("§1", "\033[0;37;34m").replace("§2", "\033[0;37;32m").replace("§3", "\033[0;37;36m").replace("§4", "\033[0;37;31m").replace("§5", "\033[0;37;35m").replace("§6", "\033[0;37;33m").replace("§7", "\033[0;37;90m").replace("§8", "\033[0;37;2m").replace(
                        "§9", "\033[0;37;94m").replace("§a", "\033[0;37;92m").replace("§b", "\033[0;37;96m").replace("§c", "\033[0;37;91m").replace("§d", "\033[0;37;95m").replace("§e", "\033[0;37;93m").replace("§f", "\033[0;37;1m").replace("§r", "\033[0m")+"\033[0m")
                    else:
                        __values.append((info+next_print_first+f+"\n").replace("§1", "\033[0;37;34m").replace("§2", "\033[0;37;32m").replace("§3", "\033[0;37;36m").replace("§4", "\033[0;37;31m").replace("§5", "\033[0;37;35m").replace("§6", "\033[0;37;33m").replace("§7", "\033[0;37;90m").replace("§8", "\033[0;37;2m").replace(
                        "§9", "\033[0;37;94m").replace("§a", "\033[0;37;92m").replace("§b", "\033[0;37;96m").replace("§c", "\033[0;37;91m").replace("§d", "\033[0;37;95m").replace("§e", "\033[0;37;93m").replace("§f", "\033[0;37;1m").replace("§r", "\033[0m")+"\033[0m")

                _values.append("".join(__values))
            else:
                _values.append(i.replace("§1", "\033[0;37;34m").replace("§2", "\033[0;37;32m").replace("§3", "\033[0;37;36m").replace("§4", "\033[0;37;31m").replace("§5", "\033[0;37;35m").replace("§6", "\033[0;37;33m").replace("§7", "\033[0;37;90m").replace("§8", "\033[0;37;2m").replace(
                "§9", "\033[0;37;94m").replace("§a", "\033[0;37;92m").replace("§b", "\033[0;37;96m").replace("§c", "\033[0;37;91m").replace("§d", "\033[0;37;95m").replace("§e", "\033[0;37;93m").replace("§f", "\033[0;37;1m").replace("§r", "\033[0m")+"\033[0m")
        else:
            _values.append(i.replace("§1", "\033[0;37;34m").replace("§2", "\033[0;37;32m").replace("§3", "\033[0;37;36m").replace("§4", "\033[0;37;31m").replace("§5", "\033[0;37;35m").replace("§6", "\033[0;37;33m").replace("§7", "\033[0;37;90m").replace("§8", "\033[0;37;2m").replace(
            "§9", "\033[0;37;94m").replace("§a", "\033[0;37;92m").replace("§b", "\033[0;37;96m").replace("§c", "\033[0;37;91m").replace("§d", "\033[0;37;95m").replace("§e", "\033[0;37;93m").replace("§f", "\033[0;37;1m").replace("§r", "\033[0m")+"\033[0m")
    _values = tuple(_values)

    # 这里是 print 的实现
    if output:
        if replace:
            file.write("\r")
            end = ""
        file.write(info)
        for i, v in enumerate(_values):
            file.write(v)
            if i != len(_values)-1:
                file.write(sep)
            else:
                file.write("\033[0m")
                file.write(end)
        if flush:
            file.flush()
    else:
        return_text = []
        for i, v in enumerate(_values):
            return_text.append(v)
            if i != len(_values)-1:
                return_text.append(sep)
            else:
                return_text.append("\033[0m")
        return "".join(return_text)

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