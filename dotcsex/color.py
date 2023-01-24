from typing import Literal, TextIO
import datetime
import sys
import re
from re import escape,compile,findall
_color_rep = {
    "§1": "\033[0;37;34m",
    "§2": "\033[0;37;32m",
    "§3": "\033[0;37;36m",
    "§4": "\033[0;37;31m",
    "§5": "\033[0;37;35m",
    "§6": "\033[0;37;33m",
    "§7": "\033[0;37;90m",
    "§8": "\033[0;37;2m",
    "§9": "\033[0;37;94m",
    "§a": "\033[0;37;92m",
    "§b": "\033[0;37;96m",
    "§c": "\033[0;37;91m",
    "§d": "\033[0;37;95m",
    "§e": "\033[0;37;93m",
    "§f": "\033[0;37;1m",
    "§r": "\033[0m",
}
color_rep = dict((escape(k), v) for k, v in _color_rep.items())
del _color_rep
color_rep_str = "|".join(color_rep.keys())
color_rep_compile = compile(color_rep_str)
del color_rep_str
_info_rep = {
    "§1": "\033[7;37;34m",
    "§2": "\033[7;37;32m",
    "§3": "\033[7;37;36m",
    "§4": "\033[7;37;31m",
    "§5": "\033[7;37;35m",
    "§6": "\033[7;37;33m",
    "§7": "\033[7;37;90m",
    "§8": "\033[7;37;2m",
    "§9": "\033[7;37;94m",
    "§a": "\033[7;37;92m",
    "§b": "\033[7;37;96m",
    "§c": "\033[7;37;91m",
    "§d": "\033[7;37;95m",
    "§e": "\033[7;37;93m",
    "§f": "\033[7;37;1m",
    "§r": "\033[0m"
}
info_rep = dict((escape(k), v) for k, v in _info_rep.items())
del _info_rep
info_rep_str = "|".join(info_rep.keys())
info_rep_compile = compile(info_rep_str)
del info_rep_str
def info_repalce(text: str) -> str:
    if type(text)==str:
        return info_rep_compile.sub(lambda m: info_rep[escape(m.group(0))], text)
    else:
        raise TypeError(f"{text}并不是str类型")

def color_replace(text: str) -> str:
    if type(text)==str:
        return color_rep_compile.sub(lambda m: color_rep[escape(m.group(0))], text)
    else:
        raise TypeError(f"{text}并不是str类型")

def color(*values, output: bool = True, end: str = '\n', replace: bool = False, replaceByNext: bool = False, info: str | bool = " 信息 ", sep=' ', file: TextIO = sys.stdout, flush=False, word_wrapping: bool = True, text: str = None, is_time: bool = True, end_not_replace: bool = False, no_color: int = 0, title_time: str = "[%H:%M:%S] ", color_mode: int = 0, **date) -> None | str:
    """
    在命令系统控制台输出信息
    默认情况下，将值打印到流或 sys.stdout。
    ---

    参数:
        values : 要输出的内容.
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
        word_wrapping : bool -> 是否在折行时,自动在前面补充其文本内容
        is_time : 是否在终端显示时间(默认为 False)
        end_not_replace : 输出的内容结尾是否不添加彩色字的重置符(默认False)
        title_time: 格式化时间 ,默认值 "[%H:%M:%S] "
    返回: None | str
    """
    if text:
        return color(text, output=output, end=end, replace=replace, replaceByNext=replaceByNext, info=info, sep=sep, file=file, flush=flush, word_wrapping=word_wrapping, text=None, **date)
    if replaceByNext:
        replace = True
    _values = []
    if replace:
        _values.append("\n")
        end = ""
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
        info = "".join([_info, info_repalce(info), "\033[0m", " "])
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
                    all_1 = len(all)-1
                    f = str(f)
                    ret = findall('§[a-fr0-9]', f)
                    if len(ret) != 0:
                        next_print_first = ret[-1]
                    if v == 0:
                        __values.append("".join([color_replace(
                            next_print_first), color_replace(f), "\033[0m", "\n"]))
                        continue
                    if v == all_1:
                        __values.append("".join([datetime.datetime.now().strftime(
                            title_time) if is_time else "", info, color_replace(next_print_first), color_replace(f), "\033[0m"]))
                        continue
                    __values.append("".join([datetime.datetime.now().strftime(
                        title_time) if is_time else "", info, color_replace(next_print_first), color_replace(f), "\033[0m", "\n"]))

                _values.append("".join(__values))
            else:
                _values.append(color_replace(i)+"\033[0m")
        else:
            _values.append(color_replace(i)+"\033[0m")
    if end_not_replace:
        _values[-1] = _values[-1].rstrip("\033[0m")
    if output:
        _values[0] = "".join([datetime.datetime.now().strftime(
            title_time) if is_time else "", info if info else "", _values[0]])
        print(*_values, sep=sep, end=end, file=file, flush=flush)