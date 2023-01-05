
import os
import re
import sys
import datetime
from typing import Literal, TextIO
if __name__ =="__main__":
    print("\n"*30 + "http://www.mcppl.art/")
# 初始化启动变量


def _color(*values, output: bool = True, end: str = '\n', replace: bool = False, replaceByNext: bool = False, info: str | bool = " 信息 ", sep=' ', file: TextIO = sys.stdout, flush=False, word_wrapping: bool = True, text=None, **date) -> None | str:
    """
    在命令系统控制台输出信息
    默认情况下，将值打印到流或 sys.stdout。可选关键字参数：
    此函数临时调用!以防输出有问题
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
        return color(text, output=output, end=end, replace=replace, replaceByNext=replaceByNext, info=info, sep=sep, file=file, flush=flush, word_wrapping=word_wrapping, text=None, **date)
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
        info += "\033[0m"
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
                    f = str(f)
                    ret = re.findall('§[a-fr0-9]', f)
                    if len(ret) == 0:
                        pass
                    else:
                        next_print_first = ret[-1]
                    if v == 0:
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


try:# 初始化变量
    from . import dotcs_ex
    lastOutputLen = 0
    lastReplace = False
    lastReplaceByNext = False
    # 兼容 旧版本 DotCS,使得 print 函数保留
    print_Py = print

    # 兼容 旧版本 DotCS,使得 dotcs_ex 这个库的部分函数映射出来
    print = dotcs_ex.color.color
    # 兼容 旧版本 DotCS,使得 dotcs_ex 这个库的部分函数映射出来
    color = dotcs_ex.color.color
    # 兼容 旧版本 DotCS,使得 dotcs_ex 这个库的部分函数映射出来
    removeColorInText = dotcs_ex.color.removeColorInText
    # 兼容 旧版本 DotCS,使得 dotcs_ex 这个库的部分函数映射出来
    getTextColorInTheEnd = dotcs_ex.color.getTextColorInTheEnd

    countdown = dotcs_ex.tool.countdown

    # 兼容 旧版本 DotCS,使得 dotcs_ex 这个库的部分变量映射出来
    version = dotcs_ex.date.date.version
    pid = os.getpid()                                               # 兼容 旧版本 DotCS

    PyPIthird = dotcs_ex.date.date.PyPIthird # 兼容旧版本 DotCS,这个变量应该没人会调用
    if __name__ =="__main__":
        color("DotCS 正在运行, 其进程 pid 为 %d." % pid)

    def exitChatbarMenu(killFB: bool = True, delay: int | float = 3, reason: str = None, force=False) -> None:
        """
        退出命令系统的函数

        参数:
            killFB: bool -> 是否同时关闭FastBuilder
            delay: int | float -> 倒计时时间(秒)
            reason: str -> 退出时显示的说明
        返回: 无返回值
        """
        raise SystemExit(0)
    del _color
except Exception as err:
    _color("§4DotCS 初始化启动错误!本次启动缺少依赖库 dotcs_ex。如果您是编译安装,则需要前往 bbs.mcppl.art 下载依赖文件 dotcs_ex。", info="§4 错误 ")
    _color("§4按下回车退出程序", info="§4 输入 ", end="")
    input()
    sys.exit()
try:# 初始化导入内置库
    import traceback
    import socket
    import datetime
    import time
    import json
    import random
    import sys
    import urllib
    import urllib.parse
    import platform
    import sqlite3
    import threading
    import struct
    import hashlib
    import shutil
    import base64
    import ctypes
    import collections
    import types
    import itertools
    import inspect
    import _thread as thread
    from typing import Union, List, Dict, Tuple, Set
except Exception as err:
    color("§c导入Python标准库库失败, 信息:\n"+str(err), info="§c 错误 ")
    color("§c"+traceback.format_exc(), info="§c 错误 ")
    exitChatbarMenu(False, 5)
try:# 初始化导入第三方库
    # 可以通过pip安装的库
    import psutil
    import requests
    import pymysql
    import qrcode
    import websocket
    import brotli
    import PIL
    import rich.console
    import Crypto.Cipher.DES3
except Exception as err:
    color("§c导入Python 第三方库失败, 信息:\n"+str(err), info="§c 错误 ")
    color("§c"+traceback.format_exc(), info="§c 错误 ")
    exitChatbarMenu(False, 5)
try:# 初始化导入本地库
    if __name__ =="__main__":
        for i in dotcs_ex.date.date.PyPIthird:
            color("DotCS 使用了 §e%s§r 库, 其作者是 §e%s§r, 链接: %s" %
                  (i["name"], i["author"], i["link"]), info=" 信息 ")

        import bdx_work_shop.canvas
        import bdx_work_shop.artists.cmd_midi_music
        from proxy import conn
        from PyPI import TDES
        from PyPI.SpaceRectangularCoordinateSystem import Point, Line, Cube
    else:
        from bdx_work_shop import canvas
        pass
except Exception as err:
    color("§c导入Python 本地库失败, 信息:\n"+str(err), info="§c 错误 ")
    color("§c"+traceback.format_exc(), info="§c 错误 ")
    exitChatbarMenu(False, 5)
try:# 第2次的初始化变量 + 欢迎语句
    platformVer = str(platform.platform())
    if "Windows" in platformVer:
        platformVer = "Windows"
    else:
        platformVer = "Linux"
    console = rich.console.Console()
    if __name__ =="__main__":
        color("控制台窗口大小: %dx%d" % (console.height, console.width), info = " 信息 ")
        if console.width < 115:
            color("§e控制台窗口宽度应大于 115, 请调整.", info = "§e 警告 ")
        while console.width < 115:
            color("§e当前宽度: %d" % console.width, replace = True, info = "§e 警告 ")
            time.sleep(0.01)
    
    # 这里是写死的,版权说明这里是必须要读的!!!
    dotcs_ex.welcome.welcome()
    if os.path.isfile("config.json")!=True:
        if __name__ !="__main__":
            pass
            color("§4在使用本库进行开发时,请前往 https://mcppl.art 阅读 库模式开发帮助文档!",info="§e 提示 ")
            color("§4严禁屏蔽 版权信息提示 的部分,本库版权声明中已经写明,必须要告知用户所使用依赖库的版权信息!",info="§e 提示 ")
            color("§4本提示会在有config.json文件时不再提示.您可以通过使用 §adotcs_community§r.§adotcs_ex§r.§aconfig§r.§ainit§r.§aconfig§6(§e\"config.json\"§6)§r §4来配置文件",info="§e 提示 ")
    if __name__ =="__main__":
        _config = dotcs_ex.config.init.config("config.json")
        _config.append_function(dotcs_ex.config.update_server.update_server)
        _config.init()
        config = _config.get_return()

    # color(title4)
       
except Exception as err:
    color("§c导入Python 本地库失败, 信息:\n"+str(err), info="§c 错误 ")
    color("§c"+traceback.format_exc(), info="§c 错误 ")
    exitChatbarMenu(False, 5)