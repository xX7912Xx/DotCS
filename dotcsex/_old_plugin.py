# DotCS Pro 旧版本插件
# 作者:去幻想乡的老art
import multiprocessing
import threading
import time
from typing import Any, TextIO
from . import conn
from . import color
from . import date
import time
import json
import os
import sys

def plugin(server: str, ip: str, colors: str = "", PiPe: multiprocessing.Pipe = None):
    "DotCS 插件进程管理"

    # 检测 FB 是否启动完成
    servers = color.info_repalce(f"{colors} {server} §r")
    while (1):
        try:
            connect = conn.ConnectFB(f"{ip}")
            conn.ReleaseConnByID(connect)
            time.sleep(1)
            break
        except Exception as err:
            pass
    color.color("§aFB启动完成", info=f"§e plugin §r {servers}", word_wrapping=False)
    
    if os.path.isdir("plugin")==False:os.makedirs("plugin")
    if os.path.isdir(os.path.join("plugin",str(server)))==False:os.makedirs(os.path.join("plugin",str(server)))
    Plugin = _Plugin(ip, server, servers, PiPe)
    Plugin.run()
    
    # 读取插件
    while (1):
        # 获取通知,是否被堵塞
        # 如果被堵塞就结束进程
        date = Plugin.recv().recv()
        if date['type'] == "listen_error":
            Plugin.stop()
            color.color( "§e正在重启插件引擎中", info=f"§e plugin §r {servers}")
            Plugin.run()
        elif date['type'] =="exit":
            Plugin.stop()
            color.color( "§e旧版本插件引擎已退出,原因:",date["message"], info=f"§e plugin §r {servers}")
            break


class _Plugin:
    "DotCS 插件系统基础类"

    def __init__(self, ip: str, server: str = None, cserver: str = None, PiPe: multiprocessing.Pipe = None):
        "插件初始化"
        self.plugins = {}
        self.ip = ip
        self.server = server
        self.conn = None
        self.conn_in_Pipe, self.conn_out_Pipe = multiprocessing.Pipe(True)
        self.cserver = cserver
        self.fb_PiPe = PiPe

    def run(self):
        "启动 conn 监听进程"
        from . import conn
        while (1):
            try:
                connect = conn.ConnectFB(f"{self.ip}")
                conn.ReleaseConnByID(connect)
                time.sleep(1)
                break
            except Exception as err:
                pass
        self.conn = multiprocessing.Process(target=listen, args=(
            self.ip, (self.conn_in_Pipe, self.conn_out_Pipe), self.cserver, self.fb_PiPe))
        self.conn.start()

    def load(self):
        "读取插件"


    def stop(self):
        self.conn.terminate()
        self.conn.join()

    def recv(self):
        return self.conn_out_Pipe
class __color:
    def __init__(self,cserver):
        self.cserver = cserver
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        kwds["info"] = f"§e plugin §r {self.cserver}"
        return color.color(*tuple(args),**kwds)

def listen(ip: str, Pipe, cserver: str, fb_Pipe: multiprocessing.Pipe = None):
    "获取 conn 的监听结果,解析由 DotCS 完成(由线程来解析 FB 的数据包的话,会出现cpu没有完全利用的情况)"
    from . import color as _color
    import sys,os
    sys.stdin = os.fdopen(0, "r")  # 打开标准输入流
    packets_listen = [-100,9,10,63,79]
    # 远古插件兼容
    def removeColorInText(text):
        return text.replace("\033[0;37;34m", "").replace("\033[0;37;32m", "").replace("\033[0;37;36m", "").replace("\033[0;37;31m", "").replace("\033[0;37;35m", "").replace("\033[0;37;33m", "").replace("\033[0;37;90m", "").replace("\033[0;37;2m", "").replace("\033[0;37;94m", "").replace("\033[0;37;92m", "").replace("\033[0;37;96m", "").replace("\033[0;37;91m", "").replace("\033[0;37;95m", "").replace("\033[0;37;93m", "").replace("\033[0;37;1m", "").replace("\033[0m", "").replace("\033[7;37;34m", "").replace("\033[7;37;32m", "").replace("\033[7;37;36m", "").replace("\033[7;37;31m", "").replace("\033[7;37;35m", "").replace("\033[7;37;33m", "").replace("\033[7;37;90m", "").replace("\033[7;37;2m", "").replace("\033[7;37;94m", "").replace("\033[7;37;92m", "").replace("\033[7;37;96m", "").replace("\033[7;37;91m", "").replace("\033[7;37;95m", "").replace("\033[7;37;93m", "").replace("\033[7;37;1m", "")


    def getTextColorInTheEnd(text):
        if "\033[" in text and "m" in text:
            return "\033[" + text.split("\033[")[-1].split("m")[0] + "m"
        else:
            return "\033[0m"
    threadList = []
    lastOutputLen = 0
    lastReplace = False
    lastReplaceByNext = False
    print_Py = print
    color = __color(cserver=cserver)
    connect = ""
    def countdown(delay: int | float, msg: str = None) -> None:
        """
        控制台显示倒计时的函数

        参数:
            delay: int | float -> 倒计时时间(秒)
            msg: str -> 倒计时运行时显示的说明
        返回: 无返回值
        """
        if msg is None:
            msg = "Countdown"
        delayStart = time.time()
        delayStop = delayStart+delay
        while delay >= 0.01:
            delay = delayStop-time.time()
            color("%s: %.2fs" % (msg, delay), replace = True, replaceByNext = True, info = f"§e plugin §r {cserver}")
            time.sleep(0.1)
    def exitChatbarMenu(killFB: bool = True, delay: int | float = 3, reason: str = None, force = False,load_Error=False) -> None:
        _color.color("§4",reason, info=f"§e plugin §r {cserver}", word_wrapping=False)
        if load_Error:
            Pipe[0].send({"type":"exit","message":""})
        else:
            Pipe[0].send({"type":"listen_error","message":""})
        return 0
    import os,sys
    try:
        import traceback, socket, datetime, time, json, random, sys, urllib, urllib.parse, platform, sqlite3, threading, struct, hashlib, shutil, base64, ctypes, collections, types, itertools, inspect, _thread as thread
        from typing import Union, List, Dict, Tuple, Set
    except Exception as err:
        _color.color("DotCS 旧版本插件兼容模块启动失败,缺少库",str(err), info=f"§e plugin §r {cserver}", word_wrapping=False)
        Pipe[0].send({"type":"exit","message":""})
        time.sleep(1)
        return 0
    try:
        import psutil, requests, pymysql, qrcode, websocket, brotli, PIL, rich.console, Crypto.Cipher.DES3,rich
    except Exception as err:
        _color.color("§eDotCS 旧版本插件兼容模块启动失败,缺少库",str(err), info=f"§e plugin §r {cserver}", word_wrapping=False)
        Pipe[0].send({"type":"exit","message":""})
        time.sleep(1)
        return 0
    try:
        # 第三方本地库.
        PyPIthird = [
            {"name": "bdx_work_shop", "author": "2401PT, SuperScript", "link": "https://github.com/CMA2401PT/BDXWorkShop"},
            {"name": "FastBuilder connector", "author": "2401PT", "link": "https://github.com/CMA2401PT/FastBuilder"},
            {"name": "TDES encrypt", "author": "7912", "link": "None"},
            {"name": "Space Rectangular Coordinate System", "author": "7912", "link": "None"}
        ]
        for i in PyPIthird:
            _color.color("DotCS 使用了 §e%s§r 库, 其作者是 §e%s§r, 链接: %s" % (i["name"], i["author"], i["link"]), info = f"§e plugin §r {cserver}")
        import bdx_work_shop.canvas
        import bdx_work_shop.artists.cmd_midi_music
        from PyPI import TDES
        from PyPI.SpaceRectangularCoordinateSystem import Point, Line, Cube
    except Exception as err:
        _color.color("§eDotCS 旧版本插件兼容模块启动失败,缺少库",str(err), info=f"§e plugin §r {cserver}", word_wrapping=False)
        Pipe[0].send({"type":"exit","message":""})
        time.sleep(1)
        return 0

    platformVer = str(platform.platform())
    if "Windows" in platformVer:
        platformVer = "Windows"
    else:
        platformVer = "Linux"
    console = rich.console.Console()
    _color.color("控制台窗口大小: %dx%d" % (console.height, console.width), info=f"§e plugin §r {cserver}")
    if console.width < 115:
        _color.color("§e控制台窗口宽度应大于 115, 请调整.", info=f"§e plugin §r {cserver}")
    while console.width < 115:
        _color.color("§e当前宽度: %d" % console.width, replace = True, info=f"§e plugin §r {cserver}")
        time.sleep(0.01)
    

    def is_port_used(port: int) -> bool:return False
    def FBkill() -> None:pass
    def runFB(killFB: bool = True) -> None:pass
    def Byte2KB(byteSize: int) -> str:
        """
        将字节单位转换为最大能转换的单位的函数

        参数:
            byteSize: int -> 字节单位大小
        返回: str: -> 转换后的格式
        """
        for i in ["B", "KB", "MB", "GB", "TB", "PB", "EB"]:
            if byteSize > 1024:
                byteSize /= 1024
            else:
                return "%.2f%s" % (byteSize, i)
    def setglobalVar(key, value):
        if value is None:
            globals().__delitem__(value)
        else:
            globals().update({key: value})
    def fileDownload(url: str, path: str, timeout: float | int = 3, freshSize: int = 10240) -> dict:
        """
        下载文件并显示进度的函数

        参数:
            url: str -> 文件链接
            path: str -> 文件存储位置
            timeout: float | int -> 下载超时处理, 单位: 秒
            freshSize: int -> 每次下载的文件大小, 单位: 字节, 说明: 此数值越大, 对CPU的使用越低, 控制台更新下载进度状态的频率也越慢
        返回:
            dict: -> 下载是否成功
                成功: status -> success
                失败: status -> fail
                    无法找到目标服务器: reason -> file not found
                    目标服务器拒绝下载: reason -> server rejected
                    下载时连接中断或超时: reason -> timed out
        """
        try:
            response = requests.get(url, stream = True, timeout = timeout)
        except Exception as err:
            _color.color("§c下载失败, 原因: 文件未找到.", info=f"§e plugin §r {cserver}")
            return {"status": "fail", "reason": "file not found"}
        fileDownloadedSize = 0
        fileSize = int(response.headers['content-length'])
        if response.status_code == 200:
            _color.color("§e开始下载, 文件大小: %s" % Byte2KB(fileSize), info=f"§e plugin §r {cserver}")
            timeDownloadStart = time.time()
            fileDownloadedLastSize = 0
            speedDownloadCurrent = 0
            timeRem = "--:--:--"
            with open(path, 'wb') as file:
                try:
                    for data in response.iter_content(chunk_size = freshSize):
                        file.write(data)
                        fileDownloadedSize += len(data)
                        if time.time()-timeDownloadStart >= 0.5:
                            speedDownloadCurrent = (fileDownloadedSize-fileDownloadedLastSize)/(time.time()-timeDownloadStart)
                            timeDownloadStart = time.time()
                            fileDownloadedLastSize = fileDownloadedSize
                            if speedDownloadCurrent != 0:
                                timeRem = second2minsec((fileSize-fileDownloadedSize)/speedDownloadCurrent)
                        _color.color("§e正在下载: %.2f%%, %s / %s, %s/s, 预计还需 %s" % (fileDownloadedSize/fileSize*100, Byte2KB(fileDownloadedSize), Byte2KB(fileSize), Byte2KB(speedDownloadCurrent), timeRem), replace = True, info = f"§e plugin §r {cserver}")
                except Exception as err:
                    _color.color("§c下载失败, 原因: 连接超时", info=f"§e plugin §r {cserver}")
                    return {"status": "fail", "reason": "timed out"}
            _color.color("§a下载完成", info=f"§e plugin §r {cserver}")
            return {"status": "success"}
        else:
            _color.color("§c下载失败, 原因: 状态码 %s" % response.status_code, info=f"§e plugin §r {cserver}")
            return {"status": "fail", "reason": "server rejected", "status_code": response.status_code}
    def updateCheck() -> None:pass
    sendtogroup = ""
    QQgroup = ""
    def NekoMaidMsg(msg, msgIndex, connToSend, isLastFormat = False): pass
    if os.path.isdir("serverMsg")==False:os.makedirs("serverMsg")
    def log(text: str, filename: str = None, mode: str = "a", encoding: str = "utf-8", errors: str = "ignore", output: bool = True, sendtogamewithRitBlk: bool = False, sendtogamewithERROR: bool = False, sendtogrp: bool = False, info = f"§e plugin §r {cserver}") -> None:
        """
        记录日志的函数

        参数:
            text: str -> 要记录的信息
            filename: str -> 写入文件位置, 默认写入在 serverMsg\%Y-%m-%d.txt
            mode: str -> 记录方法, 同open()
            encoding: str -> 记录编码, 同open()
            errors: str -> 错误处理方式, 同open()
            output: bool -> 是否同时在控制台输出
        返回: 无返回值
        """
        if filename is None:
            filename = "serverMsg/"+datetime.datetime.now().strftime("%Y-%m-%d.txt")
        if text[-1:] == "\n":
            text = text[:-1]
        info = f"§e plugin §r {cserver}"
        if output:
            _color.color(text+"\033[0m", info = info)
        try:
            with open(filename, mode, encoding = encoding, errors = errors) as file:
                file.write("["+datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+"] "+text+"\n")
        except Exception as err:
           _color.color("写入日志错误, 信息:\n"+str(err), info=f"§e plugin §r {cserver}",word_wrapping=True)
        if sendtogamewithRitBlk:
            tellrawText("@a", "§l§6Ritle§aBlock§r", text = text)
        if sendtogamewithERROR:
            tellrawText("@a", "§l§4ERROR§r", text = "§c" + text)
        if sendtogrp:
            try:
                sendtogroup("group", QQgroup, text)
            except Exception as err:
                errmsg = "log()函数中sendtogroup()报错, 信息:\n"+str(err)
                log("§c" + errmsg, info = f"§e plugin §r {cserver}")
        for i in threadList[:]:
            try:
                if i.name == "与NekoMaid网站通信":
                    for j in text.split("\n"):
                        NekoMaidMsg(["NekoMaid:console:log", {"level": "INFO", "logger": "net.minecraft.server.v1_16_R3.DedicatedServer", "msg": "%s§r" % "["+datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+"] "+j.replace("'", 'unchanged'), "time": time.time()*1000}], "42", i.data["conn"], True)
            except:
                pass
    FBlog_old = []
    def FBlogRead() -> str:pass
    gameTime = "00:00:00"
    tps = {"1s": 0, "5s": 0, "20s": 0, "1m": 0, "5m": 0, "10m": 0}
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
    def floatPos2intPos(number: float | str) -> int:
        if type(number) == str:
            number = float(number)
        if type(number) == int:
            return number
        if int(number) == number:
            return int(number)
        if number >= 0:
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
    def getGameTimeRepeat(self) -> None:
        gameTimeTickLast = 0
        timeLastGet = 0
        tpsList = [20] * 1200
        while True:
            try:
                timeStart = time.time()
                timeGet = time.time()
                gameTimeTick = (int(sendcmd("/time query daytime", True, timeout = 20)["OutputMessages"][0]["Parameters"][0])+6000)%24000
                gameTime = second2minsec(round(gameTimeTick / 24000*86400))
                tps_1s = float("%.2f" % ((gameTimeTick-gameTimeTickLast)/(timeGet-timeLastGet)))
                if tps_1s > 0 and tps_1s < 50:
                    tpsList.append(tps_1s)
                if len(tpsList) > 1200:
                    tpsList = tpsList[-1200:]
                if len(tpsList) >= 2:
                    tps["1s"] = float("%.2f" % (sum(tpsList[-2:])/2))
                if len(tpsList) >= 10:
                    tps["5s"] = float("%.2f" % (sum(tpsList[-10:])/10))
                if len(tpsList) >= 40:
                    tps["20s"] = float("%.2f" % (sum(tpsList[-40:])/40))
                if len(tpsList) >= 120:
                    tps["1m"] = float("%.2f" % (sum(tpsList[-120:])/120))
                if len(tpsList) >= 600:
                    tps["5m"] = float("%.2f" % (sum(tpsList[-600:])/600))
                if len(tpsList) >= 1200:
                    tps["10m"] = float("%.2f" % (sum(tpsList[-1200:])/1200))
            except Exception as err:
                errmsg = "getGameTimeRepeat()函数报错, 信息:\n"+str(err)
                _color.color("§c"+traceback.format_exc(), info = f"§e plugin §r {cserver}")
                log("§c" + errmsg, sendtogamewithERROR = False, info = f"§e plugin §r {cserver}")
            finally:
                while time.time() - timeStart < 0.5:
                    constChangeLock.acquire()
                    try:
                        for i in [const, const2]:
                            for j in [const, const2]:
                                for k in ["__dict_hidden__", "__dict_hidden2__"]:
                                    for l in ["__dict_hidden__", "__dict_hidden2__"]:
                                        if object.__getattribute__(i, k) != object.__getattribute__(j, l):
                                            exitChatbarMenu(reason = "§cConst has been changed?! You SHOULD NOT edit const!")
                    except:
                        exitChatbarMenu(reason = "§cConst has been changed?! You SHOULD NOT edit const!")
                    constChangeLock.release()
                    time.sleep(0.001)
                gameTimeTickLast = gameTimeTick
                timeLastGet = timeGet
    def getType(sth):return sth.__class__.__name__
    def pluginRepeat(self) -> None:
        """
        命令系统启动后处理repeat类插件的函数
        你不应该使用此函数, 命令系统会自动以新线程运行它
        """
        timeDict = {"1s": {"time": 1, "timeNow": 0}, "10s": {"time": 10, "timeNow": 0}, "1m": {"time": 60, "timeNow": 0}}
    def othersRepeat(self) -> None:
        """
        命令系统启动后每60秒运行1次的函数
        你不应该使用此函数, 命令系统会自动以新线程运行它
        """
        while True:
            timeStart = time.time()
            try:
                allplayers = getTarget('@a[name=!"%s"]' % robotname, timeout = 60)
            except Exception as err:
                pass
            finally:
                while time.time() - timeStart < 60:
                    time.sleep(1)
    def _delayExec(self):
        timeDelay = self.data["delay"]
        func = self.data["func"]
        time.sleep(timeDelay)
        try:
            if type(func).__name__ == "str":
                exec(func)
            else:
                func()
        except Exception as err:
            errmsg = "延迟执行报错, 信息:\n"+str(err)
            _color.color("§c"+traceback.format_exc(), info = f"§e plugin §r {cserver}")
            log("§c" + errmsg, info = f"§e plugin §r {cserver}", sendtogamewithERROR = False)
    def delayExec(func, delay):
        createThread("延迟执行", data = {"delay": delay, "func": func}, func = _delayExec, output = False)
    def getPlayerData(dataName: str, playerName: str, writeNew: str = "") -> (str | int | float):
        """
        获取玩家本地数据的函数
        读取文件: player\playerName\dataName.txt

        参数:
            dataName: str -> 数据名称
            playerName: str -> 玩家名称
            writeNew: str -> 若数据不存在, 写入的数据
        返回: str | int | float -> 文件读取结果
        """
        dataName = dataName.replace("\\", "/")
        fileDir = "player/%s/%s.txt" % (playerName, dataName)
        pathDir = ""
        pathAll = ("player/%s/%s" % (playerName, dataName)).split("/")
        pathAll.pop(-1)
        for i in pathAll:
            pathDir += "%s/" % i
        if not os.path.isdir(pathDir):
            pathToCreate = ""
            for i in pathDir.split("/"):
                try:
                    pathToCreate += "%s/" % i
                    os.mkdir(pathToCreate)
                except:
                    pass
        if not os.path.isfile(fileDir):
            with open(fileDir, "w", encoding = "utf-8", errors = "ignore") as file:
                file.write(writeNew)
        with open(fileDir, "r", encoding = "utf-8", errors = "ignore") as file:
            data = file.read()
        if "." not in data:
            try:
                data = int(data)
            except:
                pass
        else:
            try:
                data = float(data)
            except:
                pass
        return data
    def setPlayerData(dataName: str, playerName: str, dataValue, writeNew: str = ""):
        """
        设置玩家本地数据的函数
        写入文件: player\playerName\dataName.txt

        参数:
            dataName: str -> 数据名称
            playerName: str -> 玩家名称
            dataValue: Any -> 要设置的数据, 写入前会自动转化为str
            writeNew: str -> 若数据不存在, 写入的数据
        返回: dataValue: Any -> 设置结果
        """
        dataName = dataName.replace("\\", "/")
        fileDir = "player/%s/%s.txt" % (playerName, dataName)
        pathDir = ""
        pathAll = ("player/%s/%s" % (playerName, dataName)).split("/")
        pathAll.pop(-1)
        for i in pathAll:
            pathDir += "%s/" % i
        if not os.path.isdir(pathDir):
            pathToCreate = ""
            for i in pathDir.split("/"):
                try:
                    pathToCreate += "%s/" % i
                    os.mkdir(pathToCreate)
                except:
                    pass
        if not os.path.isfile(fileDir):
            with open(fileDir, "w", encoding = "utf-8", errors = "ignore") as file:
                file.write(writeNew)
        with open(fileDir, "w", encoding = "utf-8", errors = "ignore") as file:
            file.write(str(dataValue))
        return dataValue
    def addPlayerData(dataName: str, playerName: str, dataValue, dataType: str = "int", writeNew: str = ""):
        """
        增加/追加玩家本地数据的函数
        写入文件: player\playerName\dataName.txt

        参数:
            dataName: str -> 数据名称
            playerName: str -> 玩家名称
            dataValue: Any -> 要设置的数据, 写入前会自动转化为str
            dataType: "int" | "add" -> 设置类型
                add: 在文件末尾追加
                int: 数学计算, 加上新值
            writeNew: str -> 若数据不存在, 写入的数据
        返回: dataValue: Any -> 设置结果
        """
        if dataType == "int":
            return setPlayerData(dataName, playerName, getPlayerData(dataName, playerName, writeNew)+dataValue, writeNew)
        elif dataType == "add":
            dataName = dataName.replace("\\", "/")
            fileDir = "player/%s/%s.txt" % (playerName, dataName)
            pathDir = ""
            pathAll = ("player/%s/%s" % (playerName, dataName)).split("/")
            pathAll.pop(-1)
            for i in pathAll:
                pathDir += "%s/" % i
            if not os.path.isdir(pathDir):
                pathToCreate = ""
                for i in pathDir.split("/"):
                    try:
                        pathToCreate += "%s/" % i
                        os.mkdir(pathToCreate)
                    except:
                        pass
            with open(fileDir, "a", encoding = "utf-8", errors = "ignore") as file:
                file.write("%s\n" % str(dataValue))
            return dataValue
        else:
            raise Exception("dataType error")
    def getTarget(sth: str, timeout: bool | int = 1) -> list:
        """
        获取租赁服内对应目标选择器实体的函数

        参数:
            sth: str.MinecraftTargetSelector -> 要获取的目标选择器
        返回: list -> 获取结果
        例子:
        >>> a = getTarget("@a")
        >>> print(a)
        ["player1", "player2", ...]
        """
        if not sth.startswith("@"):
            raise Exception("Minecraft Target Selector is not correct.")
        result = sendcmd("/tell @s get%s" % sth, True, timeout)["OutputMessages"][0]["Parameters"][1][3:]
        if ", " not in result:
            if not result:
                return []
            return [result]
        else:
            return result.split(", ")
    def getScoreboardList() -> list:
        result = []
        resultList = sendcmd("/scoreboard objectives list", True)["OutputMessages"]
        if resultList[0]["Success"] == False:
            return result
        for scoreboard in resultList:
            if scoreboard["Message"] == "commands.scoreboard.objectives.list.entry":
                scoreboardCmdName = scoreboard["Parameters"][0]
                scoreboardDisplayName = scoreboard["Parameters"][1]
                result.append(scoreboardCmdName)
        return result
    def getTickingAreaList() -> dict:
        result = {}
        resultList = sendcmd("/tickingarea list all-dimensions", True)["OutputMessages"]
        if resultList[0]["Success"] == False:
            return result
        for tickareaData in resultList[1]["Message"].split("%dimension.dimensionName")[1:]:
            tickareaDimension = tickareaData.split(": \n")[0]
            tickareaList = tickareaData.split(": \n")[1].split("\n")
            for tickarea in tickareaList:
                if not tickarea:
                    continue
                tickareaName = tickarea.split("- ", 1)[1].split(": ", 1)[0]
                tickareaPos = {"start": tickarea.split(" ")[2:5], "end": tickarea.split(" ")[6:9]}
                tickareaPos["start"].pop(1)
                tickareaPos["end"].pop(1)
                result[tickareaName] = {"dimension": tickareaDimension}
                result[tickareaName].update(tickareaPos)
        return result
    def getTag(targetName) -> list:
        result = []
        resultList = sendcmd("/tag %s list" % targetName, True)["OutputMessages"][0]
        if resultList["Success"] == False:
            raise Exception(resultList["Message"])
        try:
            targetNum = int(resultList["Parameters"][0])
        except:
            targetNum = 1
        if len(resultList["Parameters"]) != 3:
            return {"targetNum": targetNum, "tag": result}
        for tag in resultList["Parameters"][2].split(", "):
            result.append(tag[2:])
        return {"targetNum": targetNum, "tag": result}
    def getBlock(x, y, z):
        result = sendcmd("/testforblock %d %d %d structure_void" % (x, y, z), True)["OutputMessages"][0]
        if result["Success"] == True:
            return "structure_void"
        if result["Message"] != "commands.testforblock.failed.tile":
            raise Exception(result["Message"])
        return result["Parameters"][3][6:-5]
    def getMultiBlock(startX, startY, startZ, endX, endY, endZ):
        """
        获取主世界一处范围内的方块的函数 (区域需要被加载)
        ---

        参数:
            startX/Y/Z: int -> 范围起点.
            endX/Y/Z: int -> 范围终点.

        返回:
            dict -> 获取结果.

        例子:
            >>> result = getMultiBlock(77910, 0, 77910, 77919, 9, 77919) # 用时: 0.9s
            >>> print(result)
            {'77910 0 77910': 'seaLantern', '77910 0 77911': 'seaLantern', ...}
            >>> print(len(result))
            1000
        """
        (startX, endX) = (endX, startX) if (startX > endX) else (startX, endX)
        (startY, endY) = (endY, startY) if (startY > endY) else (startY, endY)
        (startZ, endZ) = (endZ, startZ) if (startZ > endZ) else (startZ, endZ)
        cmds = []
        for x in range(startX, endX+1):
            for y in range(startY, endY+1):
                for z in range(startZ, endZ+1):
                    cmds.append("/testforblock %d %d %d structure_void" % (x, y, z))
        resultList = {}
        for result in sendmulticmd(cmds, waitForResponse = True, timeout = 10):
            result = result["OutputMessages"][0]
            if result["Success"] == True:
                raise Exception(result["Message"])
            if result["Message"] != "commands.testforblock.failed.tile":
                raise Exception(result["Message"])
            resultList["%s %s %s" % tuple(result["Parameters"][0:3])] = result["Parameters"][3][6:-5]
        return resultList
    def getScore(scoreboardNameToGet: str, targetNameToGet: str) -> int:
        """
        获取租赁服内对应计分板数值的函数

        参数:
            scoreboardName: str -> 计分板名称
            targetName: str -> 计分板对象名称
        返回: int -> 获取结果
        """
        resultList = sendcmd("/scoreboard players list %s" % targetNameToGet, True)["OutputMessages"]
        result = {}
        result2 = {}
        for i in resultList:
            Message = i["Message"]
            if Message == "commands.scoreboard.players.list.player.empty":
                continue
            elif Message == "§a%commands.scoreboard.players.list.player.count":
                targetName = i["Parameters"][1][1:]
            elif Message == "commands.scoreboard.players.list.player.entry":
                if targetName == "commands.scoreboard.players.offlinePlayerName":
                    continue
                scoreboardName = i["Parameters"][2]
                targetScore = int(i["Parameters"][0])
                if targetName not in result:
                    result[targetName] = {}
                result[targetName][scoreboardName] = targetScore
                if scoreboardName not in result2:
                    result2[scoreboardName] = {}
                result2[scoreboardName][targetName] = targetScore
        if not(result or result2):
            raise Exception("Failed to get the score.")
        try:
            if targetNameToGet == "*" or targetNameToGet.startswith("@"):
                if scoreboardNameToGet == "*":
                    return [result, result2]
                else:
                    return result2[scoreboardNameToGet]
            else:
                if scoreboardNameToGet == "*":
                    return result[targetNameToGet]
                else:
                    return result[targetNameToGet][scoreboardNameToGet]
        except KeyError as err:
            raise Exception("Failed to get score: %s" % str(err))
    def getPos(targetNameToGet: str, timeout: float | int = 1) -> dict:
        """
        获取租赁服内玩家坐标的函数

        参数:
            targetNameToGet: str -> 玩家名称
        返回: dict -> 获取结果
        """
        if (targetNameToGet not in allplayers) and (targetNameToGet != robotname) and (not targetNameToGet.startswith("@a")):
            raise Exception("Player not found.")
        result = sendcmd("/querytarget %s" % targetNameToGet, True, timeout)["OutputMessages"][0]
        if result["Success"] == False:
            raise Exception("Failed to get the position.")
        resultList = json.loads(result["Parameters"][0])
        result = {}
        for i in resultList:
            targetName = XUID2playerName[i["uniqueId"][-8:]]
            x = i["position"]["x"]
            y = i["position"]["y"] - 1.6200103759765
            z = i["position"]["z"]
            position = {"x": float("%.2f" % x), "y": float("%.2f" % y), "z": float("%.2f" % z)}
            dimension = i["dimension"]
            yRot = i["yRot"]
            result[targetName] = {"dimension": dimension, "position": position, "yRot": yRot}
        if targetNameToGet == "@a":
            return result
        else:
            if len(result) != 1:
                raise Exception("Failed to get the position.")
            if targetNameToGet.startswith("@a"):
                return list(result.values())[0]
            else:
                return result[targetNameToGet]
    def getItem(targetName: str, itemName: str, itemSpecialID: int = -1) -> int:
        """
        获取租赁服内玩家某物品个数的函数

        参数:
            targetName: str -> 玩家名称
            itemName: str -> 物品英文名称
            itemSpecialID: int -> 物品特殊值
        返回: int -> 获取结果
        """
        if (targetName not in allplayers) and (targetName != robotname) and (not targetName.startswith("@a")):
            raise Exception("Player not found.")
        result = sendcmd("/clear %s %s %d 0" % (targetName, itemName, itemSpecialID), True)
        if result["OutputMessages"][0]["Message"] == "commands.generic.syntax":
            raise Exception("Item name error.")
        if result["OutputMessages"][0]["Message"] == "commands.clear.failure.no.items":
            return 0
        else:
            return int(result["OutputMessages"][0]["Parameters"][1])
    def getStatus(statusName: str) -> str:
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
    def setStatus(statusName: str, status):
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
    def QRcode(text: str, where: str = "return", who: str | None = None) -> None:
        """
        在控制台或租赁服输出二维码的函数

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
            _color.color(QRstring.replace("0", "\033[0;37;7m  ").replace("1", "\033[0m  ")+"§r", info=f"§e plugin §r {cserver}")
        if where == "chatbar":
            for line in QRstring.split("\n"):
                tellrawText(who, text = "§l"+line.replace("0", "§f▓").replace("1", "§0▓"))
        if where == "actionbar":
            sendwocmd("/title %s actionbar §l" % who + QRstring.replace("0", "§f█").replace("1", "§0█") + "\n" * 15)
    "\033[0m  " "\033[0;37;7m  "
    "§0█" "§f█"
    "▓"    
    sendcmdResponse = {}
    def sendcmd(cmd: str, waitForResponse: bool = False, timeout: float | int = 1) -> None:
        """
        以 WebSocket 身份发送指令到租赁服的函数
        ---

        参数:
            cmd: str (Minecraft command) -> 要在租赁服执行的指令.
            waitForResponse: bool -> 是否等到收到命令执行结果再返回结果.
                False: 不等结果, 直接返回命令执行的uuid. `(一瞬间)`
                True : 等到收到结果了再返回结果. `(需要1~2游戏刻)`
            timeout: number -> 等待返回结果的最长时间

        返回:
            `waitForResponse = False`:
                str : 命令执行的uuid.
            `waitForResponse = True `:
                Dict: 命令执行的返回结果.

        报错:
            TimeoutError: 等待命令执行结果超时.
        """
        if cmd[0] == "/":
            cmd = cmd[1:]
        uuid = conn.SendMCCommand(connect, cmd).decode("utf-8")
        if not waitForResponse:
            return uuid
        else:
            sendcmdResponse[uuid] = None
            startTime = time.time()
            while not sendcmdResponse[uuid]:
                if int(time.time() - startTime) > timeout:
                    del sendcmdResponse[uuid]
                    raise TimeoutError("timed out")
                time.sleep(0.001)
            result = sendcmdResponse[uuid]
            del sendcmdResponse[uuid]
            return result
    def sendmulticmd(cmds: list[str], waitForResponse: bool = False, timeout: float | int = 1) ->list[dict]:
        """
        以 WebSocket 身份发送多条指令到租赁服的函数
        ---

        参数:
            cmd: list[str] (Minecraft command) -> 要在租赁服执行的指令列表.
            waitForResponse: bool -> 是否等到收到命令执行结果再返回结果.
                False: 不等结果, 直接返回命令执行的uuid. `(一瞬间)`
                True : 等到收到结果了再返回结果. `(需要1~2游戏刻)`
            timeout: number -> 等待返回结果的最长时间.

        返回:
            `waitForResponse = False`:
                list[str] : 命令执行的uuid列表.
            `waitForResponse = True `:
                list[dict]: 命令执行的返回结果.

        报错:
            TimeoutError: 等待命令执行结果超时.

        例子:
            >>> cmds = ["/say %d" % i for i in range(100)]
            >>> sendmulticmd(cmds)
            [22:17:06]  信息  8 <外部> 0
            [22:17:06]  信息  8 <外部> 1
            [22:17:06]  信息  8 <外部> 2
            ...

            >>> cmds = [
            ...     "/scoreboard players set @a a 0",
            ...     "/scoreboard players set @a b 0",
            ...     "/scoreboard players set @a c 0"
            ... ]
            >>> print(sendmulticmd(cmds, "True"))
            [命令1执行结果, 命令2执行结果, 命令3执行结果]
        """
        resultList = []
        uuidList = []
        startTime = time.time()
        for cmd in cmds:
            if cmd[0] == "/":
                cmd = cmd[1:]
            uuid = conn.SendMCCommand(connect, cmd).decode("utf-8")
            if not waitForResponse:
                resultList.append(uuid)
            else:
                uuidList.append(uuid)
                sendcmdResponse[uuid] = None
        if resultList:
            return resultList
        while not all(sendcmdResponse[i] for i in uuidList):
            if int(time.time() - startTime) > timeout:
                for uuid in uuidList:
                    del sendcmdResponse[uuid]
                raise TimeoutError("timed out")
            time.sleep(0.001)
        for uuid in uuidList:
            resultList.append(sendcmdResponse[uuid])
            del sendcmdResponse[uuid]
        return resultList
    def sendplayercmd(cmd: str, waitForResponse: bool = False) -> None:
        """
        以 玩家(FastBuilder机器人) 身份发送指令到租赁服的函数
        ---

        参数:
            cmd: str (Minecraft command) -> 要在租赁服执行的指令.
            waitForResponse: bool -> 是否等到收到命令执行结果再返回结果.
                False: 不等结果, 直接返回命令执行的uuid. `(一瞬间)`
                True : 等到收到结果了再返回结果. `(需要1~2游戏刻)`
            timeout: number -> 等待返回结果的最长时间

        返回:
            `waitForResponse = False`:
                str : 命令执行的uuid.
            `waitForResponse = True `:
                Dict: 命令执行的返回结果.

        报错:
            TimeoutError: 等待命令执行结果超时.
        """
        if cmd[0] == "/":
            cmd = cmd[1:]
        uuid = conn.SendWSCommand(connect, cmd).decode("utf-8")
        if not waitForResponse:
            return uuid
        else:
            sendcmdResponse[uuid] = None
            startTime = time.time()
            while not sendcmdResponse[uuid]:
                if int(time.time() - startTime) > 1:
                    del sendcmdResponse[uuid]
                    raise TimeoutError("timed out")
                time.sleep(0.001)
            result = sendcmdResponse[uuid]
            del sendcmdResponse[uuid]
            return result
    def sendwocmd(cmd: str) -> None:
        """
        以最高权限(租赁服控制台)身份发送指令到租赁服的函数
        ---

        你可以执行 /stop, 这会导致租赁服关闭, 然后重启

        参数:
            cmd: str (Minecraft command) -> 要在租赁服执行的指令.
        """
        if cmd[0] == "/" or cmd[0] == "!":
            cmd = cmd[1:]
        if cmd.startswith("stop"):
            _color.color("You can not use the command 'stop'.",info=f"§e plugin §r {cserver}")
        conn.SendNoResponseCommand(connect, cmd)
    def sendfbcmd(cmd: str) -> None:
        """
        发送命令到FastBuilder的函数

        参数:
            cmd: str (FastBuilder command) -> FastBuilder执行指令
        返回: 无返回值
        """
        if cmd[0] == "?":
            cmd = cmd[1:]
        conn.SendFBCommand(connect, cmd)
    def tellrawText(who: str, dispname: None | str = None, text: str = None, mode = sendcmd) -> None:
        """
        便捷执行tellraw的函数

        参数:
            who: str.MinecraftTargetSelector -> 给谁显示
            dispname: None | str -> 模拟玩家说话格式, 不传则直接tellraw
            text: str -> 要显示的信息
        返回: 无返回值
        """
        if dispname is None:
            mode(r"""/tellraw %s {"rawtext":[{"text":"%s"}]}""" % (who, text.replace('"', '’’').replace("'", '’')))
        else:
            mode(r"""/tellraw %s {"rawtext":[{"text":"<%s> %s"}]}""" % (who, dispname.replace('"', '’’').replace("'", '’'), text.replace('"', '’’').replace("'", '’')))
    def tellrawScore(scoreboardName: str, targetName: str) -> str:
        """
        返回tellraw计分板格式的函数

        参数:
            scoreboardName: str -> 计分板名称
            targetName: str -> 计分板对象
        返回: str -> tellraw计分板格式
        """
        return '{"score":{"name":"%s","objective":"%s"}}' % (targetName, scoreboardName)
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
    PWordResponse = {}
    def prohibitedWordTest(word):
        uuid = sendcmd("%s 测试 %d" % (word, random.randint(0, 100)))
        PWordResponse[uuid] = False
        result = sendcmd("Finished test.", True, 5)
        if not PWordResponse[uuid]:
            del PWordResponse[uuid]
            return True
        else:
            del PWordResponse[uuid]
            return False


    msgList = []
    rev = ""
    playername = ""
    allplayers = []
    robotname = ""
    XUID2playerName = {}
    msgLastRecvTime = time.time()
    itemNetworkID2NameDict = {}
    itemNetworkID2NameEngDict = {}
    adminhigh = []
    savePacket = False

    """""""""""
    CLASS PART
    """""""""""
    class PluginSkip(Exception):
        pass


    constChangeLock = threading.Lock()
    class _const():
        def __init__(self):
            object.__setattr__(self, "__dict_hidden__", {})
            object.__setattr__(self, "__dict_hidden2__", {})

        def __setattr__(self, key, value):
            for i in [self, const, const2]:
                if key in object.__getattribute__(i, "__dict_hidden__"):
                    raise Exception("You can not change a const variable.")
            constChangeLock.acquire()
            object.__getattribute__(const, "__dict_hidden__").update({key: value})
            object.__getattribute__(const, "__dict_hidden2__").update({key: value})
            object.__getattribute__(const2, "__dict_hidden__").update({key: value})
            object.__getattribute__(const2, "__dict_hidden2__").update({key: value})
            constChangeLock.release()

        def __delattr__(self, key):
            if key in object.__getattribute__(self, "__dict_hidden__"):
                raise Exception("You can not delete a const variable.")
            else:
                raise AttributeError(key)

        def __getattribute__(self, key):
            result = object.__getattribute__(self, "__dict_hidden__")
            if key not in object.__getattribute__(self, "__dict_hidden__"):
                raise KeyError(key)
            return result[key]

        def __dir__(self):
            raise Exception("You can not access this.")
    const = _const()
    const2 = _const()

    class createThread(threading.Thread):
        def __init__(self, name, data = {}, func = "", output = True):
            threading.Thread.__init__(self)
            self.name = name
            self.data = data
            self.func = func
            self.stopping = False
            self.output = output
            threadList.append(self)
            self.start()

        def run(self):
            try:
                if self.output:
                    _color.color("§e启动线程 %s." % self.name, info = f"§e plugin §r {cserver}")
                if getType(self.func) != "str":
                    self.func(self)
                else:
                    exec("%s(self)" % self.func)
            except Exception as err:
                errmsg = ("线程 %s 报错, 信息:\n" % self.name)+str(err)
                _color.color("§c"+traceback.format_exc(), info = f"§e plugin §r {cserver}")
                log("§c" + errmsg, sendtogamewithERROR = False, info = f"§e plugin §r {cserver}")
            except SystemExit as err:
                pass
                # color("§eThread %s has been terminated forcely." % self.name)
            finally:
                if self.output:
                    _color.color("§e终止线程 %s." % self.name, info = f"§e plugin §r {cserver}")
                threadList.remove(self)

        def get_id(self):
            if hasattr(self, '_thread_id'):
                return self._thread_id
            for id, thread in threading._active.items():
                if thread is self:
                    return id

        def stop(self):
            self.stopping = True
            # _color.color("§eTerminating thread %s." % self.name)
            thread_id = self.get_id()
            res = ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, ctypes.py_object(SystemExit))
            if res > 1:
                ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, 0)
                _color.color("§c终止线程失败", info = f"§e plugin §r {cserver}")

    
    pluginList = []
    class plugin():
        def __init__(self, pluginName, pluginCode):
            self.pluginName = pluginName
            self.pluginCode = pluginCode
            self.enable = True
            self.globals = globals()
            self.locals = {}
            pluginList.append(self)
    server = "123456"
    version = date.version
    # 加载插件
    # if "获取玩家手持物品.py" in os.listdir("plugin"):
    #     os.remove("plugin/获取玩家手持物品.py")
    # if getStatus("pluginupdate1") != "update":
    #     fileDownload("http://www.dotcs.community/update/获取玩家手持物品或装备.py", "plugin/获取玩家手持物品或装备.py")
    #     setStatus("pluginupdate1", "update")
    _color.color("§e正在加载插件.", info = f"§e plugin §r {cserver}")
    _color.color("§e[总进度 0/3] 初始化.", info = f"§e plugin §r {cserver}")
    if os.path.isdir("plugin/old/data/temp"):
        shutil.rmtree("plugin/old/data/temp")
    os.makedirs("plugin/old/data/temp")
    os.makedirs("plugin/old/data/temp/文件夹说明：这是插件加载的临时文件夹.")
    os.makedirs("plugin/old/data/temp/文件夹说明：请不要修改这里的内容. （改了也没用）")
    _color.color("§e[总进度 1/3] 正在读取插件.", info = f"§e plugin §r {cserver}")
    pluginlist = []
    pluginCode = None
    pluginCodeDict = {}
    pluginCodeList = []
    i = None
    for filename in os.listdir("plugin/old"):
        if filename.endswith(".py") or filename.endswith(".py.enc"):
            pluginlist.append(filename)
    for i in range(len(pluginlist)):
        filename = pluginlist[i]
        _color.color("§e[总进度 1/2][插件 %d/%d] 加载插件: %s" % (i+1, len(pluginlist), filename), info = f"§e plugin §r {cserver}")
        with open("plugin/old/"+filename, "rb") as file:
            if filename.endswith(".py.enc"):
                pluginCode = TDES.decrypt(file.read(), "DotCS Community plugin.", False)
            else:
                pluginCode = file.read()
            pluginCodeList = pluginCode.decode("utf-8").replace("\r", "").split("# PLUGIN TYPE: ")[1:]
            pluginCodeDict = {}
            for i in pluginCodeList:
                pluginType = i.split("\n", 1)[0]
                pluginCode = i.split("\n", 1)[1]
                filenameTemp = "plugin/old/data/temp/%s_%s" % (filename, pluginType)
                pluginCodeDict[pluginType] = compile(pluginCode, filename = filenameTemp, mode = "exec")
                with open(filenameTemp, "w", encoding = "utf-8") as file:
                    file.write(pluginCode)
            plugin(filename, pluginCodeDict)
    del pluginlist, pluginCode, pluginCodeList, pluginCodeDict, i
    _color.color("§e[总进度 2/3] 正在执行 def 类型插件.", info = f"§e plugin §r {cserver}")
    pluginRunType = "def"
    pluginIndex = 0
    for i in pluginList:
        pluginIndex += 1
        _color.color("§e[总进度 2/3][插件 %d/%d] 执行插件: %s" % (pluginIndex, len(pluginList), i.pluginName), info = f"§e plugin §r {cserver}")
        try:
            if i.enable and pluginRunType in i.pluginCode:
                exec(i.pluginCode[pluginRunType],locals())
        except Exception as err:
            errmsg = "插件 %s %s 报错, 信息:\n%s" % (i.pluginName, pluginRunType, str(err))
            _color.color("§c"+traceback.format_exc(), info = f"§e plugin §r {cserver}")
            log("§c" + errmsg, sendtogamewithERROR = False, info = f"§e plugin §r {cserver}")
            exitChatbarMenu(delay = 60, reason = "Load plugin %s %s error in step 2." % (i.pluginName, pluginRunType),load_Error=True)
    # for pluginType in ["packet %d" % packetType, pluginRunType]:
    # try:
    #     if pluginType in plugin.pluginCode:
    #         exec(plugin.pluginCode[pluginType],locals())
    for _ in pluginList:
        for i in _.pluginCode:
            
            if i.split(" ")[0] == "packet":
                print()
                try:
                    packets_listen.append(int(i.split(" ")[1]))
                except Exception as err:
                    pass
    _color.color("§a成功加载所有插件.", info = f"§e plugin §r {cserver}")
    # createThread("收取数据包", data = {}, func = revPacket)
    # createThread("检测命令系统更新并校准在线玩家", data = {}, func = othersRepeat)
    
    def processPacket(self) -> None:
        """
        处理FastBuilder发送来的包的函数
        你不应该使用此函数, 命令系统会在运行FastBuilder后以新线程启动此函数
        """
        try:
            msgList.append([-100, {"pluginRunType": "init"}, -1])
            sendwocmd("changesetting allow-cheats true")
            _color.color('§e正在检测机器人是否能正常执行指令.', info = f"§e plugin §r {cserver}")
            result = sendcmd("/time add 0", True, timeout = 20)["OutputMessages"][0]
            if result["Success"] == False:
                if result["Message"] == "commands.generic.unknown":
                    _color.color("§c执行命令失败: 未知的命令. 有可能是机器人没有op权限.", info = f"§e plugin §r {cserver}")
                if result["Message"] == "commands.generic.disabled":
                    _color.color("§c执行命令失败: 此等级未启用作弊. 有可能是未打开允许作弊.", info = f"§e plugin §r {cserver}")
                else:
                    _color.color("§c执行命令失败: %s." % result["Message"], info = f"§e plugin §r {cserver}")
                raise Exception("Can not execute operator commands.")

            sendcmd("/gamemode c")
            sendcmd("/effect @s resistance 999999 19 true")
            sendcmd("/effect @s invisibility 999999 0 true")

            _color.color("§e正在获取机器人游戏名和在线玩家.", info = f"§e plugin §r {cserver}")
            robotname = getTarget("@s", timeout = 20)[0]
            if ")" in robotname:
                _color.color("§cFastBuilder 机器人游戏名异常.", info = f"§e plugin §r {cserver}")
                exitChatbarMenu(reason = "Invalid FastBuilder robot name.")
            if robotname not in adminhigh:
                adminhigh.append(robotname)
            allplayers = getTarget("@a", timeout = 20)

            _color.color("§e正在检测在线玩家的游戏名中是否包含违禁词.", info = f"§e plugin §r {cserver}")
            for i in allplayers[:]:
                _color.color("§e正在检测: %s" % i, info = f"§e plugin §r {cserver}")
                hasPWord = False
                if getPlayerData("prohibitedWord", i, "False") == "False":
                    if prohibitedWordTest(i):
                        hasPWord = True
                        setPlayerData("prohibitedWord", i, "True")
                else:
                    hasPWord = True
                if hasPWord:
                    _color.color("§c玩家 %s 的游戏名中包含违禁词, 正在踢出." % i, info = f"§e plugin §r {cserver}")
                    sendwocmd('/kick "%s" §c您的名称内有违禁词, 无法进服.' % i)
                    allplayers.remove(i)

            _color.color("§e正在获取在线玩家的XUID.", info = f"§e plugin §r {cserver}")
            for i in allplayers:
                _color.color("§e正在获取: %s" % i, info = f"§e plugin §r {cserver}")
                result = sendcmd('/querytarget @a[name="%s"]' % i, True, timeout = 20)["OutputMessages"][0]
                if result["Success"] == False:
                    raise Exception("Failed to get the XUID.")
                XUID2playerName[json.loads(result["Parameters"][0])[0]["uniqueId"][-8:]] = i
            for i in allplayers:
                _color.color("§e正在验证: %s" % i,info = f"§e plugin §r {cserver}")
                if i not in list(XUID2playerName.values()):
                    raise Exception("Failed to get the XUID.")
            allplayers.remove(robotname)
            savePacket = True

            createThread("获取租赁服游戏时间并计算tps", data = {}, func = getGameTimeRepeat)
            createThread("执行repeat类插件", data = {}, func = pluginRepeat)

            timeSpentRun = 0
            timeSpentDotCSRun = 0
            _color.color("§a成功启动 DotCS 旧版本兼容引擎", info = f"§e plugin §r {cserver}")
            tellrawText("@a", "§l§6System§r", '§6".命令"系统成功启动.')
            tellrawText("@a", "§l§6System§r", "§6共加载 §l%d§r§6 个插件/函数." % len(pluginList))
            sendcmd("/time add 0")
            sendcmd("/kill @e[type=xp_orb]")
            sendcmd("/gamemode c")
            sendcmd("/effect @s resistance 999999 19 true")
            sendcmd("/effect @s invisibility 999999 0 true")
            sendcmd("/tp @s 100000 100000 100000")
            log("§6FastBuilder 机器人名: %s" % robotname, info = "§6  FB  ")
            log("§e当前在线玩家: "+(", ".join(allplayers)), info = "§e 信息 ")

            while True:
                if msgList == []:
                    if time.time()-msgLastRecvTime >= 45:
                        log("§c45秒未收到包", info = f"§e plugin §r {cserver}")
                        exitChatbarMenu(reason = "Receive packet timed out")
                    time.sleep(0.01)
                    continue
                try:
                    rev = msgList.pop(0)
                    packetType = rev[0]
                    jsonPkt = rev[1]
                    packetNum = rev[2]
                    pluginRunType = ""
                except:
                    continue
                if packetType == 63 and jsonPkt["ActionType"] == 0:
                    XUID2playerName[jsonPkt["Entries"][0]["XUID"]] = jsonPkt["Entries"][0]["Username"]
                    jsonPkt = {'TextType': 2, 'NeedsTranslation': True, 'SourceName': '', 'Message': '§e%multiplayer.player.joining', 'Parameters': [jsonPkt["Entries"][0]["Username"]], 'XUID': '', 'PlatformChatID': '', 'PlayerRuntimeID': ''}
                    packetType = 9

                # 已经实现类型数据的解析
                # 处理文字信息.
                if packetType == 9:
                    # 初始化
                    textType = jsonPkt["TextType"]
                    playername = jsonPkt["SourceName"]
                    msg = jsonPkt["Message"]
                    try:
                        playername = playername.replace(">§r", "").split("><")[1]
                    except:
                        pass

                    # 处理收到的say信息
                    # 将其统一格式
                    if textType == 8:
                        msg = msg.split("] ", 1)[1]

                    # 处理收到的tellraw信息
                    if textType == 9:
                        msg = msg.replace('{"rawtext":[{"text":"', "").replace('"}]}', "").replace('"},{"text":"', "").replace(r"\n", "\n"+str(textType)+" ").replace("§l", "")
                        if msg[-1] == "\n":
                            msg = msg[:-1]
                        if "报错, 信息:" not in msg:
                            msg += "§r"
                            log(str(textType)+" "+msg, info = " 信息 ")

                    # 处理系统信息
                    elif textType == 2:
                        # 处理玩家准备进服信息
                        if msg == "§e%multiplayer.player.joining":
                            playername = jsonPkt["Parameters"][0]
                            log("§e%s 正在加入游戏" % playername, info = " 信息 ")
                            hasPWord = False
                            if getPlayerData("prohibitedWord", playername, "False") == "False":
                                if prohibitedWordTest(playername):
                                    hasPWord = True
                                    setPlayerData("prohibitedWord", playername, "True")
                            else:
                                hasPWord = True
                            if hasPWord:
                                log("§c玩家 %s 的游戏名中包含违禁词, 正在踢出." % playername, info = f"§e plugin §r {cserver}")
                                sendwocmd('/kick "%s" §c您的名称内有违禁词, 无法进服.' % playername)
                                continue
                            pluginRunType = "player prejoin"

                        # 处理玩家进服信息
                        if msg == "§e%multiplayer.player.joined":
                            playername = jsonPkt["Parameters"][0]
                            if playername not in allplayers:
                                allplayers.append(playername)
                            log("§e%s 加入了游戏" % playername, info = " 信息 ")
                            pluginRunType = "player join"

                        # 处理玩家退出信息
                        elif msg == "§e%multiplayer.player.left":
                            playername = jsonPkt["Parameters"][0]
                            if playername in allplayers:
                                allplayers.remove(playername)
                            log("§e%s 退出了游戏" % playername, info = " 信息 ")
                            sendcmd("/scoreboard players reset %s" % playername)
                            pluginRunType = "player leave"

                        # 处理玩家死亡信息
                        elif msg[0:6] == "death.":
                            playername = jsonPkt["Parameters"][0]
                            if playername in allplayers:
                                if len(jsonPkt["Parameters"]) == 2:
                                    killer = jsonPkt["Parameters"][1]
                                else:
                                    killer = None
                                log("%s 失败了, 信息: %s" % (playername, msg), info = " 信息 ")
                                pluginRunType = "player death"

                        # 过滤其他信息
                        else:
                            pass

                    # 处理玩家在聊天栏发送的信息, tell信息以及say信息
                    elif textType == 1 or textType == 7 or textType == 8:
                        if not (msg.startswith("test") or msg.startswith("get")):
                            log(str(textType)+" <"+playername+">"+" "+msg, info = " 信息 ")
                        if playername in allplayers or playername == robotname:
                            pluginRunType = "player message"


                if packetType == -100:
                    pluginRunType = jsonPkt["pluginRunType"]

                for plugin in pluginList:
                    if plugin.enable:
                        for pluginType in ["packet %d" % packetType, pluginRunType]:
                            try:
                                if pluginType in plugin.pluginCode:
                                    exec(plugin.pluginCode[pluginType],locals())
                            except PluginSkip: # 感谢SuperScript提供的建议.
                                pass
                            except Exception as err:
                                errmsg = "插件 %s %s 报错, 信息:\n%s" % (plugin.pluginName, pluginRunType, str(err))

                                # 更好地输出错误信息.
                                console.print_exception(width = int(console.width*0.9))
                                # color("§c"+traceback.format_exc(), info = f"§e plugin §r {cserver}")

                                log("§c" + errmsg, sendtogamewithERROR = False, info = f"§e plugin §r {cserver}")


        except Exception as err:
            errmsg = "信息处理报错, 信息:\n"+str(err)
            color("§c"+traceback.format_exc(), info = f"§e plugin §r {cserver}")
            log("§c" + errmsg, info = f"§e plugin §r {cserver}")
            exitChatbarMenu(reason = "Process packet error.")











    connect = ""
    last_packets_listen_time = time.time()

    def pipe_listen(conn_in_Pipe, conn_out_Pipe):
        nonlocal packets_listen, connect
        "输出获取"
        while (1):
            date = conn_in_Pipe.recv()
            match date["type"]:
                case "listen_add":  # {"type":"listen_add","id":监听数据包类型id:int}
                    if date["id"] in packets_listen:
                        conn_in_Pipe.send(
                            {"type": "error", "messags": f"{date[id]}数据包已被监听"})
                    else:
                        packets_listen.append(date["id"])
                        conn_in_Pipe.send(
                            {"type": "listen_add", "messags": f"{date[id]}数据包 已添加成功"})
                case "listen_update":
                    packets_listen = date["packets_listen"]
                    conn_in_Pipe.send(
                        {"type": "packets_listen_update", "messags": f"数据包列表信息已更新 已添加成功"})

    def fb_listen(conn_in_Pipe, fb_out_Pipe):
        
        while (1):
            date = fb_out_Pipe.recv()
            if date["type"] == "reload":
                conn_in_Pipe.send(
                    {"type": "listen_error", "messags": "FB进程关闭重启"})
                return
    
    def time_listen(conn_in_Pipe, conn_out_Pipe):
        # 引擎超时检测线程
        nonlocal last_packets_listen_time
        while time.time()-last_packets_listen_time < 30:
            time.sleep(1)
        color.color(cserver, "§4哎呀,FB是不是崩了?超时了呀,给爷重启",
                    info=f"§e plugin §r {cserver}", word_wrapping=False)
        conn_in_Pipe.send({"type": "listen_error", "messags": "监听超时无反应"})

    pipe_listen_thread = threading.Thread(target=pipe_listen, args=Pipe)
    pipe_listen_thread.setDaemon(True)
    pipe_listen_thread.start()
    time_listen_thread = threading.Thread(target=time_listen, args=Pipe)
    time_listen_thread.setDaemon(True)
    time_listen_thread.start()
    fb_listen_thread = threading.Thread(
        target=fb_listen, args=(Pipe[0], fb_Pipe[1]))
    fb_listen_thread.setDaemon(True)
    fb_listen_thread.start()
    packetNum = 0
    while (1):
        try:
            connect = conn.ConnectFB(f"{ip}")
            connID = connect
            createThread("处理数据包", {}, processPacket)
            
            while True:
                try:
                    # 接收游戏数据包
                    bytesPkt = conn.RecvGamePacket(connect)
                    # 获得数据包的类型
                    packetType = conn.inspectPacketID(bytesPkt)
                    last_packets_listen_time = time.time()
                    msgLastRecvTime = time.time()
                    if packetType in packets_listen:
                        jsonPkt = json.loads(
                            conn.GamePacketBytesAsIsJsonStr(bytesPkt))
                        packetNum += 1
                        # return result
                        # color.color(cserver,"§a数据包内容§7:§b",load,info="§a plugin §r")
                        pluginRunType = "packet on another thread %d" % packetType
                        match packetType:
                            case 79:

                                uuid = jsonPkt["CommandOrigin"]["UUID"]
                                
                                for i in list(sendcmdResponse):
                                    if i == uuid:
                                        sendcmdResponse[i] = jsonPkt
                                for i in list(PWordResponse):
                                    if i == uuid:
                                        PWordResponse[i] = True
                        if savePacket:
                            msgList.append([packetType, jsonPkt, packetNum])
                        for i in pluginList:
                            try:
                                if i.enable and pluginRunType in i.pluginCode:
                                    exec(i.pluginCode[pluginRunType],locals())
                            except Exception as err:
                                errmsg = "插件 %s %s 报错, 信息:\n%s" % (i.pluginName, pluginRunType, str(err))
                                _color.color("§c"+traceback.format_exc(), info = f"§e plugin §r {cserver}")
                                log("§c" + errmsg, sendtogamewithERROR = False, info = f"§e plugin §r {cserver}")
                except Exception as err:
                    _color.color( "§4DotCS 插件监听进程发生了问题:", str(
                        err), info=f"§e plugin §r {cserver}", word_wrapping=False)
                    try:
                        conn.ReleaseConnByID(connect)
                    except Exception as errs:
                        _color.color( "§4DotCS 在尝试释放监听接口出了问题,这可能导致内存益处:", str(
                            errs), info=f"§e plugin §r {cserver}", word_wrapping=False)
                    # 处理两种数据包的示例,你可以自己选择要处理哪些数据包
                    Pipe[0].send({"type": "listen_error", "messags": "监听进程崩溃"})
                    return
        except Exception as err:
            _color.color( "§4DotCS 插件监听进程发生了问题:", str(
                err), info=f"§e plugin §r {cserver}", word_wrapping=False)
            Pipe[0].send({"type": "listen_error", "messags": "监听进程大崩"})
            return
