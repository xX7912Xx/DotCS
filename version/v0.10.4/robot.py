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
print("\n"*30 + "Code: http://www.dotcs.community/code/version/")
threadList = []
exiting = False
exitDelay = 3
exitReason = None
connected = False
try:

    """""""""
    DEF PART
    """""""""
    lastOutputLen = 0
    lastReplace = False
    lastReplaceByNext = False
    def color(text: str, output: bool = True, end: str = "\n", replace: bool = False, replaceByNext: bool = False) -> str:
        """
        在控制台输出彩色文本的函数

        参数:
            text: str -> 要输出的信息
            output: bool -> 是否在控制台输出
            end: str -> 输出时末尾的字符, 同print()
            replace: bool -> 是否以不能被下次输出替换, 但能被下次replace = True的输出替换的形式输出, 即在开头和末尾加上\r
            replaceByNext: bool -> 是否以能被下次输出替换的形式输出, 即在开头和末尾加上\r
        返回: str -> 输出
        """
        global lastOutputLen, lastReplace, lastReplaceByNext
        if text[-1] == "\n" and "Traceback" in text:
            text = text[:-1]
        if "报错, 信息:" in text:
            text = "§4"+text
        text = text.replace("§1", "\033[0;37;34m").replace("§2", "\033[0;37;32m").replace("§3", "\033[0;37;36m").replace("§4", "\033[0;37;31m").replace("§5", "\033[0;37;35m").replace("§6", "\033[0;37;33m").replace("§7", "\033[0;37;90m").replace("§8", "\033[0;37;2m").replace("§9", "\033[0;37;94m").replace("§a", "\033[0;37;92m").replace("§b", "\033[0;37;96m").replace("§c", "\033[0;37;91m").replace("§d", "\033[0;37;95m").replace("§e", "\033[0;37;93m").replace("§f", "\033[0;37;1m").replace("§r", "\033[0m")+"\033[0m"
        if output:
            if replace:
                text = "\r"+text+" "*(lastOutputLen-(len(text.replace("\033[0;37;34m", "").replace("\033[0;37;32m", "").replace("\033[0;37;36m", "").replace("\033[0;37;31m", "").replace("\033[0;37;35m", "").replace("\033[0;37;33m", "").replace("\033[0;37;90m", "").replace("\033[0;37;2m", "").replace("\033[0;37;94m", "").replace("\033[0;37;92m", "").replace("\033[0;37;96m", "").replace("\033[0;37;91m", "").replace("\033[0;37;95m", "").replace("\033[0;37;93m", "").replace("\033[0;37;1m", "").replace("\033[0m", ""))+(len(text.replace("\033[0;37;34m", "").replace("\033[0;37;32m", "").replace("\033[0;37;36m", "").replace("\033[0;37;31m", "").replace("\033[0;37;35m", "").replace("\033[0;37;33m", "").replace("\033[0;37;90m", "").replace("\033[0;37;2m", "").replace("\033[0;37;94m", "").replace("\033[0;37;92m", "").replace("\033[0;37;96m", "").replace("\033[0;37;91m", "").replace("\033[0;37;95m", "").replace("\033[0;37;93m", "").replace("\033[0;37;1m", "").replace("\033[0m", "").encode())-len(text.replace("\033[0;37;34m", "").replace("\033[0;37;32m", "").replace("\033[0;37;36m", "").replace("\033[0;37;31m", "").replace("\033[0;37;35m", "").replace("\033[0;37;33m", "").replace("\033[0;37;90m", "").replace("\033[0;37;2m", "").replace("\033[0;37;94m", "").replace("\033[0;37;92m", "").replace("\033[0;37;96m", "").replace("\033[0;37;91m", "").replace("\033[0;37;95m", "").replace("\033[0;37;93m", "").replace("\033[0;37;1m", "").replace("\033[0m", "")))//2))
                end = ""
                lastReplace = True
            else:
                if lastReplace:
                    if lastReplaceByNext:
                        text = "\r"+text+" "*(lastOutputLen-(len(text.replace("\033[0;37;34m", "").replace("\033[0;37;32m", "").replace("\033[0;37;36m", "").replace("\033[0;37;31m", "").replace("\033[0;37;35m", "").replace("\033[0;37;33m", "").replace("\033[0;37;90m", "").replace("\033[0;37;2m", "").replace("\033[0;37;94m", "").replace("\033[0;37;92m", "").replace("\033[0;37;96m", "").replace("\033[0;37;91m", "").replace("\033[0;37;95m", "").replace("\033[0;37;93m", "").replace("\033[0;37;1m", "").replace("\033[0m", ""))+(len(text.replace("\033[0;37;34m", "").replace("\033[0;37;32m", "").replace("\033[0;37;36m", "").replace("\033[0;37;31m", "").replace("\033[0;37;35m", "").replace("\033[0;37;33m", "").replace("\033[0;37;90m", "").replace("\033[0;37;2m", "").replace("\033[0;37;94m", "").replace("\033[0;37;92m", "").replace("\033[0;37;96m", "").replace("\033[0;37;91m", "").replace("\033[0;37;95m", "").replace("\033[0;37;93m", "").replace("\033[0;37;1m", "").replace("\033[0m", "").encode())-len(text.replace("\033[0;37;34m", "").replace("\033[0;37;32m", "").replace("\033[0;37;36m", "").replace("\033[0;37;31m", "").replace("\033[0;37;35m", "").replace("\033[0;37;33m", "").replace("\033[0;37;90m", "").replace("\033[0;37;2m", "").replace("\033[0;37;94m", "").replace("\033[0;37;92m", "").replace("\033[0;37;96m", "").replace("\033[0;37;91m", "").replace("\033[0;37;95m", "").replace("\033[0;37;93m", "").replace("\033[0;37;1m", "").replace("\033[0m", "")))//2))
                    else:
                        text = "\n"+text
                    lastReplace = False
            if replaceByNext:
                lastReplaceByNext = True
            else:
                lastReplaceByNext = False
            print(text, end = end)
            l = text.replace("\r", "").replace("\033[0;37;34m", "").replace("\033[0;37;32m", "").replace("\033[0;37;36m", "").replace("\033[0;37;31m", "").replace("\033[0;37;35m", "").replace("\033[0;37;33m", "").replace("\033[0;37;90m", "").replace("\033[0;37;2m", "").replace("\033[0;37;94m", "").replace("\033[0;37;92m", "").replace("\033[0;37;96m", "").replace("\033[0;37;91m", "").replace("\033[0;37;95m", "").replace("\033[0;37;93m", "").replace("\033[0;37;1m", "").replace("\033[0m", "").split("\n")[-1]
            if l:
                while l[-1] == " ":
                    l = l[:-1]
            lastOutputLen = len(l)+(len(l.encode())-len(l))//2
        else:
            return text


    paid = False
    def countdown(delay: int | float, msg: str = None, untilPaid = False) -> None:
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
            if untilPaid:
                if paid:
                    break
            delay = delayStop-time.time()
            color("%s: %.2fs" % (msg, delay), replace = True, replaceByNext = True)
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
                color("§eCleaning global varibles.")
                globals().clear()
        exitDelay = delay
        exitReason = reason
        exiting = True
        raise SystemExit(0)


    try:
        import os
        pid = os.getpid()
        os.system("echo DotCS is running, the pid of DotCS is %d." % pid)
        # Python 自带库.
        import traceback, socket, datetime, time, json, random, sys, urllib, urllib.parse, platform, sqlite3, threading, struct, hashlib, shutil, base64, ctypes, collections, types, itertools, _thread as thread
        # pip 可下载到的库.
        # pip freeze>modules.txt
        # pip uninstall -r modules.txt -y
        # pip install psutil requests pymysql qrcode websocket-client brotli pillow rich numpy pyinstaller==4.9 mido pycryptodome
        import psutil, requests, pymysql, qrcode, websocket, brotli, PIL, rich.console, Crypto.Cipher.DES3
        # 第三方库.
        PyPiThird = [
            {"name": "bdx_work_shop", "author": "2401PT, SuperScript", "link": "https://github.com/CMA2401PT/BDXWorkShop"}, 
            {"name": "FastBuilder connector", "author": "2401PT", "link": "https://github.com/CMA2401PT/FastBuilder"},
            {"name": "TDES encrypt", "author": "7912", "link": "None"}
        ]
        for i in PyPiThird:
            color("DotCS uses a PyPi named §e%s§r by §e%s§r, link: %s" % (i["name"], i["author"], i["link"]))
        import bdx_work_shop.canvas
        import bdx_work_shop.artists.cmd_midi_music
        from proxy import conn
        from PyPI import TDES
        from PyPI import getVarSize

        platformVer = str(platform.platform())
        if "Windows" in platformVer:
            platformVer = "Windows"
            outputTime = "long"
        else:
            platformVer = "Linux"
            outputTime = "short"
        console = rich.console.Console()
        color("Your console size: %dx%d" % (console.height, console.width))
        if console.width < 115:
            color("§4Console width must bigger than 115, please change it.")
        while console.width < 115:
            color("§eNow: %d" % console.width, replace = True)
            time.sleep(0.01)

    except Exception as err:
        color("§4导入Python库失败, 信息:\n"+str(err))
        color("§c"+traceback.format_exc())
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
                        color("§6Killed FastBuilder thread, pid is %d" % proc.pid)
            except:
                pass


    def runFB(killFB: bool = True) -> None:
        """
        启动FastBuilder的函数

        参数:
            killFB: bool -> 启动前是否关闭FastBuilder
        返回: 无返回值
        """
        global platformVer, FBport
        if FBip == "localhost" or FBip == "127.0.0.1":
            color("Running FastBuilder program.")
            if killFB:
                FBkill()
            if os.path.isfile("nohup.out"):
                try:
                    os.remove("nohup.out")
                    open("nohup.out", "w").write("")
                except:
                    pass
            while is_port_used(FBport):
                color("§ePort %d is used, changing." % FBport)
                FBport += 1
            if platformVer == "Windows":
                os.system('mshta vbscript:createobject("wscript.shell").run("""cmd.exe""/C phoenixbuilder.exe -t fbtoken --code %d --password %d --listen-external 0.0.0.0:%d --no-readline --no-update-check>nohup.out",0)(window.close)' % (server, serverPassword, FBport))
            else:
                os.system("nohup ./phoenixbuilder -t fbtoken --code %d --password %d --listen-external 0.0.0.0:%d --no-readline --no-update-check &" % (server, serverPassword, FBport))


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
            color("§4Failed to download, reason: file not found")
            return {"status": "fail", "reason": "file not found"}
        fileDownloadedSize = 0
        fileSize = int(response.headers['content-length'])
        if response.status_code == 200:
            color("§eStarting download, file size: %s" % Byte2KB(fileSize))
            timeDownloadStart = time.time()
            fileDownloadedLastSize = 0
            speedDownloadCurrent = 0
            with open(path, 'wb') as file:
                try:
                    for data in response.iter_content(chunk_size = freshSize):
                        file.write(data)
                        fileDownloadedSize += len(data)
                        if time.time()-timeDownloadStart >= 0.5:
                            speedDownloadCurrent = (fileDownloadedSize-fileDownloadedLastSize)/(time.time()-timeDownloadStart)
                            timeDownloadStart = time.time()
                            fileDownloadedLastSize = fileDownloadedSize
                        color("§eDownloading: %.2f%%, %s / %s, %s/s" % (fileDownloadedSize/fileSize*100, Byte2KB(fileDownloadedSize), Byte2KB(fileSize), Byte2KB(speedDownloadCurrent)), replace = True)
                except Exception as err:
                    color("§4Failed to download, reason: timed out")
                    return {"status": "fail", "reason": "timed out"}
            color("§aFinished download")
            return {"status": "success"}
        else:
            color("§4Failed to download, reason: status code is %s" % response.status_code)
            return {"status": "fail", "reason": "server rejected", "status_code": response.status_code}


    def updateCheck() -> None:
        """
        检测命令系统更新的函数, 若有更新则自动下载
        你不应该使用此函数, 命令系统会在启动时运行一次, 启动成功后每60s运行一次
        """
        if not(connected):
            color("§eChecking updates. Your version: %s" % version)
        try:
            status = requests.get("http://www.dotcs.community/status.txt", timeout=5)
            status = status.text.split("\r\n")
            newversion = status[0].split("version: ")[1]
            allow = status[1].split("allow: ")[1]
        except:
            color("§4检测更新失败, 跳过检测.")
            newversion = version
            allow = "true"
        if newversion != version:
            if platformVer == "Windows":
                color("§eLatest version: %s, downloading." % newversion)
                if fileDownload("http://www.dotcs.community/robot.exe", "robotNew.exe")["status"] == "success":
                    if os.path.isfile("robotOld.exe"):
                        os.remove("robotOld.exe")
                    if os.path.isfile("robot.exe"):
                        shutil.move("robot.exe", "robotOld.exe")
                    shutil.move("robotNew.exe", "robot.exe")
                    color("§aFinished, restarting.")
                    exitChatbarMenu(reason = "Auto updating")
                else:
                    if os.path.isfile("robotNew.exe"):
                        os.remove("robotNew.exe")
                    exitChatbarMenu(reason = "Download failed")
            else:
                pass
        else:
            if not(connected):
                color("§aYou are running the latest version.")
        if allow == "false":
            reason = status[2].split("msg: ")[1].replace(r"\n", "\n")
            color("§4%s" % reason)
            if not(connected):
                exitChatbarMenu(killFB = False)
            else:
                exitChatbarMenu()


    def blackListCheck() -> None:
        """
        检测你的租赁服号有没有被命令系统封禁, 若封禁则退出
        你不应该使用此函数, 命令系统会在启动时运行一次, 启动成功后每60s运行一次
        """
        if not(connected):
            color('§eChecking whether your server number is blocked by ".Dot" Command System - Netease Minecraft Server Chatbar Menu,\nYour server number: %s\nLocal time: %s' % (server, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        timeGetStart = time.time()
        try:
            result = requests.get("http://www.dotcs.community:7913/api?action=serverNumberBanSearch&serverNumber=%s" % server, timeout = 5).json()
            timeGetSpent = float(time.time()-timeGetStart)*1000
            if not(connected):
                color('§eServer time: %s' % result["time"])
                color('§eYour IP: %s' % result["ip"])
        except Exception as err:
            color("§4检测封禁失败, 跳过检测, 原因: "+str(err))
            result = {"status": "success", "ban": "no"}
            timeGetSpent = 9999999.99
        if result["status"] == "success":
            if result["ban"] == "yes":
                color('§4Your server number is blocked by ".Dot" Command System - Netease Minecraft Server Chatbar Menu, exiting.')
                color('§4你已被 ".命令"系统 官方封禁, 详情请询问7912或art,\n原因: %s' % result["reason"])
                exitChatbarMenu(killFB = False, delay = 60)
            elif result["ban"] == "no":
                if not(connected):
                    color("§aPassed, %.2fms" % timeGetSpent)
        else:
            color("§4检测封禁失败, 跳过检测, 原因: 命令系统服务器发生错误.")


    sendtogroup = ""
    QQgroup = ""
    def NekoMaidMsg(msg, msgIndex, connToSend, isLastFormat = False): pass
    def log(text: str, filename: str = None, mode: str = "a", encoding: str = "utf-8", errors: str = "ignore", output: bool = True, sendtogamewithRitBlk: bool = False, sendtogamewithERROR: bool = False, sendtogrp: bool = False) -> None:
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
        if output:
            if outputTime == "long":
                color("["+datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+"] "+text.replace("\n", "\n"+"["+datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+"] ")+"\033[0m")
            elif outputTime == "short":
                color("["+datetime.datetime.now().strftime("%H:%M:%S")+"] "+text.replace("\n", "\n"+"["+datetime.datetime.now().strftime("%H:%M:%S")+"] ")+"\033[0m")
            else:
                color(text+"\033[0m")
        try:
            with open(filename, mode, encoding = encoding, errors = errors) as file:
                file.write("["+datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+"] "+text+"\n")
        except Exception as err:
            color("写入日志错误, 信息:\n"+str(err))
        if sendtogamewithRitBlk and connected:
            tellrawText("@a", "§l§6Ritle§aBlock§r", text = text)
        if sendtogamewithERROR and connected:
            tellrawText("@a", "§l§4ERROR§r", text = "§c" + text)
        if sendtogrp:
            try:
                sendtogroup("group", QQgroup, text)
            except Exception as err:
                errmsg = "log()函数中sendtogroup()报错, 信息:\n"+str(err)
                log(errmsg)
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
    def FBlogRead() -> str:
        """
        读取FastBuilder日志的函数
        你不应该使用此函数, 命令系统会每秒运行1次此函数
        """
        if FBip == "localhost" or FBip == "127.0.0.1":
            global FBlog_old
            try:
                with open("nohup.out", "r", encoding = "utf-8") as file:
                    FBlog = file.readlines()
                    FBlogNew = []
                    for i in range(len(FBlog)):
                        try:
                            FBlog[i] = FBlog[i].replace("\n", "").replace("\r", "")
                        except:
                            pass
                    if FBlog != FBlog_old:
                        for i in FBlog:
                            if i not in FBlog_old:
                                FBlogNew.append(i)
                    if FBlogNew != []:
                        for i in FBlogNew:
                            color("[§6FastBuilder output§r] %s§r" % i)
                        if strInList("ERROR", FBlogNew):
                            if connected:
                                FBkill()
                            else:
                                exitChatbarMenu(reason = "FastBuilder ERROR", delay = 60)
                    FBlog_old = FBlog
                    return FBlog
            except Exception as err:
                if str(err) == "Netease server number error":
                    raise Exception("Netease server number error")
        return False


    gameTimeTick = 0
    gameTime = "00:00:00"
    tps = {"1s": 0, "5s": 0, "20s": 0, "1m": 0, "5m": 0, "10m": 0}
    def getGameTimeRepeat(self) -> None:
        global gameTime, gameTimeTick
        gameTimeTickLast = 0
        timeLastGet = 0
        tpsList = [20] * 1200
        while True:
            try:
                if exiting:
                    return
                timeStart = time.time()
                timeGet = time.time()
                gameTimeTick = (int(sendcmd("/time query daytime", True, 5)["OutputMessages"][0]["Parameters"][0])+6000)%24000
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
                log(errmsg, sendtogamewithERROR = True)
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
                    msgList.append([-100, {"pluginRunType": "repeat %s" % i}])
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
                    allplayers = getTarget("@a[rm=0.001]")
            except Exception as err:
                pass
            finally:
                while time.time() - timeStart < 60:
                    if exiting:
                        return
                    if not connected:
                        FBlog = FBlogRead()
                    time.sleep(1)


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
        try:
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
        except Exception as err:
            errmsg = "getPlayerData()函数报错, 信息:\n"+str(err)
            log(errmsg, sendtogamewithERROR = True)
            raise Exception(str(err))

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
        try:
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
        except Exception as err:
            errmsg = "setPlayerData()函数报错, 信息:\n"+str(err)
            log(errmsg, sendtogamewithERROR = True)
            raise Exception(str(err))

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
        try:
            if dataType == "int":
                return setPlayerData(dataName, playerName, getPlayerData(dataName, playerName)+dataValue, writeNew)
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
        except Exception as err:
            errmsg = "addPlayerData()函数报错, 信息:\n"+str(err)
            log(errmsg, sendtogamewithERROR = True)
            raise Exception(str(err))


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


    def getTarget(sth: str, timeout: bool | int = 1, error: None | str = None) -> list:
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
        result = sendcmd("/tell @s get%s" % sth, True, timeout, error)["OutputMessages"][0]["Parameters"][1][3:]
        if ", " not in result:
            if not result:
                return []
            return [result]
        else:
            return result.split(", ")


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


    def getPos(targetNameToGet: str) -> dict:
        """
        获取租赁服内玩家坐标的函数

        参数:
            targetNameToGet: str -> 玩家名称
        返回: dict -> 获取结果
        """
        if (targetNameToGet not in allplayers) and (targetNameToGet != robotname) and (not targetNameToGet.startswith("@a")):
            raise Exception("Player not found.")
        result = sendcmd("/querytarget %s" % targetNameToGet, True)["OutputMessages"][0]
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
        try:
            if statusName+".txt" not in os.listdir("status"):
                pass
            file = open("status/%s.txt" % statusName, "r", encoding = "utf-8", errors = "ignore")
            status = file.read()
        except:
            status = "获取失败"
            errmsg = "getStatus()函数报错, 信息:\n"+str(err)
            log(errmsg, sendtogamewithERROR = True)
        finally:
            try:
                file.close()
            except:
                pass
            finally:
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
        try:
            file = open("status/%s.txt" % statusName, "w", encoding = "utf-8", errors = "ignore")
            file.write(str(status))
        except Exception as err:
            status = "设置失败"
            errmsg = "setStatus()函数报错, 信息:\n"+str(err)
            log(errmsg, sendtogamewithERROR = True)
        finally:
            try:
                file.close()
            except:
                pass
            finally:
                return status


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
        if where != "console" and where != "server":
            raise Exception("invalid argument")
        if where == "server" and (who is None):
            raise Exception("invalid argument")
        qr = qrcode.QRCode()
        qr.add_data(text)
        qrline = ""
        for i in qr.get_matrix():
            for j in i:
                if j == False:
                    if where == "console":
                        qrline += "\033[0;37;7m  "
                    else:
                        qrline += "§f▓"
                else:
                    if where == "console":
                        qrline += "\033[0m  "
                    else:
                        qrline += "§0▓"
            if where == "console":
                color("%s\033[0m" % qrline)
            else:
                tellrawText(who, text = "§l"+qrline)
            qrline = ""


    sendcmdResponse = {}
    def sendcmd(cmd: str, waitForResponse: bool = False, timeout: float | int = 1, error: None | str = None) -> None:
        global sendcmdResponse
        """
        以Web Socket身份发送指令到租赁服的函数

        参数:
            cmd: str.MinecraftCommand -> 要在租赁服执行的指令
        返回: 无返回值
        """
        try:
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
        except Exception as err:
            if not error:
                errmsg = "sendcmd()函数报错, 信息:\n"+str(err)
                log(errmsg)
            return err

    def sendwscmd(cmd: str, waitForResponse: bool = False) -> None:
        global sendcmdResponse
        """
        以玩家(FastBuilder机器人)身份发送指令到租赁服的函数

        参数:
            cmd: str.MinecraftCommand -> 要在租赁服执行的指令
        返回: 无返回值
        """
        try:
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
        except Exception as err:
            errmsg = "sendwscmd()函数报错, 信息:\n"+str(err)
            log(errmsg)
            return err

    def sendwocmd(cmd: str) -> None:
        """
        以最高权限(租赁服控制台)身份发送指令到租赁服的函数
        警告: 你可以执行 /stop, 这会导致租赁服关闭, 然后重启

        参数:
            cmd: str.MinecraftCommand -> 要在租赁服执行的指令
        返回: 无返回值
        """
        try:
            if cmd[0] == "/" or cmd[0] == "!":
                cmd = cmd[1:]
            conn.SendNoResponseCommand(connID, cmd)
        except Exception as err:
            errmsg = "sendwocmd()函数报错, 信息:\n"+str(err)
            log(errmsg)

    def sendfbcmd(cmd: str) -> None:
        """
        发送命令到FastBuilder的函数

        参数:
            cmd: str.FastBuilderCommand -> FastBuilder执行指令
        返回: 无返回值
        """
        try:
            if cmd[0] == "?":
                cmd = cmd[1:]
            conn.SendFBCommand(connID, cmd)
        except Exception as err:
            errmsg = "sendfbcmd()函数报错, 信息:\n"+str(err)
            log(errmsg)
            exitChatbarMenu()


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
    def processPacket(self) -> None:
        """
        处理FastBuilder发送来的包的函数
        你不应该使用此函数, 命令系统会在运行FastBuilder后以新线程启动此函数
        """
        global msgLastRecvTime, XUID2playerName, timeSpentFBRun, msgList, server, server, connID, robotname, allplayers, connected
        try:
            connected = True
            msgList.append([-100, {"pluginRunType": "init"}])
            sendwocmd("changesetting allow-cheats true")
            color('§eDetecting operator permission by executing "/time add 0".')
            result = sendcmd("/time add 0", True, timeout = 10)["OutputMessages"][0]
            if result["Success"] == False:
                if result["Message"] == "commands.generic.unknown":
                    color("§4执行命令失败: 未知的命令. 有可能是机器人没有op权限.")
                if result["Message"] == "commands.generic.disabled":
                    color("§4执行命令失败: 此等级未启用作弊. 有可能是未打开允许作弊.")
                else:
                    color("§4执行命令失败: %s." % result["Message"])
                raise Exception("Can not execute operator commands.")

            color("§eGetting robot name and online players.")
            robotname = getTarget("@s", timeout = 5)[0]
            if ")" in robotname:
                color("§4Invalid FastBuilder robot name.")
                exitChatbarMenu(reason = "Invalid FastBuilder robot name.")
            if robotname not in adminhigh:
                adminhigh.append(robotname)
            allplayers = getTarget("@a", timeout = 5)

            color("§eTesting whether there are prohibited words in players' nickname.")
            for i in allplayers[:]:
                color("§eNow testing: %s" % i, replace = True, replaceByNext = True)
                hasPWord = False
                if getPlayerData("prohibitedWord", i, "False") == "False":
                    if prohibitedWordTest(i):
                        hasPWord = True
                        setPlayerData("prohibitedWord", i, "True")
                else:
                    hasPWord = True
                if hasPWord:
                    color("§4There are prohibited words in %s's nickname. DotCS will kick him." % i)
                    sendwocmd('/kick "%s" §c您的名称内有违禁词, 无法进服.' % i)
                    allplayers.remove(i)

            color("§eGetting players' XUID.")
            for i in allplayers:
                color("§eNow getting: %s" % i, replace = True, replaceByNext = True)
                result = sendcmd('/querytarget @a[name="%s"]' % i, True, 5)["OutputMessages"][0]
                if result["Success"] == False:
                    raise Exception("Failed to get the XUID.")
                XUID2playerName[json.loads(result["Parameters"][0])[0]["uniqueId"][-8:]] = i
            for i in allplayers:
                color("§eNow authing: %s" % i, replace = True, replaceByNext = True)
                if i not in list(XUID2playerName.values()):
                    raise Exception("Failed to get the XUID.")
            allplayers.remove(robotname)

            createThread("获取租赁服游戏时间并计算tps", data = {}, func = getGameTimeRepeat)
            createThread("执行repeat类插件", data = {}, func = pluginRepeat)

            timeSpentRun = float(time.time()-timeStartRun)
            timeSpentDotCSRun = timeSpentRun-timeSpentFBRun
            color("§aDotCS Community started successfully. (total: %.2fs, DotCS: %.2fs, FB: %.2fs)" % (timeSpentRun, timeSpentDotCSRun, timeSpentFBRun))
            tellrawText("@a", "§l§6System§r", '§6".命令"系统成功启动.')
            tellrawText("@a", "§l§6System§r", "§6共加载 §l%d§r§6 个插件/函数." % len(pluginList))
            sendcmd("/time add 0")
            sendcmd("/kill @e[type=xp_orb]")
            sendcmd("/gamemode c")
            sendcmd("/effect @s resistance 999999 19 true")
            sendcmd("/effect @s invisibility 999999 0 true")
            sendcmd("/tp @s 100000 100000 100000")
            if not faststart:
                color('You can type "faststart" in console to make DotCS start quicklier.')

            log("§6Your FastBuilder robot name: %s" % robotname)
            log("§eOnline players: "+(", ".join(allplayers)))

            while True:
                if exiting:
                    return
                if msgList == []:
                    if time.time()-msgLastRecvTime >= 30:
                        log("§430秒未收到包")
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
                            log(str(textType)+" "+msg)
                    
                    # 处理系统信息
                    elif textType == 2:
                        # 处理玩家准备进服信息
                        if msg == "§e%multiplayer.player.joining":
                            playername = jsonPkt["Parameters"][0]
                            log("§e%s 正在加入游戏" % playername)
                            hasPWord = False
                            if getPlayerData("prohibitedWord", playername, "False") == "False":
                                if prohibitedWordTest(playername):
                                    hasPWord = True
                                    setPlayerData("prohibitedWord", playername, "True")
                            else:
                                hasPWord = True
                            if hasPWord:
                                log("§4There are prohibited words in %s's nickname. DotCS will kick him." % playername)
                                sendwocmd('/kick "%s" §c您的名称内有违禁词, 无法进服.' % playername)
                                continue
                            pluginRunType = "player prejoin"

                        # 处理玩家进服信息
                        if msg == "§e%multiplayer.player.joined":
                            playername = jsonPkt["Parameters"][0]
                            if playername not in allplayers:
                                allplayers.append(playername)
                            log("§e%s 加入了游戏" % playername)
                            pluginRunType = "player join"
                        
                        # 处理玩家退出信息
                        elif msg == "§e%multiplayer.player.left":
                            playername = jsonPkt["Parameters"][0]
                            if playername in allplayers:
                                allplayers.remove(playername)
                            log("§e%s 退出了游戏" % playername)
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
                                log("%s 失败了, 信息: %s" % (playername, msg))
                                pluginRunType = "player death"
                        
                        # 过滤其他信息
                        else:
                            pass
                    
                    # 处理玩家在聊天栏发送的信息, tell信息以及say信息
                    elif textType == 1 or textType == 7 or textType == 8:
                        if not (msg.startswith("test") or msg.startswith("get")):
                            log(str(textType)+" <"+playername+">"+" "+msg)
                        if playername in allplayers or playername == robotname:
                            pluginRunType = "player message"


                if packetType == -100:
                    pluginRunType = jsonPkt["pluginRunType"]

                for i in pluginList:
                    if i.enable:
                        for j in ["packet -1", "packet %d" % packetType, pluginRunType]:
                            try:
                                if j in i.pluginCode:
                                    exec(i.pluginCode[j])
                            except PluginSkip: # 感谢SuperScript提供的建议.
                                pass
                            except Exception as err:
                                errmsg = "插件 %s %s 报错, 信息:\n%s" % (i.pluginName, pluginRunType, str(err))
                                log(errmsg, sendtogamewithERROR = True)
                                color("§c"+traceback.format_exc())


        except Exception as err:
            errmsg = "信息处理报错, 信息:\n"+str(err)
            log(errmsg)
            color("§c"+traceback.format_exc())
            exitChatbarMenu(reason = "Process packet error.")


    def revPacket(self) -> None:
        """
        连接FastBuilder并接收其发送来的包的函数
        你不应该使用此函数, 命令系统会在运行FastBuilder后以新线程启动此函数
        """
        global msgLastRecvTime, timeSpentFBRun, msgList, connID, timeStartFBRun, FBlog

        # 尝试连接
        color("§eConnecting to FastBuilder program.")
        startTime = time.time()
        while True:
            try:
                connID = conn.ConnectFB("%s:%d" % (FBip, FBport))
                break
            except:
                spendTime = time.time()-startTime
                if spendTime >= 20:
                    color("§4FastBuilder超过20秒未连接上租赁服, 正在退出.")
                    exitChatbarMenu(reason = "FastBuilder timed out.")
                color("Connecting FastBuilder, %.2fs" % spendTime, replace = True, replaceByNext = True)
        # 连上了
        color("§aConnected to FastBuilder program.")
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
                msgList.append([packetType, jsonPkt, packetNum])
                for i in pluginList:
                    try:
                        if i.enable and pluginRunType in i.pluginCode:
                            exec(i.pluginCode[pluginRunType])
                    except Exception as err:
                        errmsg = "插件 %s %s 报错, 信息:\n%s" % (i.pluginName, pluginRunType, str(err))
                        log(errmsg, sendtogamewithERROR = True)
                        color("§c"+traceback.format_exc())

            except Exception as err:
                errmsg = "收取数据包报错, 信息:\n"+str(err)
                log(errmsg)
                color("§c"+traceback.format_exc())
                exitChatbarMenu(reason = "Receive packet error.")


    def consoleInput(self) -> None:
        """
        控制台执行代码或使用聊天栏菜单的函数
        你不应该使用此函数, 命令系统会启动时以新线程运行此函数
        """
        while True:
            try:
                time.sleep(0.1)
                input_msg = input("")
                if not input_msg:
                    continue
                if input_msg == "exit" or input_msg == ".restart" or input_msg == ".stop":
                    exitChatbarMenu()
                    time.sleep(1)
                elif input_msg == "faststart":
                    setStatus("faststart", "True")
                elif input_msg[0] == "/":
                    sendcmd(input_msg)
                elif input_msg[0] == "!":
                    sendwocmd(input_msg)
                elif input_msg[0] == "?":
                    sendfbcmd(input_msg)
                elif input_msg[0] == ".":
                    msgList.append([9, {"TextType": 1, "SourceName": robotname, "Message": input_msg}])
                elif input_msg == "list":
                    print(allplayers)
                else:
                    exec(input_msg)
            except Exception as err:
                errmsg = "console()报错, 信息:\n"+str(err)
                log(errmsg, sendtogamewithERROR = True)
                color("§c"+traceback.format_exc())



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
                    color("§eStarting thread %s." % self.name)
                if getType(self.func) != "str":
                    self.func(self)
                else:
                    exec("%s(self)" % self.func)
            except Exception as err:
                errmsg = ("Thread %s 报错, 信息:\n" % self.name)+str(err)
                log(errmsg, sendtogamewithERROR = True)
                color("§c"+traceback.format_exc())
            except SystemExit as err:
                pass
                # color("§eThread %s has been terminated forcely." % self.name)
            finally:
                if self.output:
                    color("§eEnded thread %s." % self.name)
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
                color('Exception raise failure')


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
        version = "v0.10.4" # 设置版本号
        timeStartRun = time.time() # 记录启动时间
        FBip = "127.0.0.1"
        FBport = 8000
        if os.path.isfile("robotOld.exe"):
            os.remove("robotOld.exe")
        if os.path.isfile("robotNew.exe"):
            os.remove("robotNew.exe")
        faststart = getStatus("faststart")
        if faststart == "获取失败":
            faststart = ""
        if not faststart:
            countdown(0.1, "§e命令系统即将开始启动")

        color(title4)
        color('§b".命令"系统社区版 - 租赁服聊天栏菜单\n".Dot" Command System Community(DotCS)\n社区版及其自带插件作者: 7912\nPro版作者: art\n此版本为社区版, 费用将不超过0.01元/月\nDotCS基于FastBuilder.')
        color('§b用户交流群: 467443403')
        if not faststart:
            countdown(3, "§e请阅读说明")

        # 检测fbtoken文件
        if "fbtoken" not in os.listdir():
            color("§4请下载fbtoken, 放进目录后重启.")
            exitChatbarMenu(delay = 60, reason = "fbtoken not found")

        color("FastBuilder connection address: %s:%d" % (FBip, FBport))

        # 如果租赁服号未设置, 则请求输入租赁服号并存入server.txt
        print("Reading server number.")
        if not os.path.isfile("server.txt"):
            json.dump({"code": 0, "password": 0}, open("server.txt", "w", encoding = "utf-8"), indent = 4, ensure_ascii = True, sort_keys = True)
        serverConfig = json.load(open("server.txt", "r", encoding = "utf-8"))
        try:
            server, serverPassword = int(serverConfig["code"]), int(serverConfig["password"])
        except:
            try:
                server, serverPassword = int(serverConfig["serverNumber"]), int(serverConfig["serverPassword"])
            except:
                server, serverPassword = 0, 0
            json.dump({"code": server, "password": serverPassword}, open("server.txt", "w", encoding = "utf-8"), indent = 4, ensure_ascii = True, sort_keys = True)
        if server == 0:
            server = int(input("Please input your server code: "))
            json.dump({"code": server, "password": serverPassword}, open("server.txt", "w", encoding = "utf-8"), indent = 4, ensure_ascii = True, sort_keys = True)
        if serverPassword == 0:
            serverPassword = input("Please input your server password: ")
            if not serverPassword:
                serverPassword = 7912
            serverPassword = int(serverPassword)
            json.dump({"code": server, "password": serverPassword}, open("server.txt", "w", encoding = "utf-8"), indent = 4, ensure_ascii = True, sort_keys = True)

        FBkill()
        updateCheck()

        # 加载插件
        # if "获取玩家手持物品.py" in os.listdir("plugin"):
        #     os.remove("plugin/获取玩家手持物品.py")
        # if getStatus("pluginupdate1") != "update":
        #     fileDownload("http://www.dotcs.community/update/获取玩家手持物品或装备.py", "plugin/获取玩家手持物品或装备.py")
        #     setStatus("pluginupdate1", "update")
        
        color("§eLoading plugins.")
        color("§eStep 1: Reading plugins.")
        pluginlist = []
        for filename in os.listdir("plugin"):
            if filename.endswith(".py") or filename.endswith(".py.enc"):
                pluginlist.append(filename)

        for i in range(len(pluginlist)):
            filename = pluginlist[i]
            color("§e[Step 1/2][Plugin %d/%d] Now loading: %s" % (i+1, len(pluginlist), filename), replace = True, replaceByNext = True)
            with open("plugin/"+filename, "rb") as file:
                if filename.endswith(".py.enc"):
                    pluginCode = TDES.decrypt(file.read(), "DotCS Community plugin.", False)
                else:
                    pluginCode = file.read()
                pluginCodeList = pluginCode.decode("utf-8").replace("\r", "").split("# PLUGIN TYPE: ")[1:]
                pluginCodeDict = {}
                for i in pluginCodeList:
                    pluginCodeDict[i.split("\n", 1)[0]] = i.split("\n", 1)[1]
                plugin(filename, pluginCodeDict)
        del pluginlist, pluginCode, pluginCodeList, pluginCodeDict

        color("§eStep 2: Executing def plugins.")
        pluginRunType = "def"
        pluginIndex = 0
        for i in pluginList:
            pluginIndex += 1
            color("§e[Step 2/2][Plugin %d/%d] Now executing: %s" % (pluginIndex, len(pluginList), i.pluginName), replace = True, replaceByNext = True)
            try:
                if i.enable and pluginRunType in i.pluginCode:
                    exec(i.pluginCode[pluginRunType])
            except Exception as err:
                errmsg = "插件 %s %s 报错, 信息:\n%s" % (i.pluginName, pluginRunType, str(err))
                log(errmsg, sendtogamewithERROR = True)
                color("§c"+traceback.format_exc())
                exitChatbarMenu(delay = 60, reason = "Load plugin %s %s error in step 2." % (i.pluginName, pluginRunType))
        color("§aLoaded all plugins.")

        # 启动FastBuilder并等待连接.
        runFB()
        timeStartFBRun = time.time()
        color("§eWaiting for FastBuilder to connect to server %s, please wait." % server)
        createThread("控制台执行命令", data = {}, func = consoleInput)
        createThread("收取数据包", data = {}, func = revPacket)
        createThread("检测命令系统更新并校准在线玩家", data = {}, func = othersRepeat)

        while not exiting:
            time.sleep(0.1)
        
        sys.exit()


except:
    try:
        if not connected:
            color("§c"+traceback.format_exc())
        if exitReason is None:
            color("§eExiting.")
        else:
            color("§eExiting, reason: %s" % str(exitReason))
        color("§eTerminating threads.")
        startTime = time.time()
        while threadList and time.time() - startTime < 10:
            for i in threadList[:]:
                i.stop()
            time.sleep(1)
        if connected:
            conn.ReleaseConnByID(connID)
            time.sleep(0.5)
        if exitDelay != 0:
            countdown(exitDelay, "§eExiting")
    except:
        pass
    finally:
        try:
            FBkill()
        except:
            pass
        threadNum = len(threadList)
        if threadNum > 1:
            color("§4Quit forcely with %d threads have not been terminated:" % threadNum)
            for i in range(len(threadList)):
                color("§4%d. %s" % (i+1, threadList[i].name))
        elif threadNum == 1:
            color("§4Quit forcely with %d thread has not been terminated: \n1. %s" % (threadNum, threadList[0].name))
        elif threadNum == 0:
            color("§aQuit correctly, all threads were terminated.")
