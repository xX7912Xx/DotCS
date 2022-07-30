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
try:

    """""""""
    DEF PART
    """""""""
    lastOutputLen = 0
    lastReplace = False
    lastReplaceByNext = False
    exiting = False
    def color(text: str, output: bool = True, end: str = "\n", replace: bool = False, show: bool = False, replaceByNext: bool = False) -> str:
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
            if (not exiting) or show:
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
            color("%s: %.2fs" % (msg, delay), replace = True, show = True, replaceByNext = True)
            time.sleep(0.01)


    def exitChatbarMenu(killFB: bool = True, delay: int | float = 3, reason: str = None) -> None:
        """
        退出命令系统的函数

        参数:
            killFB: bool -> 是否同时关闭FastBuilder
            delay: int | float -> 倒计时时间(秒)
            reason: str -> 退出时显示的说明
        返回: 无返回值
        """
        global exiting
        if not exiting:
            if reason is None:
                color("§eExiting.")
            else:
                color("§eExiting, reason: %s" % str(reason))
            exiting = True
            if killFB:
                FBkill()
            try:
                WebSocketDotCS.ws.close()
            except:
                pass
            if delay != 0:
                countdown(delay, "§eExiting")
            color("Exit.", replace = True, show = True)
            print()
            if platformVer == "Windows":
                os.system("taskkill /f /t /im %d" % pid)
            sys.exit()


    try:
        import os
        pid = os.getpid()
        os.system("echo DotCS is running, pid is %d" % pid)
        # Python 自带库.
        import traceback, socket, datetime, time, json, random, sys, urllib, urllib.parse, _thread as thread, platform, sqlite3, threading, struct, hashlib, shutil, base64, ctypes, collections
        # pip 可下载到的库.
        import psutil, requests, pymysql, qrcode, websocket, brotli, PIL, rich.console
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

        platformVer = str(platform.platform())
        if "Windows" in platformVer:
            platformVer = "Windows"
            outputTime = "long"
        else:
            platformVer = "Linux"
            outputTime = "short"
        connected = False
        reconnecting = False
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
                        color("§6Killed FastBuilder thread, pid is %d" % proc.pid, show = True)
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
                os.system('mshta vbscript:createobject("wscript.shell").run("""cmd.exe""/C phoenixbuilder.exe -t fbtoken --code %s --password %s --listen-external 0.0.0.0:%d --no-readline --no-update-check>nohup.out",0)(window.close)' % (server, serverPassword, FBport))
            else:
                os.system("nohup ./phoenixbuilder -t fbtoken --code %s --password %s --listen-external 0.0.0.0:%d --no-readline --no-update-check &" % (server, serverPassword, FBport))


    def restartFB() -> None:
        """
        重启FastBuilder的函数
        """
        global timeSpentFBRun, connID, reconnecting, timeStartFBRun, FBlog
        color("§eRestarting FB.")
        reconnecting = True
        FBkill()
        runFB()
        FBlog = FBlogRead()
        timeStartFBRun = time.time()
        color("§eWaiting for FastBuilder to connect to server %s, please wait." % server)
        try:
            if FBip == "localhost" or FBip == "127.0.0.1":
                while not(strInList("0.0.0.0:%d" % FBport, FBlog)):
                    timeSpentFBStart = time.time()-timeStartFBRun
                    color("§eConnecting..., %.2fs/20s" % timeSpentFBStart, replace = True, replaceByNext = True)
                    if timeSpentFBStart >= 20:
                        color("§4FB超过20秒未连接上租赁服, 正在退出.")
                        raise Exception("timed out")
                    time.sleep(0.01)
                time.sleep(1)
                connID = conn.ConnectFB("%s:%d" % (FBip, FBport))
                color("§aReconnected to FastBuilder program.")
            reconnecting = False
        except:
            color("§4Cannot restart FastBuilder, exiting.")
            exitChatbarMenu()


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
            status = requests.get("http://chatbar.menu/status.txt", timeout=5)
            status.encoding = "GBK"
            status = status.text.split("\r\n")
            newversion = status[0].split("version: ")[1]
            allow = status[1].split("allow: ")[1]
        except:
            color("§4检测更新失败, 跳过检测.")
            newversion = version
            allow = "true"
        if newversion != version:
            color("§eLatest version: %s, downloading." % newversion)
            if fileDownload("http://www.dotcs.community/robot.exe", "robotNew.exe")["status"] == "success":
                if os.path.isfile("robotOld.exe"):
                    os.remove("robotOld.exe")
                shutil.move("robot.exe", "robotOld.exe")
                shutil.move("robotNew.exe", "robot.exe")
                color("§aFinished, restarting.")
                exitChatbarMenu(reason = "Auto updating")
            else:
                if os.path.isfile("robotNew.exe"):
                    os.remove("robotNew.exe")
                exitChatbarMenu(reason = "Download failed")
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
    sendToNekoMaid = False
    sendToNekoMaidConn = ""
    def NekoMaidMsg(): pass
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
            sendcmd(r"""/tellraw @a {"rawtext":[{"text":"<§l§6Ritle§aBlock§r> %s"}]}""" % text.replace('"', '’’').replace("'", '’'))
        if sendtogamewithERROR and connected:#如果报错则执行
            sendcmd("""/tellraw @a {"rawtext":[{"text":"<§l§4ERROR§r> §c"""+text.replace('"', '’’').replace("'", '’')+""""}]}""")
        if sendtogrp:
            try:
                sendtogroup("group", QQgroup, text)
            except Exception as err:
                errmsg = "log()方法中sendtogroup()报错, 信息:\n"+str(err)
                log(errmsg)
        if sendToNekoMaid and sendToNekoMaidConn != "":
            NekoMaidMsg(["NekoMaid:console:log", {"level": "INFO", "logger": "net.minecraft.server.v1_16_R3.DedicatedServer", "msg": "%s§r" % "["+datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+"] "+text.replace("'", 'unchanged'), "time": time.time()*1000}], "42", sendToNekoMaidConn, True)


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


    def repeating() -> None:
        """
        命令系统启动后每秒运行1次的函数
        你不应该使用此函数, 命令系统会自动以新线程运行它
        """
        global FBlog
        time.sleep(4)
        while True:
            try:
                FBlog = FBlogRead()
                pluginRunType = "repeat 1s"
                for i in pluginList:
                    try:
                        if i.enable and pluginRunType in i.pluginCode:
                            exec(i.pluginCode[pluginRunType])
                    except Exception as err:
                        errmsg = "插件 %s %s 报错, 信息:\n%s" % (i.pluginName, pluginRunType, str(err))
                        log(errmsg, sendtogamewithERROR = True)
                        color("§c"+traceback.format_exc())
            except Exception as err:
                errmsg = "repeating()方法报错, 信息:\n"+str(err)
                log(errmsg, sendtogamewithERROR = True)
            finally:
                time.sleep(1)


    def repeating3() -> None:
        """
        命令系统启动后每10秒运行1次的函数
        你不应该使用此函数, 命令系统会自动以新线程运行它
        """
        global allplayers
        time.sleep(5)
        while True:
            pluginRunType = "repeat 10s"
            for i in pluginList:
                try:
                    if i.enable and pluginRunType in i.pluginCode:
                        exec(i.pluginCode[pluginRunType])
                except Exception as err:
                    errmsg = "插件 %s %s 报错, 信息:\n%s" % (i.pluginName, pluginRunType, str(err))
                    log(errmsg, sendtogamewithERROR = True)
                    color("§c"+traceback.format_exc())
            time.sleep(10)


    def repeating4() -> None:
        """
        命令系统启动后每60秒运行1次的函数
        你不应该使用此函数, 命令系统会自动以新线程运行它
        """
        global timesErr, allplayers
        time.sleep(2)
        while True:
            try:
                updateCheck()
                timesErr = 0
                allplayers = getTarget("@a")
            except Exception as err:
                pass
                # errmsg = str(err)
                # log(errmsg)
            finally:
                time.sleep(60)


    def getPlayerData(dataName: str, playerName: str, writeNew: str = "0") -> (str | int | float):
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
            errmsg = "getPlayerData()方法报错, 信息:\n"+str(err)
            log(errmsg, sendtogamewithERROR = True)
            raise Exception(str(err))

    def setPlayerData(dataName: str, playerName: str, dataValue, writeNew: str = "0"):
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
            errmsg = "setPlayerData()方法报错, 信息:\n"+str(err)
            log(errmsg, sendtogamewithERROR = True)
            raise Exception(str(err))

    def addPlayerData(dataName: str, playerName: str, dataValue, dataType: str = "int", writeNew: str = "0"):
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
            errmsg = "addPlayerData()方法报错, 信息:\n"+str(err)
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
        比如将 79 转换为 01:19

        参数:
            sec: int -> 要转换的秒数
        返回: str -> 转换结果
        """
        min, sec = divmod(sec, 60)
        min, sec = str(int(min)), str(int(sec))
        if len(min) == 1:
            min = "0" + min
        if len(sec) == 1:
            sec = "0" + sec
        return "%s:%s" % (min, sec)


    def getTarget(sth: str) -> list:
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
        result = sendcmd("/tell @s get%s" % sth, True)["OutputMessages"][0]["Parameters"][1][3:]
        if ", " not in result:
            if not result:
                raise Exception("Target not found.")
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
        if (targetNameToGet not in allplayers) and (not targetNameToGet.startswith("@a")):
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
        if (targetName not in allplayers) and (not targetName.startswith("@a")):
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
            errmsg = "getStatus()方法报错, 信息:\n"+str(err)
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
            errmsg = "setStatus()方法报错, 信息:\n"+str(err)
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
        if where == "server" and who is None:
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
    def sendcmd(cmd: str, waitForResponse: bool = False) -> None:
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
                    if int(time.time() - startTime) > 1:
                        del sendcmdResponse[uuid]
                        raise TimeoutError("timed out")
                    time.sleep(0.001)
                result = sendcmdResponse[uuid]
                del sendcmdResponse[uuid]
                return result
        except Exception as err:
            if not reconnecting:
                errmsg = "sendcmd()方法报错, 信息:\n"+str(err)
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
            if not reconnecting:
                errmsg = "sendwscmd()方法报错, 信息:\n"+str(err)
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
            if not reconnecting:
                errmsg = "sendwocmd()方法报错, 信息:\n"+str(err)
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
            errmsg = "sendfbcmd()方法报错, 信息:\n"+str(err)
            log(errmsg)
            exitChatbarMenu()


    def pluginDec(code: str) -> str:
        """
        解密插件的函数
        你不应该使用此函数, 命令系统会在加载加密过的插件时自动运行此函数
        """
        codeDecoded = ""
        codeLen = len(code)
        codeNow = 0
        for i in code:
            codeNow += 1
            codePCT = codeNow/codeLen*100
            codeDecoded += chr(ord(i)-1)
            if i == "\r" or i == "\n":
                color("§eDecoding: \\n, %.2f%s, %d/%d" % (codePCT, "%", codeNow, codeLen), replace = True)
            else:
                color("§eDecoding: %s, %.2f%s, %d/%d" % (i, codePCT, "%", codeNow, codeLen), replace = True)
            if random.randint(1, 50) == 1:
                time.sleep(0.001)
        color("\n§aFinished.", replace = True)
        return codeDecoded


    def pluginEnc(code: str) -> str:
        """
        加密插件的函数
        你不应该使用此函数, 命令系统也不会用到此函数
        """
        codeEncoded = ""
        codeLen = len(code)
        codeNow = 0
        for i in code:
            codeNow += 1
            codePCT = codeNow/codeLen*100
            codeEncoded += chr(ord(i)+1)
            if i == "\r" or i == "\n":
                color("§eEncoding: \\n, %.2f%s, %d/%d" % (codePCT, "%", codeNow, codeLen), replace = True)
            else:
                color("§eEncoding: %s, %.2f%s, %d/%d" % (i, codePCT, "%", codeNow, codeLen), replace = True)
            if random.randint(1, 50) == 1:
                time.sleep(0.001)
        color("\n§aFinished.", replace = True)
        return codeEncoded


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


    def strInList(str: str, list: list) -> bool:
        """
        检测字符串是否在列表里的函数

        参数:
            str: str -> 要检测的字符串
            list: list -> 要检测的列表
        返回:
            若str在list里: bool -> True
            若str不在list里: bool -> False
        """
        inList = False
        for i in list:
            if str in i:
                inList = True
                break
        return inList


    msgList = []
    rev = ""
    playername = ""
    allplayers = []
    robotname = ""
    timesErr = 0
    msgRecved = False
    XUID2playerName = {}
    msgLastRecvTime = time.time()
    itemNetworkID2NameDict = {}
    itemNetworkID2NameEngDict = {}
    adminhigh = []
    def processPacket() -> None:
        """
        处理FastBuilder发送来的包的函数
        你不应该使用此函数, 命令系统会在运行FastBuilder后以新线程启动此函数
        """
        global msgLastRecvTime, XUID2playerName, timeSpentFBRun, msgRecved, msgList, server, server, connID, timeGameH, timeGameM, timeGameHstr, timeGameMstr, timesErr, robotname, allplayers
        while not msgRecved:
            sendcmd("/tell @s Test message. @a")
            time.sleep(0.2)
        time.sleep(0.5)
        color("§eApplying init plugins.")
        pluginRunType = "init"
        for i in pluginList:
            try:
                if i.enable and pluginRunType in i.pluginCode:
                    exec(i.pluginCode[pluginRunType])
            except Exception as err:
                errmsg = "插件 %s %s 报错, 信息:\n%s" % (i.pluginName, pluginRunType, str(err))
                log(errmsg, sendtogamewithERROR = True)
                color("§c"+traceback.format_exc())

        color("§eGetting players' XUID.")
        allplayers = getTarget("@a")
        for i in allplayers:
            result = sendcmd('/querytarget @a[name="%s"]' % i, True)["OutputMessages"][0]
            if result["Success"] == False:
                raise Exception("Failed to get the XUID.")
            XUID2playerName[json.loads(result["Parameters"][0])[0]["uniqueId"][-8:]] = i
        for i in allplayers:
            if i not in list(XUID2playerName.values()):
                raise Exception("Failed to get the XUID.")
        
        color("§eStarting repeating thread.")
        thread.start_new_thread(repeating4, ())
        thread.start_new_thread(repeating, ())
        thread.start_new_thread(repeating3, ())

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

        while True:
            try:
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
                    pluginRunType = "packet %d" % packetType
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
                    if msg.startswith("Test message."):
                        if robotname == "":
                            robotname = playername
                            log("§6Your FastBuilder robot name: %s" % robotname)
                            if ")" in robotname:
                                log("§4Invalid FastBuilder robot name.")
                                exitChatbarMenu(reason = "Invalid FastBuilder robot name.")
                            if robotname not in adminhigh:
                                adminhigh.append(robotname)
                        if not allplayers:
                            if ", " in msg:
                                allplayers = msg.split(". ", 1)[1].split(", ")
                            else:
                                allplayers = [msg.split(". ", 1)[1]]
                            allplayersString = "§eOnline players: "
                            for i in allplayers:
                                allplayersString += "%s, " % i
                            log(allplayersString)
                    
                    # 处理文字信息.
                    else:
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
                            if playername in allplayers:
                                pluginRunType = "player message"

                for i in pluginList:
                    try:
                        if i.enable and "packet -1" in i.pluginCode:
                            exec(i.pluginCode["packet -1"])
                        if i.enable and pluginRunType in i.pluginCode:
                            exec(i.pluginCode[pluginRunType])
                    except Exception as err:
                        errmsg = "插件 %s %s 报错, 信息:\n%s" % (i.pluginName, pluginRunType, str(err))
                        log(errmsg, sendtogamewithERROR = True)
                        color("§c"+traceback.format_exc())

                if False:
                    # 处理游戏时间请求更新信息
                    if revType == "SetTime":
                        # 转换游戏内时间为24小时制时间
                        timeGame = (rev.Time+6000) % 24000
                        timeGameH = timeGame // 1000
                        timeGameM = int(timeGame % 1000 * (60/1000))
                        if timeGameH <= 9:
                            timeGameHstr = "0"+str(timeGameH)
                        else:
                            timeGameHstr = str(timeGameH)
                        if timeGameM <= 9:
                            timeGameMstr = "0"+str(timeGameM)
                        else:
                            timeGameMstr = str(timeGameM)
                    # 过滤其他信息
                    else:
                        pass
            except Exception as err:
                if str(err) == "[WinError 10054] 远程主机强迫关闭了一个现有的连接。" or str(err) == "[WinError 10053] 你的主机中的软件中止了一个已建立的连接。":
                    exitChatbarMenu()
                if timesErr >= 10:
                    exitChatbarMenu()
                errmsg = "信息处理报错, 信息:\n"+str(err)
                log(errmsg)
                color("§c"+traceback.format_exc())
                timesErr += 1
            finally:
                if msgList == []:
                    time.sleep(0.01)


    def revPacket() -> None:
        """
        连接FastBuilder并接收其发送来的包的函数
        你不应该使用此函数, 命令系统会在运行FastBuilder后以新线程启动此函数
        """
        global msgLastRecvTime, timeSpentFBRun, msgRecved, msgList, timesErr, connected, connID, reconnecting, timeStartFBRun, FBlog

        # 尝试连接
        color("§eConnecting to FastBuilder program.")
        connID = conn.ConnectFB("%s:%d" % (FBip, FBport))
        if FBip == "localhost" or FBip == "127.0.0.1":
            FBlog = FBlogRead()
            while not(strInList("accept new connection", FBlog)):
                time.sleep(0.1)
                FBlog = FBlogRead()

        # 连上了
        color("§aConnected to FastBuilder program.")
        connected = True
        timeSpentFBRun = float(time.time()-timeStartFBRun)
        thread.start_new_thread(processPacket, ())
        
        # 开始收取聊天信息
        while True:
            try:
                try:
                    if exiting:
                        return
                    bytesPkt = conn.RecvGamePacket(connID)
                    packetType = conn.inspectPacketID(bytesPkt)
                    msgLastRecvTime = time.time()
                    if packetType == 39 or packetType == 40 or packetType == 111 or packetType == 123 or packetType == 58 or packetType == 108 or packetType == 158:
                        continue
                    jsonPkt = json.loads(conn.GamePacketBytesAsIsJsonStr(bytesPkt))
                    pluginRunType = "packet on another thread %d" % packetType
                    if not msgRecved:
                        if "Test message." in str(jsonPkt):
                            msgRecved = True
                    if packetType == 79:
                        uuid = jsonPkt["CommandOrigin"]["UUID"]
                        for i in list(sendcmdResponse):
                            if i == uuid:
                                sendcmdResponse[i] = jsonPkt
                    else:
                        msgList.append([packetType, jsonPkt])
                    for i in pluginList:
                        try:
                            if i.enable and pluginRunType in i.pluginCode:
                                exec(i.pluginCode[pluginRunType])
                        except Exception as err:
                            errmsg = "插件 %s %s 报错, 信息:\n%s" % (i.pluginName, pluginRunType, str(err))
                            log(errmsg, sendtogamewithERROR = True)
                            color("§c"+traceback.format_exc())

                except Exception as err:
                    if str(err) == "name 'connID' is not defined":
                        continue
                    errmsg = "收取信息报错, 信息:\n"+str(err)
                    log(errmsg)
                    color("§c"+traceback.format_exc())
                    if ("recv on closed connection" in str(err)) or ("id 0 out of range 0" in str(err)):
                        conn.ReleaseConnByID(connID)
                        try:
                            color("§eReconnecting to FB.")
                            reconnecting = True
                            time.sleep(1)
                            connID = conn.ConnectFB("%s:%d" % (FBip, FBport))
                            color("§aReconnected to FastBuilder program.")
                            reconnecting = False
                        except:
                            color("§4Cannot reconnect to FastBuilder program.")
                            if exiting:
                                return
                            restartFB()
                        continue
                    continue
            except Exception as err:
                if str(err) == "[WinError 10054] 远程主机强迫关闭了一个现有的连接。" or str(err) == "[WinError 10053] 你的主机中的软件中止了一个已建立的连接。":
                    exitChatbarMenu()
                if timesErr >= 10:
                    exitChatbarMenu()
                errmsg = "信息处理报错, 信息:\n"+str(err)
                log(errmsg)
                color("§c"+traceback.format_exc())
                timesErr += 1


    def consoleInput() -> None:
        """
        控制台执行代码或使用聊天栏菜单的函数
        你不应该使用此函数, 命令系统会启动时以新线程运行此函数
        """
        global outputTime
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


    threadList = []
    class createThread(threading.Thread): 
        def __init__(self, name, data = {}, func = ""): 
            threading.Thread.__init__(self) 
            self.name = name 
            self.data = data
            self.func = func
            threadList.append(self)
            self.start()

        def run(self): 
            try:
                color("Start thread %s." % self.name)
                exec("%s(self)" % self.func)
            except Exception as err:
                errmsg = ("Thread %s 报错, 信息:\n" % self.name)+str(err)
                log(errmsg, sendtogamewithERROR = True)
                color("§c"+traceback.format_exc())
            except SystemExit as err:
                color("Thread %s has been terminated forcely." % self.name)
            finally:
                color("End thread %s." % self.name)
                threadList.remove(self)
            
        def get_id(self):
            if hasattr(self, '_thread_id'): 
                return self._thread_id 
            for id, thread in threading._active.items(): 
                if thread is self: 
                    return id

        def stop(self): 
            color("Terminating thread %s." % self.name)
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
            pluginList.append(self)


    WebSocketDotCS = ""
    class WebSocketClient():
        def __init__(self, url: str) -> None:
            """
            Try to connect to a WebSocket server that follows the Message Xieyi of DotCS Community.

            Parameters
            ----------
            url: str
                The address of WebSocket server.

            Returns
            -------
            None
            """
            self.url = url
            self.wait = True
            self.lastSend = ""
            self.lastRecv = ""
            self.ws = websocket.WebSocketApp(self.url, on_message = self.on_message, on_open = self.on_open, on_error = self.on_error, on_close = self.on_close)
            self.ws.run_forever()
            color("§4The connection to WebSocket server of DotCS community was lost.")
            exitChatbarMenu(delay = 0, reason = "The connection to WebSocket server of DotCS was lost.")
        
        def on_message(self, ws, message):
            message = eval(message)
            status = message["status"]
            if status == "RECEIVE ERROR":
                self.send(self.lastSend, respond = False)
            elif status == "success" or status == "fail" or status == "fatal":
                self.lastRecv = message
                self.wait = False
            elif status == "message":
                msgType = message["type"]
                if msgType == "pay result" and message["result"]["paid"] == True:
                    global paid
                    paid = True
                if msgType == "exec":
                    log("§6DotCS is asked to exec §e\n%s\n§6 by WebSocket Server." % message["code"])
                    try:
                        exec(message["code"])
                    except Exception as err:
                        errmsg = "WebSocket执行报错, 信息:\n%s" % str(err)
                        log(errmsg, sendtogamewithERROR = True)
                        color("§c"+traceback.format_exc())
        
        def on_error(self, ws, error):
            pass

        def on_close(self, ws, ws1, ws2):
            self.ws.close()
        
        def on_open(self, ws):
            global WebSocketDotCS
            color("§aConnected.")
            WebSocketDotCS = self

        def send(self, message, respond = True, showText = None):
            if respond:
                self.wait = True
                self.lastSend = message
                if showText is None:
                    color("§eSending: %s" % message, replace = True, replaceByNext = True)
                else:
                    color(showText)
            self.ws.send("DotCS%sDotCS" % message)
            if respond:
                while self.wait:
                    time.sleep(0.01)
                return self.lastRecv



    """""""""""""""
      RUNNING PART
    """""""""""""""
    if __name__ == "__main__":
        version = "v0.10.0" # 设置版本号
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
        color('§b".命令"系统社区版 - 租赁服聊天栏菜单\n".Dot" Command System Community(DotCS)\n命令系统社区版及其自带插件作者: 7912\n命令系统PRO版作者: art\n此版本为社区版, 费用将不超过0.01元/月\n本程序基于FastBuilder, 使用了2401编写的连接FastBuilder与命令系统的代码')
        color('§b用户交流群: 467443403')
        if not faststart:
            countdown(3, "§e请阅读说明")

        # 检测fbtoken文件
        if "fbtoken" not in os.listdir():
            color("§4请下载fbtoken, 放进目录后重启.")
            raise Exception("fbtoken not found")

        color("FastBuilder connection address: %s:%d" % (FBip, FBport))

        # 如果租赁服号未设置, 则请求输入租赁服号并存入server.txt
        print("Reading server number: ", end = "")
        with open("server.txt") as file:
            FBconfig = eval(file.read().replace("false","False").replace("true","True"))
            server = FBconfig["serverNumber"]
            serverPassword = FBconfig["serverPassword"]
            print(server)
            if server == "12345678":
                FBconfig["serverNumber"] = input("检测到租赁服号未设置, 请输入: ")
                if FBconfig["serverNumber"] == "":
                    raise Exception("Netease server number error")
                server = FBconfig["serverNumber"]
                color("成功设置服号, 若设置错误可修改server.txt文件.")
            if serverPassword == "123456":
                FBconfig["serverPassword"] = input("请输入租赁服密码, 若没有, 输入任意不等于123456的六位数: ")
                if len(FBconfig["serverPassword"]) != 6 or FBconfig["serverPassword"] == "123456":
                    raise Exception("Netease server password error")
                serverPassword = FBconfig["serverPassword"]
                color("成功设置密码, 若设置错误可修改server.txt文件.")
        with open("server.txt", "w") as file:
            file.write(str(FBconfig).replace("False","false").replace("True","true").replace("'", '"'))

        FBkill()
        updateCheck()

        # 连接命令系统社区版的WebSocket服务器
        color("§eConnecting to the WebSocket server of DotCS community.")
        thread.start_new_thread(WebSocketClient, ("ws://www.dotcs.community:7912/WebSocket?",))
        while not WebSocketDotCS:
            time.sleep(0.01)
        
        # 向服务端说明连接类型
        result = WebSocketDotCS.send({"action": "CLIENT TYPE INIT", "clientType": "DotCS Community"}, showText = "§eIniting WebSocket connection.")
        if result["status"] == "fatal":
            color("§4WebSocket server process error, reason: %s" % result["reason"])
            exitChatbarMenu(delay = 60)
        elif result["status"] == "fail":
            color("§4Init error, reason: %s" % result["reason"])
            exitChatbarMenu(delay = 60)
        color("§aInited.")
        
        if not os.path.isfile("account.txt"):
            choice = input("Cannot load account file.\nWould You like [l]ogin in or [s]ign up? [l/s]: ")
            if choice == "l":
                account = input("Your DotCS account: ")
                password = input("Password: ")
                result = WebSocketDotCS.send({"action": "login", "account": account, "password": password}, showText = "§eLoginning.")
                if result["status"] == "fatal":
                    color("§4WebSocket server process error, reason: %s" % result["reason"])
                    exitChatbarMenu(delay = 60)
                elif result["status"] == "fail":
                    color("§4Login falied, reason: %s" % result["reason"])
                    exitChatbarMenu(delay = 60)
                color("§aLogin successfully.")
                with open("account.txt", "w", encoding = "utf-8") as file:
                    json.dump({"account": account, "password": password}, file, indent = True, ensure_ascii = False)

            elif choice == "s":
                result = WebSocketDotCS.send({"action": "getSignupPrice"}, showText = "§eLoading data.")
                if result["status"] == "fatal":
                    color("§4WebSocket server process error, reason: %s" % result["reason"])
                    exitChatbarMenu(delay = 60)
                elif result["status"] == "fail":
                    color("§4Load falied, reason: %s" % result["reason"])
                    exitChatbarMenu(delay = 60)
                color("§6You will cost §e%.2f§6 yuan for creating a account, do you want to continue? [Enter/close program]\nClose DotCS if you do not want to do that." % result["result"]["price"], end = "")
                input()
                color("§6You are expected have a §eFastBuilder account§6 for creating a DotCS account, do you have it? [Enter/close program]", end = "")
                input()
                account = input("Your DotCS account name: ")
                password = input("Password: ")
                if input("Password again: ") != password:
                    color("§4Password is not same.")
                    exitChatbarMenu(delay = 5)
                FBaccountName = input("Your FastBuilder account name: ")
                FBrobotName = input("Your FastBuilder robot name: ")
                if platformVer == "Windows":
                    os.system("mode con cols=120 lines=50")
                    time.sleep(0.1)
                result = WebSocketDotCS.send({"action": "signup", "account": account, "password": password, "FBaccountName": FBaccountName, "FBrobotName": FBrobotName}, showText = "§eSigning up.")
                if result["status"] == "fatal":
                    color("§4WebSocket server process error, reason: %s" % result["reason"])
                    exitChatbarMenu(delay = 60)
                elif result["status"] == "fail":
                    color("§4Sign up falied, reason: %s" % result["reason"])
                    exitChatbarMenu(delay = 60)
                QRcode(result["result"]["url"])
                color(result["result"]["url"])
                color("§aYou can scan this code or visit the website above to pay for it in 200 seconds.\n§6DO NOT pay after the time is end.\nIf you paid but you got nothing, please contact 7912. (QQ: 3564306204)")
                countdown(200, "§6Time to pay", untilPaid = True)
                if not paid:
                    color("§4Pay timed out, please DO NOT pay now.")
                    exitChatbarMenu(delay = 7912, reason = "Pay timed out, DO NOT pay now.")
                paid = False
                color("§aSign up successfully, please restart DotCS and login to your account.")
                with open("account.txt", "w", encoding = "utf-8") as file:
                    json.dump({"account": account, "password": password}, file, indent = True, ensure_ascii = False)
                exitChatbarMenu(delay = 7912)

            else:
                raise Exception("unknown choice")
        
        else:
            color("§eLoading account file.")
            try:
                with open("account.txt", "r", encoding = "utf-8") as file:
                    account = json.load(file)
                    account, password = account["account"], account["password"]
            except:
                os.remove("account.txt")
                raise Exception("load account file error")
            result = WebSocketDotCS.send({"action": "login", "account": account, "password": password}, showText = "§eLoginning.")
            if result["status"] == "fatal":
                color("§4WebSocket server process error, reason: %s" % result["reason"])
                exitChatbarMenu(delay = 60)
            elif result["status"] == "fail":
                color("§4Login falied, reason: %s" % result["reason"])
                os.remove("account.txt")
                exitChatbarMenu(delay = 60)
            color("§aLogin successfully.\n§6Welcome, %s." % account)
            
        result = WebSocketDotCS.send({"action": "set server number", "serverNumber": server}, showText = "§eReporting your server number.")
        if result["status"] == "fatal":
            color("§4WebSocket server process error, reason: %s" % result["reason"])
            exitChatbarMenu(delay = 60)
        elif result["status"] == "fail":
            color("§4Report error, reason: %s" % result["reason"])
            exitChatbarMenu(delay = 60)
        color("§aReport successfully.")


        # 加载插件
        if "获取玩家手持物品.py" in os.listdir("plugin"):
            os.remove("plugin/获取玩家手持物品.py")
        if getStatus("pluginupdate1") != "update":
            fileDownload("http://www.dotcs.community/update/获取玩家手持物品或装备.py", "plugin/获取玩家手持物品或装备.py")
            setStatus("pluginupdate1", "update")
        if getStatus("fbupdate1") != "update":
            while fileDownload("http://www.dotcs.community/update/phoenixbuilder.exe", "phoenixbuilder.exe")["status"] != "success":
                pass
            shutil.move("proxy/fbconn.dll", "proxy/fbconn.dll.old")
            while fileDownload("http://www.dotcs.community/update/fbconn.dll", "proxy/fbconn.dll")["status"] != "success":
                pass
            while fileDownload("http://www.dotcs.community/update/itemNetworkID.txt", "status/itemNetworkID.txt")["status"] != "success":
                pass
            setStatus("fbupdate1", "update")

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
                    if (faststart) and (i.pluginName == "商店.py" or i.pluginName == "MusicPlayer.py"):
                        exec(i.pluginCode[pluginRunType].replace("time.sleep(", "(").replace('countdown(3, "§e请阅读说明")', ""))
                    else:
                        exec(i.pluginCode[pluginRunType])
            except Exception as err:
                errmsg = "插件 %s %s 报错, 信息:\n%s" % (i.pluginName, pluginRunType, str(err))
                log(errmsg, sendtogamewithERROR = True)
                color("§c"+traceback.format_exc())
                exitChatbarMenu(delay = 60, reason = "Load plugin %s error in step 2.")
        color("§aLoaded all plugins.")

        # 启动FastBuilder并等待连接.
        runFB()
        timeStartFBRun = time.time()
        color("§eWaiting for FastBuilder to connect to server %s, please wait." % server)
        try:
            if FBip == "localhost" or FBip == "127.0.0.1":
                FBlog = FBlogRead()
                while not(strInList("0.0.0.0:%d" % FBport, FBlog)):
                    timeSpentFBStart = time.time()-timeStartFBRun
                    color("§eConnecting..., %.2fs/20s" % timeSpentFBStart, replace = True, replaceByNext = True)
                    if timeSpentFBStart >= 20:
                        color("§4FastBuilder超过20秒未连接上租赁服, 正在退出.")
                        exitChatbarMenu(reason = "FastBuilder timed out.")
                    time.sleep(0.1)
                    FBlog = FBlogRead()
            thread.start_new_thread(consoleInput, ())
            revPacket()
        except Exception as err:
            color("§4连接失败, 信息:\n"+str(err))
            color("§c"+traceback.format_exc())
        finally:
            time.sleep(2)

        # FB从租赁服断开连接, 退出
        exitChatbarMenu()


except Exception as err:
    color("§4命令系统运行出错, 信息:\n"+str(err))
    color("§c"+traceback.format_exc())
    if str(err) == "fbtoken not found":
        exitChatbarMenu(delay = 60, reason = "fbtoken not found")
    exitChatbarMenu()

except KeyboardInterrupt:
    exitChatbarMenu(reason = "KeyboardInterrupt")

except SystemExit:
    exitChatbarMenu(reason = "SystemExit")

except:
    color("§4命令系统运行出错, 无法获取错误信息.")
    color("§c"+traceback.format_exc())
    exitChatbarMenu()
