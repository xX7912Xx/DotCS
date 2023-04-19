import os,sys
import subprocess
def run_cmd_sync(cmd)->bool:
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,env=os.environ)
    while p.poll() is None:
        line = p.stdout.readline()
        line = line.strip()
        if line:
            try:
                print("\t",line.decode(encoding='utf-8'),flush=True) 
            except Exception as e:
                try:
                    print("\t",line.decode(encoding='gbk'),flush=True) 
                except Exception as e:
                    print("\t",line) 
    return p.returncode == 0

def install_lib(lib_name:str,lib_install_name:str=None,mirror_site:str="https://mirrors.bfsu.edu.cn/pypi/web/simple",python_exec:str=None)->bool:
    '''
        安装需要的库,lib_name 为 import时的名字,lib_install_name 为 pip install 时的名字
        一般来说,lib_name 和 lib_install_name 是一样的
        例如，如果要：
        import websocket 
        而库 websocket 是第三方库，用户没有安装,而这个库用pip安装时名字为websocket-client，那么可以
        install_lib(lib_name="websocket",lib_install_name="websocket-client")
    '''
    import importlib
    try:
        importlib.import_module(lib_name)
        return True
    except Exception as e:
        # print(e)
        pass 
    print(f"开始安装库: {lib_name}")
    if python_exec is None:
        python_exec=sys.executable
    # if install_path is None:
    #     install_path=omega_args.lib_3rd_install_path
    if lib_install_name is None:
        lib_install_name=lib_name
    # cmd=[python_exec,"-m","pip","install","-i",mirror_site,f"--target={install_path}",lib_install_name]
    cmd=[python_exec,"-m","pip","install","-i",mirror_site,lib_install_name]
    if run_cmd_sync(cmd):
        return True
    else:
        raise Exception(f"库 {lib_name} 安装失败")

install_lib("psutil")
install_lib("requests")
install_lib("pymysql")
install_lib("qrcode")
install_lib("websocket","websocket-client")
install_lib("brotli")
install_lib("PIL","pillow")
install_lib("rich")
install_lib("numpy")
install_lib("mido")
from genericpath import exists
import os 
print(os.getcwd(),flush=True)

title1 = \
"""
  ____        _    ____ ____     ____                                      _ _         
 |  _ \  ___ | |_ / ___/ ___|   / ___|___  _ __ ___  _ __ ___  _   _ _ __ (_) |_ _   _ 
 | | | |/ _ \| __| |   \___ \  | |   / _ \| '_ ` _ \| '_ ` _ \| | | | '_ \| | __| | | |
 | |_| | (_) | |_| |___ ___) | | |__| (_) | | | | | | | | | | | |_| | | | | | |_| |_| |
 |____/ \___/ \__|\____|____/   \____\___/|_| |_| |_|_| |_| |_|\__,_|_| |_|_|\__|\__, |
                                                                                 |___/ 
"""
title4 = \
"""
┌────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
|                                                                                                            |
|                                                                                                            |
|    DDDDDDDDDDDDD                                  tttt                 CCCCCCCCCCCCC   SSSSSSSSSSSSSSS     |
|    D::::::::::::DDD                            ttt:::t              CCC::::::::::::C SS:::::::::::::::S    |
|    D:::::::::::::::DD                          t:::::t            CC:::::::::::::::CS:::::SSSSSS::::::S    |
|    DDD:::::DDDDD:::::D                         t:::::t           C:::::CCCCCCCC::::CS:::::S     SSSSSSS    |
|      D:::::D    D:::::D    ooooooooooo   ttttttt:::::ttttttt    C:::::C       CCCCCCS:::::S                |
|      D:::::D     D:::::D oo:::::::::::oo t:::::::::::::::::t   C:::::C              S:::::S                |
|      D:::::D     D:::::Do:::::::::::::::ot:::::::::::::::::t   C:::::C               S::::SSSS             |
|      D:::::D     D:::::Do:::::ooooo:::::otttttt:::::::tttttt   C:::::C                SS::::::SSSSS        |
|      D:::::D     D:::::Do::::o     o::::o      t:::::t         C:::::C                  SSS::::::::SS      |
|      D:::::D     D:::::Do::::o     o::::o      t:::::t         C:::::C                     SSSSSS::::S     |
|      D:::::D     D:::::Do::::o     o::::o      t:::::t         C:::::C                          S:::::S    |
|      D:::::D    D:::::D o::::o     o::::o      t:::::t    ttttttC:::::C       CCCCCC            S:::::S    |
|    DDD:::::DDDDD:::::D  o:::::ooooo:::::o      t::::::tttt:::::t C:::::CCCCCCCC::::CSSSSSSS     S:::::S    |
|    D:::::::::::::::DD   o:::::::::::::::o      tt::::::::::::::t  CC:::::::::::::::CS::::::SSSSSS:::::S    |
|    D::::::::::::DDD      oo:::::::::::oo         tt:::::::::::tt    CCC::::::::::::CS:::::::::::::::SS     |
|    DDDDDDDDDDDDD           ooooooooooo             ttttttttttt         CCCCCCCCCCCCC SSSSSSSSSSSSSSS       |
|                                                                                                            |
|                                                                                                            |
|                                                                                                            |
|                           ____                                      _ _                                    |
|                          / ___|___  _ __ ___  _ __ ___  _   _ _ __ (_) |_ _   _                            |
|                         | |   / _ \| '_ ` _ \| '_ ` _ \| | | | '_ \| | __| | | |                           |
|                         | |__| (_) | | | | | | | | | | | |_| | | | | | |_| |_| |                           |
|                          \____\___/|_| |_| |_|_| |_| |_|\__,_|_| |_|_|\__|\__, |                           |
|                                                                           |___/                            |
└────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
                  艺术字来源: http://patorjk.com/software/taag/#p=testall&t=DotCS%20Community                  
"""
print("\n"*30 + "http://www.dotcs.community/",flush=True)
threadList = []
exiting = False
exitDelay = 3
exitReason = None
connected = False
try:

    """""""""
    DEF PART
    """""""""
    def removeColorInText(text):
        return text.replace("\033[0;37;34m", "").replace("\033[0;37;32m", "").replace("\033[0;37;36m", "").replace("\033[0;37;31m", "").replace("\033[0;37;35m", "").replace("\033[0;37;33m", "").replace("\033[0;37;90m", "").replace("\033[0;37;2m", "").replace("\033[0;37;94m", "").replace("\033[0;37;92m", "").replace("\033[0;37;96m", "").replace("\033[0;37;91m", "").replace("\033[0;37;95m", "").replace("\033[0;37;93m", "").replace("\033[0;37;1m", "").replace("\033[0m", "").replace("\033[7;37;34m", "").replace("\033[7;37;32m", "").replace("\033[7;37;36m", "").replace("\033[7;37;31m", "").replace("\033[7;37;35m", "").replace("\033[7;37;33m", "").replace("\033[7;37;90m", "").replace("\033[7;37;2m", "").replace("\033[7;37;94m", "").replace("\033[7;37;92m", "").replace("\033[7;37;96m", "").replace("\033[7;37;91m", "").replace("\033[7;37;95m", "").replace("\033[7;37;93m", "").replace("\033[7;37;1m", "")


    def getTextColorInTheEnd(text):
        if "\033[" in text and "m" in text:
            return "\033[" + text.split("\033[")[-1].split("m")[0] + "m"
        else:
            return "\033[0m"


    lastOutputLen = 0
    lastReplace = False
    lastReplaceByNext = False
    print_Py = print
    def color(text: str, output: bool = True, end: str = "\n", replace: bool = False, replaceByNext: bool = False, info = " 信息 ") -> str:
        """
        在命令系统控制台输出信息
        ---

        参数:
            text: str -> 要输出的内容.
            output: bool -> 是否输出.
            end: str -> 输出时末尾的字符, 同print()中的.
            replace: bool -> 是否被下次输出覆盖.
                True: 若下次输出时 replace还是为True, 则这次输出将被下次输出覆盖, 否则不会被覆盖.
                False: 普通的输出.
            replaceByNext: bool -> 是否一定被下次输出覆盖.
                True : 这次输出将被下次输出覆盖.
                False: 普通的输出.
            info: str -> 输出内容前的反色信息.

        返回: str -> 输出
        """
        global lastOutputLen, lastReplace, lastReplaceByNext
        if replaceByNext:
            replace = True
        if type(text) != str:
            text = str(text)
        if text[-1] == "\n" and "Traceback" in text:
            text = text[:-1]
        if text.startswith("§"):
            text = text.replace("\n", "\n" + text[0:2])
        text = text.replace("§1", "\033[0;37;34m").replace("§2", "\033[0;37;32m").replace("§3", "\033[0;37;36m").replace("§4", "\033[0;37;31m").replace("§5", "\033[0;37;35m").replace("§6", "\033[0;37;33m").replace("§7", "\033[0;37;90m").replace("§8", "\033[0;37;2m").replace("§9", "\033[0;37;94m").replace("§a", "\033[0;37;92m").replace("§b", "\033[0;37;96m").replace("§c", "\033[0;37;91m").replace("§d", "\033[0;37;95m").replace("§e", "\033[0;37;93m").replace("§f", "\033[0;37;1m").replace("§r", "\033[0m")+"\033[0m"
        if info:
            info = info.replace("§1", "\033[7;37;34m").replace("§2", "\033[7;37;32m").replace("§3", "\033[7;37;36m").replace("§4", "\033[7;37;31m").replace("§5", "\033[7;37;35m").replace("§6", "\033[7;37;33m").replace("§7", "\033[7;37;90m").replace("§8", "\033[7;37;2m").replace("§9", "\033[7;37;94m").replace("§a", "\033[7;37;92m").replace("§b", "\033[7;37;96m").replace("§c", "\033[7;37;91m").replace("§d", "\033[7;37;95m").replace("§e", "\033[7;37;93m").replace("§f", "\033[7;37;1m").replace("§r", "\033[0m")+"\033[0m "
            textNew = text.split("\n")
            for i in range(len(textNew)):
                if i == 0:
                    if not info.startswith("\033["):
                        textNew[i] = "\033[7m" + info + textNew[i]
                    else:
                        textNew[i] = info + textNew[i]
                else:
                    textColor = getTextColorInTheEnd(textNew[i-1])
                    if not info.startswith("\033["):
                        textNew[i] = textColor.replace("\033[0", "\033[7") + info + textColor + textNew[i]
                    else:
                        textNew[i] = info + textColor + textNew[i]
            text = "\n".join(textNew)
            del textNew
        timeInfo = "[%s] " % datetime.datetime.now().strftime("%H:%M:%S")
        text = timeInfo + text.replace("\n", "\n" + timeInfo)
        if output:
            if replace:
                text = "\r"+text+" "*(lastOutputLen-(len(removeColorInText(text))+(len(removeColorInText(text).encode())-len(removeColorInText(text)))//2))
                end = ""
                lastReplace = True
            else:
                if lastReplace:
                    if lastReplaceByNext:
                        text = "\r"+text+" "*(lastOutputLen-(len(removeColorInText(text))+(len(removeColorInText(text).encode())-len(removeColorInText(text)))//2))
                    else:
                        text = "\n"+text
                    lastReplace = False
            if replaceByNext:
                lastReplaceByNext = True
            else:
                lastReplaceByNext = False
            print_Py(text, end = end,flush=True)
            l = removeColorInText(text).replace("\r", "").split("\n")[-1]
            if l:
                while l[-1] == " ":
                    l = l[:-1]
            lastOutputLen = len(l)+(len(l.encode())-len(l))//2
        else:
            return text
    print = color

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
            color("%s: %.2fs" % (msg, delay), replace = True, replaceByNext = True, info = "§e 等待 ")
            time.sleep(0.01)


    def exitChatbarMenu(killFB: bool = True, delay: int | float = 3, reason: str = None, force = False) -> None:
        """
        退出命令系统的函数

        参数:
            killFB: bool -> 是否同时关闭FastBuilder
            delay: int | float -> 倒计时时间(秒)
            reason: str -> 退出时显示的说明
        返回: 无返回值
        """
        global exiting, exitDelay, exitReason
        if force:
            try:
                FBkill()
            except:
                pass
            finally:
                color("§e正在清空globals变量.", info = "§e 加载 ")
                globals().clear()
        exitDelay = delay
        exitReason = reason
        exiting = True
        raise SystemExit(0)


    try:
        import os
        pid = os.getpid()
        os.system("echo DotCS 正在运行, 其进程 pid 为 %d." % pid)
        # Python 自带库.
        import traceback, socket, datetime, time, json, random, sys, urllib, urllib.parse, platform, sqlite3, threading, struct, hashlib, shutil, base64, ctypes, collections, types, itertools, _thread as thread
        from typing import Union, List, Dict, Tuple, Set
        # pip 可下载到的库.
        # pip freeze>modules.txt
        # pip uninstall -r modules.txt -y
        # pip install psutil requests pymysql qrcode websocket-client brotli pillow rich numpy pyinstaller==4.9 mido
        import psutil, requests, pymysql, qrcode, websocket, brotli, PIL, rich.console
        # 第三方库.
        PyPIthird = [
            {"name": "bdx_work_shop", "author": "2401PT, SuperScript", "link": "https://github.com/CMA2401PT/BDXWorkShop"},
            {"name": "FastBuilder connector", "author": "2401PT", "link": "https://github.com/CMA2401PT/FastBuilder"},
            {"name": "TDES encrypt", "author": "7912", "link": "None"},
            {"name": "Space Rectangular Coordinate System", "author": "7912", "link": "None"}
        ]
        for i in PyPIthird:
            color("DotCS 使用了 §e%s§r 库, 其作者是 §e%s§r, 链接: %s" % (i["name"], i["author"], i["link"]), info = " 信息 ")
        import bdx_work_shop.canvas
        import bdx_work_shop.artists.cmd_midi_music
        from proxy import conn
        from PyPI.SpaceRectangularCoordinateSystem import Point, Line, Cube

        platformVer = str(platform.platform())
        if "Windows" in platformVer:
            platformVer = "Windows"
            outputTime = "long"
        else:
            platformVer = "Linux"
            outputTime = "short"
        # console = rich.console.Console()
        # color("控制台窗口大小: %dx%d" % (console.height, console.width), info = " 信息 ")
        # if console.width < 115:
        #     color("§e控制台窗口宽度应大于 115, 请调整.", info = "§e 警告 ")
        # while console.width < 115:
        #     color("§e当前宽度: %d" % console.width, replace = True, info = "§e 警告 ")
        #     time.sleep(0.01)

    except Exception as err:
        color("§c导入Python库失败, 信息:\n"+str(err), info = "§c 错误 ")
        color("§c"+traceback.format_exc(), info = "§c 错误 ")
        exitChatbarMenu(False, 5)


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


    def FBkill() -> None:
        """
        关闭FastBuilder的函数
        """
        for proc in psutil.process_iter():
            try:
                if "phoenixbuilder" in proc.name():
                    if strInList(server, proc.cmdline()):
                        proc.kill()
                        color("§6已终止 FastBuilder ,其 pid 为 %d" % proc.pid, info = "§6  FB  ")
            except:
                pass

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


    def setGlobalVar(key, value):
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
            color("§c下载失败, 原因: 文件未找到.", info = "§c 错误 ")
            return {"status": "fail", "reason": "file not found"}
        fileDownloadedSize = 0
        fileSize = int(response.headers['content-length'])
        if response.status_code == 200:
            color("§e开始下载, 文件大小: %s" % Byte2KB(fileSize), info = "§e 下载 ")
            timeDownloadStart = time.time()
            fileDownloadedLastSize = 0
            speedDownloadCurrent = 0
            timeRem = "--:--:--"
            with open(path, 'wb') as file:
                try:
                    for data in response.iter_content(chunk_size = freshSize):
                        if exiting:
                            color("§c下载失败, 原因: 命令系统退出", info = "§c 错误 ")
                            return {"status": "fail", "reason": "exit"}
                        file.write(data)
                        fileDownloadedSize += len(data)
                        if time.time()-timeDownloadStart >= 0.5:
                            speedDownloadCurrent = (fileDownloadedSize-fileDownloadedLastSize)/(time.time()-timeDownloadStart)
                            timeDownloadStart = time.time()
                            fileDownloadedLastSize = fileDownloadedSize
                            if speedDownloadCurrent != 0:
                                timeRem = second2minsec((fileSize-fileDownloadedSize)/speedDownloadCurrent)
                        color("§e正在下载: %.2f%%, %s / %s, %s/s, 预计还需 %s" % (fileDownloadedSize/fileSize*100, Byte2KB(fileDownloadedSize), Byte2KB(fileSize), Byte2KB(speedDownloadCurrent), timeRem), replace = True, info = "§e 下载 ")
                except Exception as err:
                    color("§c下载失败, 原因: 连接超时", info = "§c 错误 ")
                    return {"status": "fail", "reason": "timed out"}
            color("§a下载完成", info = "§a 成功 ")
            return {"status": "success"}
        else:
            color("§c下载失败, 原因: 状态码 %s" % response.status_code, info = "§c 错误 ")
            return {"status": "fail", "reason": "server rejected", "status_code": response.status_code}


    def updateCheck() -> None:
        """
        检测命令系统更新的函数, 若有更新则自动下载
        你不应该使用此函数, 命令系统会在启动时运行一次, 启动成功后每60s运行一次
        """
        if not(connected):
            color("§e正在检查更新, 当前版本: %s" % version, info = "§e 信息 ")
        try:
            status = requests.get("http://www.dotcs.community/status.txt", timeout = 10)
            status = status.text.split("\r\n")
            newversion = status[0].split("version: ")[1]
            allow = status[1].split("allow: ")[1]
        except:
            color("§c检测更新失败, 跳过检测.", info = "§c 错误 ")
            newversion = version
            allow = "true"
        if newversion != version:
            if platformVer == "Windows":
                color("§e最新版本: %s, 正在下载." % newversion, info = "§e 信息 ")
                if fileDownload("http://www.dotcs.community/robot.exe", "robotNew.exe", 5)["status"] == "success":
                    if os.path.isfile("robotOld.exe"):
                        os.remove("robotOld.exe")
                    if os.path.isfile("robot.exe"):
                        shutil.move("robot.exe", "robotOld.exe")
                    shutil.move("robotNew.exe", "robot.exe")
                    color("§a更新下载完成, 正在重启.", info = "§a 成功 ")
                    exitChatbarMenu(reason = "Auto updating")
                else:
                    if os.path.isfile("robotNew.exe"):
                        os.remove("robotNew.exe")
                    exitChatbarMenu(reason = "Download failed")
            else:
                pass
        else:
            if not(connected):
                color("§a你正在使用最新版本.", info = "§a 信息 ")
        if allow == "false":
            reason = status[2].split("msg: ")[1].replace(r"\n", "\n")
            color("§c%s" % reason, info = "§c 禁止 ")
            if not(connected):
                exitChatbarMenu(killFB = False)
            else:
                exitChatbarMenu()


    sendtogroup = ""
    QQgroup = ""
    def NekoMaidMsg(msg, msgIndex, connToSend, isLastFormat = False): pass
    def log(text: str, filename: str = None, mode: str = "a", encoding: str = "utf-8", errors: str = "ignore", output: bool = True, sendtogamewithRitBlk: bool = False, sendtogamewithERROR: bool = False, sendtogrp: bool = False, info = " 信息 ") -> None:
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
            os.makedirs("serverMsg",exist_ok=True)
            filename = os.path.join("serverMsg",datetime.datetime.now().strftime("%Y-%m-%d.txt"))
        if text[-1:] == "\n":
            text = text[:-1]
        if output:
            color(text+"\033[0m", info = info)
        try:
            with open(filename, mode, encoding = encoding, errors = errors) as file:
                file.write("["+datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+"] "+text+"\n")
        except Exception as err:
            color("写入日志错误, 信息:\n"+str(err), info = "§c 错误 ")
        if sendtogamewithRitBlk and connected:
            tellrawText("@a", "§l§6Ritle§aBlock§r", text = text)
        if sendtogamewithERROR and connected:
            tellrawText("@a", "§l§4ERROR§r", text = "§c" + text)
        if sendtogrp:
            try:
                sendtogroup("group", QQgroup, text)
            except Exception as err:
                errmsg = "log()函数中sendtogroup()报错, 信息:\n"+str(err)
                log("§c" + errmsg, info = "§c 错误 ")
        for i in threadList[:]:
            try:
                if i.name == "与NekoMaid网站通信":
                    for j in text.split("\n"):
                        NekoMaidMsg(["NekoMaid:console:log", {"level": "INFO", "logger": "net.minecraft.server.v1_16_R3.DedicatedServer", "msg": "%s§r" % "["+datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+"] "+j.replace("'", 'unchanged'), "time": time.time()*1000}], "42", i.data["conn"], True)
            except:
                pass


    def tellrawText(who: str, dispname: None | str = None, text: str = None) -> None:
        """
        便捷执行tellraw的函数

        参数:
            who: str.MinecraftTargetSelector -> 给谁显示
            dispname: None | str -> 模拟玩家说话格式, 不传则直接tellraw
            text: str -> 要显示的信息
        返回: 无返回值
        """
        if dispname is None:
            sendcmd(r"""/tellraw %s {"rawtext":[{"text":"%s"}]}""" % (who, text.replace('"', '’’').replace("'", '’')))
        else:
            sendcmd(r"""/tellraw %s {"rawtext":[{"text":"<%s> %s"}]}""" % (who, dispname.replace('"', '’’').replace("'", '’'), text.replace('"', '’’').replace("'", '’')))


    def tellrawScore(scoreboardName: str, targetName: str) -> str:
        """
        返回tellraw计分板格式的函数

        参数:
            scoreboardName: str -> 计分板名称
            targetName: str -> 计分板对象
        返回: str -> tellraw计分板格式
        """
        return '{"score":{"name":"%s","objective":"%s"}}' % (targetName, scoreboardName)


    FBlog_old = []

    gameTime = "00:00:00"
    tps = {"1s": 0, "5s": 0, "20s": 0, "1m": 0, "5m": 0, "10m": 0}
    def getGameTimeRepeat(self) -> None:
        global gameTime
        gameTimeTickLast = 0
        timeLastGet = 0
        tpsList = [20] * 1200
        while True:
            try:
                if exiting:
                    return
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
                color("§c"+traceback.format_exc(), info = "§c 错误 ")
                log("§c" + errmsg, sendtogamewithERROR = True, info = "§c 错误 ")
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


    def pluginRepeat(self) -> None:
        """
        命令系统启动后处理repeat类插件的函数
        你不应该使用此函数, 命令系统会自动以新线程运行它
        """
        global msgList
        timeDict = {"1s": {"time": 1, "timeNow": 0}, "10s": {"time": 10, "timeNow": 0}, "1m": {"time": 60, "timeNow": 0}}
        while True:
            if exiting:
                return
            for i in timeDict:
                if timeDict[i]["timeNow"] == 0:
                    timeDict[i]["timeNow"] = timeDict[i]["time"]
                    msgList.append([-100, {"pluginRunType": "repeat %s" % i}, -1])
                timeDict[i]["timeNow"] -= 1
            time.sleep(1)


    def othersRepeat(self) -> None:
        """
        命令系统启动后每60秒运行1次的函数
        你不应该使用此函数, 命令系统会自动以新线程运行它
        """
        global allplayers, FBlog
        while True:
            timeStart = time.time()
            try:
                if connected:
                    updateCheck()
                    allplayers = getTarget('@a[name=!"%s"]' % robotname, timeout = 60)
            except Exception as err:
                pass
            finally:
                while time.time() - timeStart < 60:
                    if exiting:
                        return
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
            color("§c"+traceback.format_exc(), info = "§c 错误 ")
            log("§c" + errmsg, info = "§c 错误 ", sendtogamewithERROR = True)


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


    def getType(sth):
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


    def floatPos2intPos(number: float | str) -> int:
        if type(number) == str:
            number = float(number)
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



    def QRcode(text: str, where: str = "console", who: str | None = None) -> None:
        """
        在控制台或租赁服输出二维码的函数

        参数:
            text: str -> 要转换的信息
            where: "console" | "server" -> 输出地点
                console: 控制台
                server: 租赁服
            who: str.MinecraftTargetSelector -> 如果发到租赁服, 发送的对象
        返回: None
        """
        if where != "console" and where != "chatbar" and where != "actionbar":
            raise Exception("invalid argument")
        if where != "console" and (who is None):
            raise Exception("invalid argument")
        qr = qrcode.QRCode()
        qr.add_data(text)
        qrline = ""
        qrall = ""
        for i in qr.get_matrix():
            for j in i:
                if j == False:
                    qrline += "\033[0;37;7m  " if (where == "console") else "§f▓"
                else:
                    qrline += "\033[0m  " if (where == "console") else "§0▓"
            if where == "console":
                color("%s\033[0m" % qrline)
            elif where == "chatbar":
                tellrawText(who, text = "§l"+qrline)
            qrall += qrline
            qrline = ""
        if where == "actionbar":
            sendcmd("/title %s actionbar %s" % (who, qrall))


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
        global sendcmdResponse
        if cmd[0] == "/":
            cmd = cmd[1:]
        uuid = conn.SendMCCommand(connID, cmd).decode("utf-8")
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
        global sendcmdResponse
        if cmd[0] == "/":
            cmd = cmd[1:]
        uuid = conn.SendWSCommand(connID, cmd).decode("utf-8")
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
            exitChatbarMenu(reason = "You can not use the command 'stop'.")
        conn.SendNoResponseCommand(connID, cmd)

    def sendfbcmd(cmd: str) -> None:
        """
        发送命令到FastBuilder的函数

        参数:
            cmd: str (FastBuilder command) -> FastBuilder执行指令
        返回: 无返回值
        """
        if cmd[0] == "?":
            cmd = cmd[1:]
        conn.SendFBCommand(connID, cmd)


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
    def processPacket(self) -> None:
        """
        处理FastBuilder发送来的包的函数
        你不应该使用此函数, 命令系统会在运行FastBuilder后以新线程启动此函数
        """
        global msgLastRecvTime, XUID2playerName, timeSpentFBRun, msgList, server, connID, robotname, allplayers, connected, savePacket
        try:
            connected = True
            msgList.append([-100, {"pluginRunType": "init"}, -1])
            sendwocmd("changesetting allow-cheats true")
            color('§e正在检测机器人是否能正常执行指令.', info = "§e 加载 ")
            result = sendcmd("/time add 0", True, timeout = 20)["OutputMessages"][0]
            if result["Success"] == False:
                if result["Message"] == "commands.generic.unknown":
                    color("§c执行命令失败: 未知的命令. 有可能是机器人没有op权限.", info = "§c 错误 ")
                if result["Message"] == "commands.generic.disabled":
                    color("§c执行命令失败: 此等级未启用作弊. 有可能是未打开允许作弊.", info = "§c 错误 ")
                else:
                    color("§c执行命令失败: %s." % result["Message"], info = "§c 错误 ")
                raise Exception("Can not execute operator commands.")

            sendcmd("/gamemode c")
            sendcmd("/effect @s resistance 999999 19 true")
            sendcmd("/effect @s invisibility 999999 0 true")

            color("§e正在获取机器人游戏名和在线玩家.", info = "§e 加载 ")
            robotname = getTarget("@s", timeout = 20)[0]
            if ")" in robotname:
                color("§cFastBuilder 机器人游戏名异常.", info = "§c 错误 ")
                exitChatbarMenu(reason = "Invalid FastBuilder robot name.")
            if robotname not in adminhigh:
                adminhigh.append(robotname)
            allplayers = getTarget("@a", timeout = 20)

            color("§e正在检测在线玩家的游戏名中是否包含违禁词.", info = "§e 加载 ")
            for i in allplayers[:]:
                color("§e正在检测: %s" % i, replace = True, replaceByNext = True, info = "§e 加载 ")
                hasPWord = False
                if getPlayerData("prohibitedWord", i, "False") == "False":
                    if prohibitedWordTest(i):
                        hasPWord = True
                        setPlayerData("prohibitedWord", i, "True")
                else:
                    hasPWord = True
                if hasPWord:
                    color("§c玩家 %s 的游戏名中包含违禁词, 正在踢出." % i, info = "§c 警告 ")
                    sendwocmd('/kick "%s" §c您的名称内有违禁词, 无法进服.' % i)
                    allplayers.remove(i)

            color("§e正在获取在线玩家的XUID.", info = "§e 加载 ")
            for i in allplayers:
                color("§e正在获取: %s" % i, replace = True, replaceByNext = True, info = "§e 加载 ")
                result = sendcmd('/querytarget @a[name="%s"]' % i, True, timeout = 20)["OutputMessages"][0]
                if result["Success"] == False:
                    raise Exception("Failed to get the XUID.")
                XUID2playerName[json.loads(result["Parameters"][0])[0]["uniqueId"][-8:]] = i
            for i in allplayers:
                color("§e正在验证: %s" % i, replace = True, replaceByNext = True, info = "§e 加载 ")
                if i not in list(XUID2playerName.values()):
                    raise Exception("Failed to get the XUID.")
            allplayers.remove(robotname)
            savePacket = True

            createThread("获取租赁服游戏时间并计算tps", data = {}, func = getGameTimeRepeat)
            createThread("执行repeat类插件", data = {}, func = pluginRepeat)

            timeSpentRun = float(time.time()-timeStartRun)
            timeSpentDotCSRun = timeSpentRun-timeSpentFBRun
            color("§a成功启动 DotCS 社区版, 用时: %.2fs. (DotCS: %.2fs, FB: %.2fs)" % (timeSpentRun, timeSpentDotCSRun, timeSpentFBRun), info = "§a 成功 ")
            tellrawText("@a", "§l§6System§r", '§6".命令"系统成功启动.')
            tellrawText("@a", "§l§6System§r", "§6共加载 §l%d§r§6 个插件/函数." % len(pluginList))
            sendcmd("/time add 0")
            sendcmd("/kill @e[type=xp_orb]")
            sendcmd("/gamemode c")
            sendcmd("/effect @s resistance 999999 19 true")
            sendcmd("/effect @s invisibility 999999 0 true")
            sendcmd("/tp @s 100000 100000 100000")
            if not faststart:
                color("在控制台输入'faststart'可进入快速启动模式", info = " 提示 ")

            log("§6FastBuilder 机器人名: %s" % robotname, info = "§6  FB  ")
            log("§e当前在线玩家: "+(", ".join(allplayers)), info = "§e 信息 ")

            while True:
                if exiting:
                    return
                if msgList == []:
                    if time.time()-msgLastRecvTime >= 45:
                        log("§c45秒未收到包", info = "§c 错误 ")
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
                                log("§c玩家 %s 的游戏名中包含违禁词, 正在踢出." % playername, info = "§c 警告 ")
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
                        for pluginType in ["packet -1", "packet %d" % packetType, pluginRunType]:
                            try:
                                if pluginType in plugin.pluginCode:
                                    exec(plugin.pluginCode[pluginType])
                            except PluginSkip: # 感谢SuperScript提供的建议.
                                pass
                            except Exception as err:
                                errmsg = "插件 %s %s 报错, 信息:\n%s" % (plugin.pluginName, pluginRunType, str(err))

                                # 更好地输出错误信息.
                                console.print_exception(width = int(console.width*0.9))
                                # color("§c"+traceback.format_exc(), info = "§c 错误 ")

                                log("§c" + errmsg, sendtogamewithERROR = True, info = "§c 错误 ")


        except Exception as err:
            errmsg = "信息处理报错, 信息:\n"+str(err)
            color("§c"+traceback.format_exc(), info = "§c 错误 ")
            log("§c" + errmsg, info = "§c 错误 ")
            exitChatbarMenu(reason = "Process packet error.")


    def revPacket(self) -> None:
        """
        连接FastBuilder并接收其发送来的包的函数
        你不应该使用此函数, 命令系统会在运行FastBuilder后以新线程启动此函数
        """
        global msgLastRecvTime, timeSpentFBRun, msgList, connID, timeStartFBRun, FBlog

        # 尝试连接
        color("§e正在连接到 FastBuilder.", info = "§e 加载 ")
        startTime = time.time()
        while True:
            try:
                if exiting:
                    return
                print("%s:%s" % (FBip, FBport))
                connID = conn.ConnectFB("%s:%s" % (FBip, FBport))
                break
            except Exception as e:
                print(e)
                spendTime = time.time()-startTime
                if spendTime >= 60:
                    color("§cFastBuilder超过60秒未连接上租赁服, 正在退出.", info = "§c 错误 ")
                    exitChatbarMenu(reason = "FastBuilder timed out.")
                color("§e正在连接到 FastBuilder, %.2fs" % spendTime, replace = True, replaceByNext = True, info = "§e 加载 ")
                time.sleep(0.01)

        # 连上了
        color("§a成功连接到 FastBuilder.", info = "§a 成功 ")
        timeSpentFBRun = float(time.time()-timeStartFBRun)
        msgRecved = False

        # 开始收取聊天信息
        packetNum = 0
        while True:
            try:
                if exiting:
                    return
                packetNum += 1
                bytesPkt = conn.RecvGamePacket(connID)
                packetType = conn.inspectPacketID(bytesPkt)
                msgLastRecvTime = time.time()
                if not msgRecved:
                    msgRecved = True
                if packetNum == 1:
                    createThread("处理数据包", {}, processPacket)
                # if packetType == 39 or packetType == 40 or packetType == 111 or packetType == 123 or packetType == 58 or packetType == 108 or packetType == 158 or packetType == 67:
                #     continue
                jsonPkt = json.loads(conn.GamePacketBytesAsIsJsonStr(bytesPkt))
                pluginRunType = "packet on another thread %d" % packetType
                if packetType == 79:
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
                            exec(i.pluginCode[pluginRunType])
                    except Exception as err:
                        errmsg = "插件 %s %s 报错, 信息:\n%s" % (i.pluginName, pluginRunType, str(err))
                        color("§c"+traceback.format_exc(), info = "§c 错误 ")
                        log("§c" + errmsg, sendtogamewithERROR = True, info = "§c 错误 ")

            except Exception as err:
                errmsg = "收取数据包报错, 信息:\n"+str(err)
                color("§c"+traceback.format_exc(), info = "§c 错误 ")
                log("§c" + errmsg, info = "§c 错误 ")
                exitChatbarMenu(reason = "Receive packet error.")

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
            self.daemon = True
            self.output = output
            threadList.append(self)
            self.start()

        def run(self):
            try:
                if self.output:
                    color("§e启动线程 %s." % self.name, info = "§e 线程 ")
                if getType(self.func) != "str":
                    self.func(self)
                else:
                    exec("%s(self)" % self.func)
            except Exception as err:
                errmsg = ("线程 %s 报错, 信息:\n" % self.name)+str(err)
                color("§c"+traceback.format_exc(), info = "§c 错误 ")
                log("§c" + errmsg, sendtogamewithERROR = True, info = "§c 错误 ")
            except SystemExit as err:
                pass
                # color("§eThread %s has been terminated forcely." % self.name)
            finally:
                if self.output:
                    color("§e终止线程 %s." % self.name, info = "§e 线程 ")
                threadList.remove(self)

        def get_id(self):
            if hasattr(self, '_thread_id'):
                return self._thread_id
            for id, thread in threading._active.items():
                if thread is self:
                    return id

        def stop(self):
            self.stopping = True
            # color("§eTerminating thread %s." % self.name)
            thread_id = self.get_id()
            res = ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, ctypes.py_object(SystemExit))
            if res > 1:
                ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, 0)
                color("§c终止线程失败", info = "§c 错误 ")


    pluginList = []
    class plugin():
        def __init__(self, pluginName, pluginCode):
            self.pluginName = pluginName
            self.pluginCode = pluginCode
            self.enable = True
            self.globals = globals()
            self.locals = {}
            pluginList.append(self)


    """""""""""""""
      RUNNING PART
    """""""""""""""
    if __name__ == "__main__":
        import sys 
        
        version = "v0.10.9" # 设置版本号
        timeStartRun = time.time() # 记录启动时间
        FBip = "localhost"
        FBport = sys.argv[1]
        if os.path.isfile("robotOld.exe"):
            os.remove("robotOld.exe")
        if os.path.isfile("robotNew.exe"):
            os.remove("robotNew.exe")
        faststart = getStatus("faststart")
        if not faststart:
            countdown(0.1, "§e命令系统即将开始启动")

        # color(title4)
        color('§b".命令"系统社区版 - 租赁服聊天栏菜单\n".Dot" Command System Community(DotCS)\nDotCS基于FastBuilder.\n社区版作者: 7912\n其官方插件作者: 7912, Pomelo', info = "§b 信息 ")
        color('§b用户交流群: 833303126', info = "§b 信息 ")
        color("FastBuilder 连接地址: %s:%s" % (FBip, FBport), info = " 信息 ")

        # 如果租赁服号未设置, 则请求输入租赁服号并存入server.txt
        print(os.getcwd())
        color("§e正在读取租赁服配置信息.", info = "§e 加载 ")
        if not os.path.isfile("server.txt"):
            json.dump({"code": "0", "password": "0"}, open("server.txt", "w", encoding = "utf-8"), indent = 4, ensure_ascii = True, sort_keys = True)
        serverConfig = json.load(open("server.txt", "r", encoding = "utf-8"))
        try:
            server, serverPassword = str(serverConfig["code"]), str(serverConfig["password"])
        except:
            json.dump({"code": "0", "password": "0"}, open("server.txt", "w", encoding = "utf-8"), indent = 4, ensure_ascii = True, sort_keys = True)
            server, serverPassword = "0", "0"
        json.dump({"code": server, "password": serverPassword}, open("server.txt", "w", encoding = "utf-8"), indent = 4, ensure_ascii = True, sort_keys = True)
        if server == "0":
            # server = input("Please input your server code: ")
            sever="01234567"
            json.dump({"code": server, "password": serverPassword}, open("server.txt", "w", encoding = "utf-8"), indent = 4, ensure_ascii = True, sort_keys = True)
        if serverPassword == "0":
            # serverPassword = input("Please input your server password: ")
            serverPassword="01234567"
            if not serverPassword:
                serverPassword = "7912"
            json.dump({"code": server, "password": serverPassword}, open("server.txt", "w", encoding = "utf-8"), indent = 4, ensure_ascii = True, sort_keys = True)

        FBkill()

        # 加载插件
        if "获取玩家手持物品.py" in os.listdir("plugin"):
            os.remove("plugin/获取玩家手持物品.py")
        if getStatus("pluginupdate1") != "update":
            fileDownload("http://www.dotcs.community/update/获取玩家手持物品或装备.py", "plugin/获取玩家手持物品或装备.py")
            setStatus("pluginupdate1", "update")

        color("§e正在加载插件.", info = "§e 加载 ")
        color("§e[总进度 0/2] 初始化.", info = "§e 加载 ")
        if os.path.isdir("plugin/data/temp"):
            shutil.rmtree("plugin/data/temp")
        os.makedirs("plugin/data/temp",exist_ok=True)
        color("§e[总进度 1/2] 正在读取插件.", info = "§e 加载 ")
        pluginlist = []
        for filename in os.listdir("plugin"):
            if filename.endswith(".py") or filename.endswith(".py.enc"):
                pluginlist.append(filename)

        for i in range(len(pluginlist)):
            filename = pluginlist[i]
            color("§e[总进度 1/2][插件 %d/%d] 加载插件: %s" % (i+1, len(pluginlist), filename), replace = True, replaceByNext = True, info = "§e 加载 ")
            with open("plugin/"+filename, "rb") as file:
                pluginCode = file.read()
                pluginCodeList = pluginCode.decode("utf-8").replace("\r", "").split("# PLUGIN TYPE: ")[1:]
                pluginCodeDict = {}
                for i in pluginCodeList:
                    pluginType = i.split("\n", 1)[0]
                    pluginCode = i.split("\n", 1)[1]
                    filenameTemp = "plugin/data/temp/%s_%s" % (filename, pluginType)
                    pluginCodeDict[pluginType] = compile(pluginCode, filename = filenameTemp, mode = "exec")
                    with open(filenameTemp, "w", encoding = "utf-8") as file:
                        file.write(pluginCode)
                plugin(filename, pluginCodeDict)
        del pluginlist, pluginCode, pluginCodeList, pluginCodeDict, i

        color("§e[总进度 2/2] 正在执行 def 类型插件.", info = "§e 加载 ")
        pluginRunType = "def"
        pluginIndex = 0
        for i in pluginList:
            pluginIndex += 1
            color("§e[总进度 2/2][插件 %d/%d] 执行插件: %s" % (pluginIndex, len(pluginList), i.pluginName), replace = True, replaceByNext = True, info = "§e 加载 ")
            try:
                if i.enable and pluginRunType in i.pluginCode:
                    exec(i.pluginCode[pluginRunType])
            except Exception as err:
                errmsg = "插件 %s %s 报错, 信息:\n%s" % (i.pluginName, pluginRunType, str(err))
                color("§c"+traceback.format_exc(), info = "§c 错误 ")
                log("§c" + errmsg, sendtogamewithERROR = True, info = "§c 错误 ")
                exitChatbarMenu(delay = 60, reason = "Load plugin %s %s error in step 2." % (i.pluginName, pluginRunType))
        color("§a成功加载所有插件.", info = "§a 成功 ")

        # 启动FastBuilder并等待连接.
        timeStartFBRun = time.time()
        color("§e正在等待 FastBuilder 连接到租赁服 %s." % server, info = "§e 加载 ")
        createThread("收取数据包", data = {}, func = revPacket)
        createThread("检测命令系统更新并校准在线玩家", data = {}, func = othersRepeat)

        while not exiting:
            time.sleep(0.1)

        sys.exit()


except:
    try:
        if not connected:
            color("§c"+traceback.format_exc(), info = "§c 错误 ")
        if exitReason is None:
            color("§e正在退出, 请稍等.", info = "§e 退出 ")
        else:
            color("§e正在退出, 原因: %s" % str(exitReason), info = "§e 退出 ")
        color("§e正在终止子线程.", info = "§e 线程 ")
        startTime = time.time()
        while threadList and time.time() - startTime < 10:
            for i in threadList[:]:
                i.stop()
            time.sleep(1)
        if connected:
            conn.ReleaseConnByID(connID)
            time.sleep(0.5)
        if exitDelay != 0:
            countdown(exitDelay, "§e正在退出")
    except:
        pass
    finally:
        try:
            FBkill()
        except:
            pass
        threadNum = len(threadList)
        if threadNum >= 1:
            color("§c强制退出命令系统, %d 个线程还未被终止:" % threadNum, info = "§c 错误 ")
            for i in range(len(threadList)):
                color("§c%d. %s" % (i+1, threadList[i].name), info = "§c 错误 ")
        elif threadNum == 0:
            color("§a正常退出.", info = "§a 信息 ")
