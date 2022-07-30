title1 = \
"""
  ____        _    ____ ____     ____                                      _ _         
 |  _ \  ___ | |_ / ___/ ___|   / ___|___  _ __ ___  _ __ ___  _   _ _ __ (_) |_ _   _ 
 | | | |/ _ \| __| |   \___ \  | |   / _ \| '_ ` _ \| '_ ` _ \| | | | '_ \| | __| | | |
 | |_| | (_) | |_| |___ ___) | | |__| (_) | | | | | | | | | | | |_| | | | | | |_| |_| |
 |____/ \___/ \__|\____|____/   \____\___/|_| |_| |_|_| |_| |_|\__,_|_| |_|_|\__|\__, |
                                                                                 |___/ 
"""
title2 = \
"""
DDDDDDDDDDDDD                                  tttt                 CCCCCCCCCCCCC   SSSSSSSSSSSSSSS 
D::::::::::::DDD                            ttt:::t              CCC::::::::::::C SS:::::::::::::::S
D:::::::::::::::DD                          t:::::t            CC:::::::::::::::CS:::::SSSSSS::::::S
DDD:::::DDDDD:::::D                         t:::::t           C:::::CCCCCCCC::::CS:::::S     SSSSSSS
  D:::::D    D:::::D    ooooooooooo   ttttttt:::::ttttttt    C:::::C       CCCCCCS:::::S            
  D:::::D     D:::::D oo:::::::::::oo t:::::::::::::::::t   C:::::C              S:::::S            
  D:::::D     D:::::Do:::::::::::::::ot:::::::::::::::::t   C:::::C               S::::SSSS         
  D:::::D     D:::::Do:::::ooooo:::::otttttt:::::::tttttt   C:::::C                SS::::::SSSSS    
  D:::::D     D:::::Do::::o     o::::o      t:::::t         C:::::C                  SSS::::::::SS  
  D:::::D     D:::::Do::::o     o::::o      t:::::t         C:::::C                     SSSSSS::::S 
  D:::::D     D:::::Do::::o     o::::o      t:::::t         C:::::C                          S:::::S
  D:::::D    D:::::D o::::o     o::::o      t:::::t    ttttttC:::::C       CCCCCC            S:::::S
DDD:::::DDDDD:::::D  o:::::ooooo:::::o      t::::::tttt:::::t C:::::CCCCCCCC::::CSSSSSSS     S:::::S
D:::::::::::::::DD   o:::::::::::::::o      tt::::::::::::::t  CC:::::::::::::::CS::::::SSSSSS:::::S
D::::::::::::DDD      oo:::::::::::oo         tt:::::::::::tt    CCC::::::::::::CS:::::::::::::::SS 
DDDDDDDDDDDDD           ooooooooooo             ttttttttttt         CCCCCCCCCCCCC SSSSSSSSSSSSSSS   
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
print(\
"""





























Code: http://www.dotcs.community/code/version/""")
try:

    """""""""
    DEF PART
    """""""""
    def __clear_env():
        n = 0
        __keyListNew = []
        for i in globals().keys():
            if i not in __keyList:
                __keyListNew.append(i)
        for i in __keyListNew:
            n += 1
            color("§cCleaning %d/%d: %s" % (n, len(__keyListNew), i))
            globals().pop(i)


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
            exit()


    try:
        PyPiThird = [
            {"name": "bdx_work_shop", "author": "2401PT, SuperScript", "link": "https://github.com/CMA2401PT/BDXWorkShop"}, 
            {"name": "FastBuilder connector", "author": "2401PT", "link": "https://github.com/CMA2401PT/FastBuilder"}
            ]
        import os
        pid = os.getpid()
        os.system("echo DotCS is running, pid is %d" % pid)
        import traceback
        import socket
        import datetime
        import time
        import json
        import random
        import sys
        import urllib
        import urllib.parse
        import _thread as thread
        import requests
        import platform
        import psutil
        import sqlite3
        import pymysql
        import qrcode
        import threading
        import struct
        import hashlib
        import base64
        import websocket
        import brotli
        import PIL
        import rich.console
        import ctypes
        # 初始化变量
        platformVer = str(platform.platform()) # 检测系统版本
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
            time.sleep(0.1)

        for i in PyPiThird:
            color("DotCS uses a PyPi named §e%s§r by §e%s§r, link: %s" % (i["name"], i["author"], i["link"]))
        import bdx_work_shop.canvas
        import bdx_work_shop.artists.cmd_midi_music
        import collections
        from proxy import conn
    except Exception as err:
        color("§4导入Python库失败, 信息:\n"+str(err))
        color("§c"+traceback.format_exc())
        exitChatbarMenu(False, 5)

    class GetTimeoutError(Exception):
        pass

    class TargetNotFoundError(Exception):
        pass

    class PluginSkip(Exception):
        pass


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
        time.sleep(0.5)


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
            try:
                if platformVer == "Linux":
                    os.system("rm nohup.out")
                else:
                    os.system("del nohup.out")
                with open("nohup.out", "w") as file:
                    file.write("")
            except:
                FBkill()
                with open("nohup.out", "w") as file:
                    file.write("")
            if killFB:
                FBkill()
            while is_port_used(FBport):
                color("§ePort %d is used, changing." % FBport)
                FBport += 1
            if platformVer == "Windows":
                os.system('mshta vbscript:createobject("wscript.shell").run("""cmd.exe""/C phoenixbuilder.exe -t fbtoken --code %s --password %s --listen-external 0.0.0.0:%d --no-readline --no-update-check>nohup.out",0)(window.close)' % (server, serverPassword, FBport))
            else:
                os.system("nohup ./phoenixbuilder -t fbtoken --code %s --password %s --listen-external 0.0.0.0:%d --no-readline --no-update-check &" % (server, serverPassword, FBport))


    def restartFB() -> None:
        """
        重启FB的函数
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
            time.sleep(1)
            if platformVer == "Windows":
                if fileDownload("http://www.dotcs.community/robot.exe", "robot_new.exe")["status"] == "success":
                    time.sleep(0.1)
                    if os.path.isfile("robot_old.exe") == True:
                        os.system("del robot_old.exe")
                        time.sleep(0.1)
                    os.system("ren robot.exe robot_old.exe")
                    time.sleep(0.1)
                    os.system("ren robot_new.exe robot.exe")
                    color("§aFinished, restarting.")
                    exitChatbarMenu(reason = "Auto updating")
                else:
                    if os.path.isfile("robot_new.exe") == True:
                        os.system("del robot_new.exe")
                        time.sleep(0.1)
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
                color("["+datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+"] "+text+"\033[0m")
            elif outputTime == "short":
                color("["+datetime.datetime.now().strftime("%H:%M:%S")+"] "+text+"\033[0m")
            else:
                color(text+"\033[0m")
        try:
            with open(filename, mode, encoding = encoding, errors = errors) as file:
                file.write("["+datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+"] "+text+"\n")
        except Exception as err:
            print("写入日志错误, 信息:\n"+str(err))
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
                finally:
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
        return type(sth).__name__


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
        global needToGet, target
        timeStartGet = time.time()
        target = sth
        needToGet = True
        sendcmd("/tell @s getting "+target)
        while True:
            if int(time.time() - timeStartGet) > 1:
                needToGet = False
                raise Exception("timed out")
            if not(needToGet):
                return target
            time.sleep(0.05)


    def getScore(scoreboardName: str, targetName: str) -> int:
        """
        获取租赁服内对应计分板数值的函数

        参数:
            scoreboardName: str -> 计分板名称
            targetName: str -> 计分板对象名称
        返回: int -> 获取结果
        """
        global needToGetScore, score
        timeStartGetScore = time.time()
        score = targetName
        needToGetScore = True
        sendcmd('/tellraw @s {"rawtext":[{"text":"getting "}, {"score":{"name":"%s","objective":"%s"}}]}' % (targetName, scoreboardName))
        while True:
            if int(time.time() - timeStartGetScore) > 1:
                needToGetScore = False
                raise GetTimeoutError("timed out")
            if not(needToGetScore):
                try:
                    score = int(score)
                except:
                    raise Exception("failed to get, maybe the target has no score or the scoreboard doesn't exist.")
                return score
            time.sleep(0.05)


    def getPos(targetName: str) -> dict:
        """
        获取租赁服内玩家坐标的函数

        参数:
            targetName: str -> 玩家名称
        返回: dict -> 获取结果
        """
        global needToGetPos, targPosList
        if targetName not in allplayers and "@a[" not in targetName:
            raise TargetNotFoundError("player not found")
        timeStartGetPos = time.time()
        needToGetPos = True
        if "@a[" in targetName:
            sendcmd("querytarget %s" % targetName)
        else:
            sendcmd("querytarget @a[name=%s]" % targetName)
        while True:
            if int(time.time() - timeStartGetPos) > 1:
                needToGetPos = False
                raise GetTimeoutError("timed out")
            if not(needToGetPos):
                return targPosList
            time.sleep(0.05)


    def getItem(targetName: str, itemName: str, itemSpecialID: int = -1) -> int:
        """
        获取租赁服内玩家某物品个数的函数

        参数:
            targetName: str -> 玩家名称
            itemName: str -> 物品英文名称
            itemSpecialID: int -> 物品特殊值
        返回: int -> 获取结果
        """
        global needToGetItem, haveItem
        if targetName not in allplayers:
            raise TargetNotFoundError("player not found")
        timeStartGetItem = time.time()
        haveItem = 0
        needToGetItem = True
        sendcmd("/clear %s %s %d 0" % (targetName, itemName, itemSpecialID))
        while True:
            if int(time.time() - timeStartGetItem) > 1:
                needToGetItem = False
                raise TimeoutError("timed out")
            if not(needToGetItem):
                return int(haveItem)
            time.sleep(0.05)


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
                print("%s\033[0m" % qrline)
            else:
                tellrawText(who, text = "§l"+qrline)
            qrline = ""


    def msgPlayerSend(playername: str, msg: str) -> None:
        """
        命令系统启动后玩家每发一条信息就运行1次的函数
        你不应该使用此函数, 命令系统会自动在收到玩家发出的信息时运行1次
        """
        for i in range(1, 100):
            exec("global tp_%d, tp_%d_time, tp_%d_time_use" % (i, i, i))
        pluginRunType = "player message"
        for i in pluginList:
            try:
                if i.enable and pluginRunType in i.pluginCode:
                    exec(i.pluginCode[pluginRunType])
            except Exception as err:
                errmsg = "插件 %s %s 报错, 信息:\n%s" % (i.pluginName, pluginRunType, str(err))
                log(errmsg, sendtogamewithERROR = True)
                color("§c"+traceback.format_exc())


    def msgPlayerDeath(playername: str, msg: str, killer: str) -> None:
        """
        命令系统启动后玩家死亡时运行1次的函数
        你不应该使用此函数, 命令系统会自动在玩家死亡时运行1次
        """
        pluginRunType = "player death"
        for i in pluginList:
            try:
                if i.enable and pluginRunType in i.pluginCode:
                    exec(i.pluginCode[pluginRunType])
            except Exception as err:
                errmsg = "插件 %s %s 报错, 信息:\n%s" % (i.pluginName, pluginRunType, str(err))
                log(errmsg, sendtogamewithERROR = True)
                color("§c"+traceback.format_exc())


    def msgPlayerPreJoin(playername: str, msg: str) -> None:
        """
        命令系统启动后玩家准备加入租赁服时运行1次的函数
        你不应该使用此函数, 命令系统会自动在玩家准备加入租赁服时运行1次
        """
        pluginRunType = "player prejoin"
        for i in pluginList:
            try:
                if i.enable and pluginRunType in i.pluginCode:
                    exec(i.pluginCode[pluginRunType])
            except Exception as err:
                errmsg = "插件 %s %s 报错, 信息:\n%s" % (i.pluginName, pluginRunType, str(err))
                log(errmsg, sendtogamewithERROR = True)
                color("§c"+traceback.format_exc())


    def msgPlayerJoin(playername: str, msg: str) -> None:
        """
        命令系统启动后玩家加入租赁服时运行1次的函数
        你不应该使用此函数, 命令系统会自动在玩家加入租赁服时运行1次
        """
        pluginRunType = "player join"
        for i in pluginList:
            try:
                if i.enable and pluginRunType in i.pluginCode:
                    exec(i.pluginCode[pluginRunType])
            except Exception as err:
                errmsg = "插件 %s %s 报错, 信息:\n%s" % (i.pluginName, pluginRunType, str(err))
                log(errmsg, sendtogamewithERROR = True)
                color("§c"+traceback.format_exc())


    def msgPlayerLeave(playername: str, msg: str) -> None:
        """
        命令系统启动后玩家退出租赁服时运行1次的函数
        你不应该使用此函数, 命令系统会自动在玩家退出租赁服时运行1次
        """
        pluginRunType = "player leave"
        for i in pluginList:
            try:
                if i.enable and pluginRunType in i.pluginCode:
                    exec(i.pluginCode[pluginRunType])
            except Exception as err:
                errmsg = "插件 %s %s 报错, 信息:\n%s" % (i.pluginName, pluginRunType, str(err))
                log(errmsg, sendtogamewithERROR = True)
                color("§c"+traceback.format_exc())


    def sendcmd(cmd: str) -> None:
        """
        以Web Socket身份发送指令到租赁服的函数

        参数:
            cmd: str.MinecraftCommand -> 要在租赁服执行的指令
        返回: 无返回值
        """
        try:
            if cmd[0] == "/":
                cmd = cmd[1:]
            conn.SendMCCommand(connID, cmd)
        except Exception as err:
            if not reconnecting:
                errmsg = "sendcmd()方法报错, 信息:\n"+str(err)
                log(errmsg)

    def sendwscmd(cmd: str) -> None:
        """
        以玩家(FastBuilder机器人)身份发送指令到租赁服的函数

        参数:
            cmd: str.MinecraftCommand -> 要在租赁服执行的指令
        返回: 无返回值
        """
        try:
            if cmd[0] == "/":
                cmd = cmd[1:]
            conn.SendWSCommand(connID, cmd)
        except Exception as err:
            errmsg = "sendwscmd()方法报错, 信息:\n"+str(err)
            log(errmsg)

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
                            if strInList("Unauthorized rental server number", FBlogNew) or strInList("对应租赁服号尚未授权", FBlogNew):
                                with open("server.txt", "r") as file:
                                    FBconfig = eval(file.read().replace("false","False").replace("true","True"))
                                    FBconfig["serverNumber"] = input("请重新输入服号: ")
                                    if FBconfig["serverNumber"] == "":
                                        raise Exception("Netease server number error")
                                with open("server.txt", "w") as file:
                                    file.write(str(FBconfig).replace("False","false").replace("True","true").replace("'", '"'))
                                color("§a成功设置服号")
                            if connected:
                                FBkill()
                                # restartFB()
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
    target = ""
    allplayers = []
    robotname = ""
    timesErr = 0
    msgRecved = False
    entityRuntimeID2playerName = {}
    XUID2playerName = {}
    msgLastRecvTime = time.time()
    itemNetworkID2NameDict = {}
    itemNetworkID2NameEngDict = {}
    adminhigh = []
    needToGetMainhandItem = False
    needToGetArmorItem = False
    needToGetMainhandAndArmorItem = False
    targetMainhandAndArmor = ""
    itemMainhandAndArmor = ""
    targetArmor = ""
    targetMainhand = ""
    def processMsg() -> None:
        """
        处理FastBuilder发送来的包的函数
        你不应该使用此函数, 命令系统会在运行FastBuilder后以新线程启动此函数
        """
        global msgLastRecvTime, XUID2playerName, entityRuntimeID2playerName, timeSpentFBRun, msgRecved, msgList, needToGet, target, server, connected, server, connID, timeGameH, timeGameM, timeGameHstr, timeGameMstr, timesErr, robotname, needToGetScore, score, needToGetPos, targPosList, haveItem, needToGetItem, allplayers, needToGetMainhandItem, itemMainhand, needToGetArmorItem, itemArmor, needToGetMainhandAndArmorItem, itemMainhandAndArmor, targetArmor, targetMainhand
        time_old = time.time()
        while not msgRecved:
            sendcmd("/tell @s Test message. @a")
            time.sleep(0.2)
        try:
            adminhigh.append(robotname)
        except:
            pass
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

        color("§eStarting repeating thread.")
        thread.start_new_thread(repeating4, ())
        thread.start_new_thread(repeating, ())
        thread.start_new_thread(repeating3, ())

        sendcmd("/kill @e[type=xp_orb]")
        tellrawText("@a", "§l§6System§r", '§6".命令"系统成功启动.')
        tellrawText("@a", "§l§6System§r", "§6共加载 §l%d§r§6 个插件/函数:" % len(pluginList))
        for i in range(len(pluginList)):
            pass
            # tellrawText("@a", "§l§6System§r", "§6%d. %s" % (i+1, pluginList[i].pluginName))
        # if pluginIgnoredNum >= 1:
        #     tellrawText("@a", "§l§4ERROR§r", "§c共忽略 §l%d§r§c 个插件/函数:" % pluginIgnoredNum)
        #     FinishedLoadingNum = 1
        #     for i in pluginIgnoredNameList:
        #         tellrawText("@a", "§l§4ERROR§r", "§c%d. %s" % (FinishedLoadingNum, i))
        #         FinishedLoadingNum += 1
        timeSpentRun = float(time.time()-timeStartRun)
        timeSpentDotCSRun = timeSpentRun-timeSpentFBRun
        color("§aDotCS Community started successfully. (total: %.2fs, DotCS: %.2fs, FB: %.2fs)" % (timeSpentRun, timeSpentDotCSRun, timeSpentFBRun))
        sendcmd("/time add 0")
        sendcmd("/gamemode c")
        sendcmd("/effect @s resistance 99999 19 true")
        sendcmd("/tp @s 10000 10000 10000")
        if getStatus("report") != "off":
            color("上报租赁服状态已开启, 可于\n§ehttp://www.dotcs.community:7913/api?action=serverRunningSearch§r\n查看, 若不想公开租赁服于网页, 请输入report off来关闭上报.")
        else:
            color("上报租赁服状态已关闭, 可输入report on重新打开.")
        # for i in range(9999):sendcmd("/say %d" % i)

        while True:
            try:
                if msgList == []:
                    if time.time()-msgLastRecvTime >= 30:
                        log("§430秒未收到包")
                        exitChatbarMenu(reason = "Receive packet timed out")
                    # else:
                    #     color(str(time.time()-msgLastRecvTime), replace = True, replaceByNext = True)
                    time.sleep(0.01)
                    continue
                else:
                    try:
                        rev = msgList.pop(0)
                        packetType = rev[0]
                        jsonPkt = json.loads(rev[1])
                    except:
                        continue
                    if packetType == 63 and jsonPkt["ActionType"] == 0:
                        XUID2playerName[jsonPkt["Entries"][0]["XUID"]] = jsonPkt["Entries"][0]["Username"]
                        jsonPkt = {'TextType': 2, 'NeedsTranslation': True, 'SourceName': '', 'Message': '§e%multiplayer.player.joining', 'Parameters': [jsonPkt["Entries"][0]["Username"]], 'XUID': '', 'PlatformChatID': '', 'PlayerRuntimeID': ''}
                        packetType = 9
                    # if "lvl" in str(jsonPkt):
                    #     print(packetType, jsonPkt)

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
                        if "executing" in msg:
                            spent = time.time()-time_old
                            time_old = time.time()
                            if spent != 0:
                                tps = int(20/spent)
                                if tps <= 30:
                                    sendcmd("/scoreboard players set tps main "+str(tps))
                        elif "getting " in msg and textType != 9:
                            targString = msg.split("getting ")[1]
                            if ", " in targString:
                                target = targString.split(", ")
                            else:
                                target = []
                                target.append(targString)
                            needToGet = False
                        elif msg.startswith("Test message."):
                            if robotname == "":
                                robotname = playername
                                log("§6Your FastBuilder robot name: %s" % robotname)
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
                                if outputTime == "long":
                                    msg = msg.replace('{"rawtext":[{"text":"', "").replace('"}]}', "").replace('"},{"text":"', "").replace(r"\n", "\n"+"["+datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+"] "+str(textType)+" ").replace("§l", "")
                                elif outputTime == "short":
                                    msg = msg.replace('{"rawtext":[{"text":"', "").replace('"}]}', "").replace('"},{"text":"', "").replace(r"\n", "\n"+"["+datetime.datetime.now().strftime("%H:%M:%S")+"] "+str(textType)+" ").replace("§l", "")
                                else:
                                    msg = msg.replace('{"rawtext":[{"text":"', "").replace('"}]}', "").replace('"},{"text":"', "").replace(r"\n", "\n"+str(textType)+" ").replace("§l", "")
                                if msg[-1] == "\n":
                                    msg = msg[:-1]
                                if "getting" in msg and needToGetScore:
                                    try:
                                        score = int(msg.split("getting ")[1].replace("\n", ""))
                                    except:
                                        score = "获取失败"
                                    finally:
                                        needToGetScore = False
                                elif "报错, 信息:" not in msg:
                                    msg += "§r"
                                    log(str(textType)+" "+msg)
                            
                            # 处理系统信息
                            elif textType == 2:
                                # 处理玩家准备进服信息
                                if msg == "§e%multiplayer.player.joining":
                                    playername = jsonPkt["Parameters"][0]
                                    log("§e%s 正在加入游戏" % playername)
                                    thread.start_new_thread(msgPlayerPreJoin, (playername, msg))

                                # 处理玩家进服信息
                                if msg == "§e%multiplayer.player.joined":
                                    playername = jsonPkt["Parameters"][0]
                                    if playername not in allplayers:
                                        allplayers.append(playername)
                                    log("§e%s 加入了游戏" % playername)
                                    thread.start_new_thread(msgPlayerJoin, (playername, msg))
                                
                                # 处理玩家退出信息
                                elif msg == "§e%multiplayer.player.left":
                                    playername = jsonPkt["Parameters"][0]
                                    if playername in allplayers:
                                        allplayers.remove(playername)
                                    log("§e%s 退出了游戏" % playername)
                                    thread.start_new_thread(msgPlayerLeave, (playername, msg))
                                    
                                # 处理玩家死亡信息
                                elif msg[0:6] == "death.":
                                    playername = jsonPkt["Parameters"][0]
                                    if len(jsonPkt["Parameters"]) == 2:
                                        killer = jsonPkt["Parameters"][1]
                                    else:
                                        killer = None
                                    log("%s 失败了, 信息: %s" % (playername, msg))
                                    thread.start_new_thread(msgPlayerDeath, (playername, msg, killer))
                                
                                # 过滤其他信息
                                else:
                                    pass
                            
                            # 处理玩家在聊天栏发送的信息, tell信息以及say信息
                            elif textType == 1 or textType == 7 or textType == 8:
                                if not msg.startswith("test"):
                                    log(str(textType)+" <"+playername+">"+" "+msg)
                                thread.start_new_thread(msgPlayerSend, (playername, msg))
                            
                            # 不记得是什么了
                            elif textType == 10:
                                pass

                    # 处理执行命令后的返回信息
                    elif packetType == 79:
                        if "getting " not in str(jsonPkt):
                            outputMessageList = jsonPkt["OutputMessages"]
                            if outputMessageList == []:
                                continue
                            # 用于getPos(), 获取坐标函数
                            if "commands.querytarget.success" in str(outputMessageList):
                                targPosList = []
                                targDimension = int(str(outputMessageList).split('    "dimension" : ')[1].split(r',\n    ')[0])
                                targPosX = float(str(outputMessageList).split(r',\n      "position" : {\n         "x" : ')[1].split(r',\n         "y" : ')[0])
                                targPosY = float(str(outputMessageList).split(r',\n         "y" : ')[1].split(r',\n         "z" : ')[0])-1.6200103759765
                                targPosZ = float(str(outputMessageList).split(r',\n         "z" : ')[1].split(r'\n      },\n      "uniqueId" : ')[0])
                                targRotY = float(str(outputMessageList).split(r',\n      "yRot" : ')[1].split(r"\n   }\n]\n']")[0])
                                targPosList.append({"dimension": targDimension, "x": str(int(targPosX)), "y": str(int(targPosY)), "z": str(int(targPosZ)), "yRot": str(int(targRotY)), "xFloat": float("%.2f" % targPosX), "yFloat": float("%.2f" % targPosY), "zFloat": float("%.2f" % targPosZ), "yRotFloat": float("%.2f" % targRotY)})
                                needToGetPos = False

                            # 用于getItem(), 获取玩家物品数量函数
                            elif "commands.clear.failure.no.items" in str(outputMessageList):
                                haveItem = 0
                                needToGetItem = False
                            elif "commands.clear.testing" in str(outputMessageList):
                                haveItem = int(outputMessageList[0]["Parameters"][1])
                                needToGetItem = False
                            elif outputMessageList[0]["Message"] == "commands.generic.syntax" and len(outputMessageList) == 1:
                                msg = outputMessageList[0]["Parameters"][0]+outputMessageList[0]["Parameters"][1]+outputMessageList[0]["Parameters"][2]
                                if msg[-5:] == " -1 0" or msg[-2:] == " 0":
                                    haveItem = 0
                                    needToGetItem = False

                    # 用于getMainhandItem(), 获取玩家手持物品名称函数
                    elif packetType == 12:
                        try:
                            entityRuntimeID2playerName[jsonPkt["EntityRuntimeID"]] = jsonPkt["Username"]
                        except:
                            pass
                        if needToGetMainhandItem and targetMainhand == jsonPkt["Username"]:
                            itemMainhand = jsonPkt["HeldItem"]["Stack"]
                            try:
                                itemMainhand["itemName"] = itemNetworkID2NameDict[str(jsonPkt["HeldItem"]["Stack"]["NetworkID"])]
                                itemMainhand["itemCmdName"] = itemNetworkID2NameEngDict[str(jsonPkt["HeldItem"]["Stack"]["NetworkID"])]
                            except:
                                itemMainhand["itemName"] = "未知"
                                itemMainhand["itemCmdName"] = "unknown"
                            needToGetMainhandItem = False
                        if needToGetMainhandAndArmorItem and targetMainhandAndArmor == jsonPkt["Username"]:
                            itemMainhandAndArmor["mainHand"] = jsonPkt["HeldItem"]["Stack"]
                            try:
                                itemMainhandAndArmor["mainHand"]["itemName"] = itemNetworkID2NameDict[str(jsonPkt["HeldItem"]["Stack"]["NetworkID"])]
                                itemMainhandAndArmor["mainHand"]["itemCmdName"] = itemNetworkID2NameEngDict[str(jsonPkt["HeldItem"]["Stack"]["NetworkID"])]
                            except:
                                itemMainhandAndArmor["mainHand"]["itemName"] = "未知"
                                itemMainhandAndArmor["mainHand"]["itemCmdName"] = "unknown"

                    # 用于getArmorItem(), 获取玩家装备物品名称函数
                    elif packetType == 32:
                        if needToGetArmorItem and targetArmor == entityRuntimeID2playerName[jsonPkt["EntityRuntimeID"]]:
                            itemArmor["Helmet"] = jsonPkt["Helmet"]["Stack"]
                            itemArmor["Chestplate"] = jsonPkt["Chestplate"]["Stack"]
                            itemArmor["Leggings"] = jsonPkt["Leggings"]["Stack"]
                            itemArmor["Boots"] = jsonPkt["Boots"]["Stack"]
                            for i in itemArmor:
                                try:
                                    itemArmor[i]["itemName"] = itemNetworkID2NameDict[str(jsonPkt[i]["Stack"]["NetworkID"])]
                                    itemArmor[i]["itemCmdName"] = itemNetworkID2NameEngDict[str(jsonPkt[i]["Stack"]["NetworkID"])]
                                except:
                                    itemArmor[i]["itemName"] = "未知"
                                    itemArmor[i]["itemCmdName"] = "unknown"
                            needToGetArmorItem = False
                        if needToGetMainhandAndArmorItem and targetMainhandAndArmor == entityRuntimeID2playerName[jsonPkt["EntityRuntimeID"]]:
                            itemMainhandAndArmor["armor"] = {}
                            itemMainhandAndArmor["armor"]["Helmet"] = jsonPkt["Helmet"]["Stack"]
                            itemMainhandAndArmor["armor"]["Chestplate"] = jsonPkt["Chestplate"]["Stack"]
                            itemMainhandAndArmor["armor"]["Leggings"] = jsonPkt["Leggings"]["Stack"]
                            itemMainhandAndArmor["armor"]["Boots"] = jsonPkt["Boots"]["Stack"]
                            for i in itemMainhandAndArmor["armor"]:
                                try:
                                    itemMainhandAndArmor["armor"][i]["itemName"] = itemNetworkID2NameDict[str(jsonPkt[i]["Stack"]["NetworkID"])]
                                    itemMainhandAndArmor["armor"][i]["itemCmdName"] = itemNetworkID2NameEngDict[str(jsonPkt[i]["Stack"]["NetworkID"])]
                                except:
                                    itemMainhandAndArmor["armor"][i]["itemName"] = "未知"
                                    itemMainhandAndArmor["armor"][i]["itemCmdName"] = "unknown"
                            needToGetMainhandAndArmorItem = False

                    # 用于getArmorItem(), 获取玩家装备物品名称函数
                    elif packetType == 203:
                        if needToGetArmorItem:
                            itemArmor = {}
                            needToGetArmorItem = False
                        if needToGetMainhandAndArmorItem:
                            itemMainhandAndArmor["armor"] = {}
                            needToGetMainhandAndArmorItem = False

                    pluginRunType = "packet %d" % packetType
                    for i in pluginList:
                        try:
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


    def revMsg() -> None:
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

        # 开始处理信息
        thread.start_new_thread(processMsg, ())
        # sendcmd("/gamerule sendcommandfeedback false")
        
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
                    if not msgRecved:
                        if "Test message." in conn.GamePacketBytesAsIsJsonStr(bytesPkt):
                            msgRecved = True
                    msgList.append([packetType, conn.GamePacketBytesAsIsJsonStr(bytesPkt)])
                except Exception as err:
                    if str(err) == "name 'connID' is not defined":
                        continue
                    errmsg = "收取信息报错, 信息:\n"+str(err)
                    log(errmsg)
                    color("§c"+traceback.format_exc())
                    if ("recv on closed connection" in str(err)) or ("id 0 out of range 0" in str(err)):
                        conn.ReleaseConnByID(connID)
                        # errmsg = "FB连接断开报错, 信息:\n"+str(err)
                        # log(errmsg)
                        # exitChatbarMenu()
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
                        # exitChatbarMenu()
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
                if input_msg == "exit":
                    exitChatbarMenu()
                    break
                elif input_msg[0] == "/":
                    sendcmd(input_msg)
                elif input_msg[0] == "!":
                    sendwocmd(input_msg)
                elif input_msg[0] == "?":
                    sendfbcmd(input_msg)
                elif input_msg[0] == ".":
                    thread.start_new_thread(msgPlayerSend, (robotname, input_msg))
                elif input_msg == "list":
                    print(getTarget("@a"))
                elif input_msg == "report on":
                    setStatus("report", "on")
                    color("已开启上报租赁服运行状态")
                elif input_msg == "report off":
                    setStatus("report", "off")
                    color("已关闭上报租赁服运行状态")
                elif input_msg == "output time long":
                    outputTime = "long"
                    color("已设定输出显示长时间")
                elif input_msg == "output time short":
                    outputTime = "short"
                    color("已设定输出显示短时间")
                elif input_msg == "output time none":
                    outputTime = "none"
                    color("已关闭输出显示时间")
                elif input_msg == "set server number":
                    with open("server.txt", "r") as file:
                        FBconfig = eval(file.read().replace("false","False").replace("true","True"))
                        FBconfig["serverNumber"] = input("服号: ")
                    with open("server.txt", "w") as file:
                        file.write(str(FBconfig).replace("False","false").replace("True","true").replace("'", '"'))
                    color("§a成功设置服号")
                    exitChatbarMenu()
                else:
                    exec(input_msg)
            except Exception as err:
                errmsg = "console()报错, 信息:\n"+str(err)
                log(errmsg, sendtogamewithERROR = True)
                color("§c"+traceback.format_exc())










    """""""""""
    CLASS PART
    """""""""""
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
                print("Start thread %s." % self.name)
                exec("%s(self)" % self.func)
            except Exception as err:
                errmsg = ("Thread %s 报错, 信息:\n" % self.name)+str(err)
                log(errmsg, sendtogamewithERROR = True)
                color("§c"+traceback.format_exc())
            except SystemExit as err:
                print("Thread %s has been terminated forcely." % self.name)
            finally:
                print("End thread %s." % self.name)
                threadList.remove(self)
            
        def get_id(self):
            if hasattr(self, '_thread_id'): 
                return self._thread_id 
            for id, thread in threading._active.items(): 
                if thread is self: 
                    return id

        def stop(self): 
            print("Terminating thread %s." % self.name)
            thread_id = self.get_id() 
            res = ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, ctypes.py_object(SystemExit)) 
            if res > 1: 
                ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, 0) 
                print('Exception raise failure')


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
            self.lastShowTextSent = ""
            self.lastIsShowTextSent = False
            self.lastShowTextSendError = ""
            self.lastIsShowTextSendError = False
            self.resendTimes = 0
            self.ws = websocket.WebSocketApp(self.url, on_message = self.on_message, on_open = self.on_open, on_error = self.on_error, on_close = self.on_close)
            self.ws.run_forever()
            # color("§eReconnecting to WebSocket server of DotCS community.")
            color("§4The connection to WebSocket server of DotCS community was lost.")
            exitChatbarMenu(delay = 0, reason = "The connection to WebSocket server of DotCS was lost.")
            # color("§eReconnecting to WebSocket server of DotCS community.", replace = True, replaceByNext = True)
        
        def on_message(self, ws, message):
            # print("Recv: %s" % message)
            message = eval(message)
            status = message["status"]
            if status == "RECEIVE ERROR":
                self.resendTimes += 1
                if self.lastIsShowTextSendError == False:
                    # color("§4Failed to send, resending times is %d: %s" % (self.resendTimes, self.lastSend), replace = True, replaceByNext = True)
                    pass
                else:
                    color(self.lastShowTextSendError, replace = True, replaceByNext = True)
                self.send(self.lastSend, respond = False)
            elif status == "success" or status == "fail" or status == "fatal":
                if self.lastIsShowTextSent == False:
                    # color("§eSent: %s" % self.lastSend)
                    pass
                else:
                    color(self.lastShowTextSent)
                self.lastRecv = message
                self.wait = False
                self.resendTimes = 0
            elif status == "message":
                msgType = message["type"]
                if msgType == "pay result" and message["result"]["paid"] == True:
                    global paid
                    paid = True
                if msgType == "exec":
                    log("§6DotCS is asked to exec §e\n%s\n§6 by WebSocket Server." % message["code"])
                    try:
                        result = {}
                        exec(message["code"])
                        WebSocketDotCS.send({"action": "exec result", "result": result}, showText = "§eSending the result of the exec.")
                    except Exception as err:
                        errmsg = "WebSocket执行报错, 信息:\n%s" % str(err)
                        log(errmsg, sendtogamewithERROR = True)
                        color("§c"+traceback.format_exc())
                        WebSocketDotCS.send({"action": "exec result", "result": str(err)}, showText = "§eSending the result of the exec.")

        
        def on_error(self, ws, error):
            pass

        def on_close(self, ws, ws1, ws2):
            self.ws.close()
            # color("§4The connection to WebSocket server of DotCS community was lost, reconnecting.")
        
        def on_open(self, ws):
            global WebSocketDotCS
            color("§aConnected.")
            WebSocketDotCS = self

            # thread.start_new_thread(self.console, ())

        def send(self, message, respond = True, showText = None, showTextSent = None, showTextSendError = None):
            if respond:
                self.wait = True
                self.lastSend = message
                if showText is None:
                    color("§eSending: %s" % message, replace = True, replaceByNext = True)
                else:
                    color(showText)
                if showTextSent is None:
                    self.lastIsShowTextSent = False
                    self.lastShowTextSent = ""
                else:
                    self.lastIsShowTextSent = True
                    self.lastShowTextSent = showTextSent
                if showTextSendError is None:
                    self.lastIsShowTextSendError = False
                    self.lastShowTextSendError = ""
                else:
                    self.lastIsShowTextSendError = True
                    self.lastShowTextSendError = showTextSendError
            self.ws.send("DotCS%sDotCS" % message)
            if respond:
                while self.wait:
                    time.sleep(0.01)
                return self.lastRecv

        def console(self):
            while True:
                self.send(input("Input your message: "))





    # i = ""
    # __keyList = []
    # for i in globals().keys():
    #     __keyList.append(i)

    """""""""""""""
      RUNNING PART
    """""""""""""""
    if __name__ == "__main__":
        version = "v0.9.2" # 设置版本号
        timeStartRun = time.time() # 记录启动时间
        # FBip = "43.154.99.183"
        FBip = "127.0.0.1"
        FBport = 8000
        # FBip = "124.222.6.29"
        # FBport = 3456
        os.system("del robot_old.exe")
        countdown(0.1, "§e命令系统即将开始启动")

        color(title4)
        color('§b".命令"系统社区版 - 租赁服聊天栏菜单\n".Dot" Command System Community(DotCS)\n命令系统社区版及其自带插件作者: 7912\n命令系统PRO版作者: art\n此版本为社区版, 费用将不超过0.01元/月\n本程序基于FastBuilder, 使用了2401编写的连接FastBuilder与命令系统的代码')
        color('§b用户交流群: 467443403')
        countdown(5, "§e请阅读说明")

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
                print("成功设置服号, 若设置错误可修改server.txt文件.")
            if serverPassword == "123456":
                FBconfig["serverPassword"] = input("请输入租赁服密码, 若没有, 输入任意不等于123456的六位数: ")
                if len(FBconfig["serverPassword"]) != 6 or FBconfig["serverPassword"] == "123456":
                    raise Exception("Netease server password error")
                serverPassword = FBconfig["serverPassword"]
                print("成功设置密码, 若设置错误可修改server.txt文件.")
        with open("server.txt", "w") as file:
            file.write(str(FBconfig).replace("False","false").replace("True","true").replace("'", '"'))

        FBkill()
        updateCheck()

        # 连接命令系统社区版的WebSocket服务器
        color("§eConnecting to the WebSocket server of DotCS community.")
        thread.start_new_thread(WebSocketClient, ("ws://www.dotcs.community:7912/WebSocket?",))
        while not WebSocketDotCS:
            time.sleep(0.05)
        
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


        # time.sleep(9999)
 




        # 加载插件
        color("§eLoading plugins.")
        color("§eStep -1: Loading old format plugins.")
        if not os.path.isdir("plugin/data"):
            os.mkdir("plugin/data")
        pluginlist = os.listdir("plugin")
        cmds_runcode = []
        onopen_runcode = []
        repeat1s_runcode = []
        repeat10s_runcode = []
        join_runcode = []
        prejoin_runcode = []
        left_runcode = []
        def_runcode = []
        death_runcode = []
        packet_runcode = []
        pluginLoadedNum = 0
        pluginLoadedNameList = []
        pluginIgnoredNum = 0
        pluginIgnoredNameList = []
        for filename in pluginlist:
            try:
                if os.path.isdir("plugin/%s" % filename):
                    continue
                if filename[-10:-3]=="cmdsrun":
                    color("§eNow loading: %s" % filename, replace = True)
                    plugincode = open("plugin/"+filename, "r", encoding = "utf-8")
                    if filename[0:4] == "enc_":
                        cmds_runcode.append(pluginDec(plugincode.read()))
                    else:
                        cmds_runcode.append("#%s\n%s" % (filename, plugincode.read()))
                    plugincode.close()
                    try:
                        if filename.replace("_cmdsrun.py", "") not in pluginLoadedNameList:
                            pluginLoadedNum += 1
                            pluginLoadedNameList.append(filename.replace("_cmdsrun.py", ""))
                    except Exception as err:
                        color("§4Ignored: %s, reason: %s\n" % (filename, err), replace = True)
                        pluginIgnoredNum += 1
                        pluginIgnoredNameList.append(filename+", 原因: "+str(err))
                elif filename[-11:-3]=="repeat1s":
                    color("§eNow loading: %s" % filename, replace = True)
                    plugincode = open("plugin/"+filename, "r", encoding = "utf-8")
                    if filename[0:4] == "enc_":
                        repeat1s_runcode.append(pluginDec(plugincode.read()).replace("game.ws.close()", "exitChatbarMenu()"))
                    else:
                        repeat1s_runcode.append("#%s\n%s" % (filename, plugincode.read().replace("game.ws.close()", "exitChatbarMenu()")))
                    plugincode.close()
                    try:
                        if filename.replace("_repeat1s.py", "") not in pluginLoadedNameList:
                            pluginLoadedNum += 1
                            pluginLoadedNameList.append(filename.replace("_repeat1s.py", ""))
                    except Exception as err:
                        color("§4Ignored: %s, reason: %s\n" % (filename, err), replace = True)
                        pluginIgnoredNum += 1
                        pluginIgnoredNameList.append(filename+", 原因: "+str(err))
                elif filename[-12:-3]=="repeat10s":
                    color("§eNow loading: %s" % filename, replace = True)
                    plugincode = open("plugin/"+filename, "r", encoding = "utf-8")
                    if filename[0:4] == "enc_":
                        repeat10s_runcode.append(pluginDec(plugincode.read()))
                    else:
                        repeat10s_runcode.append("#%s\n%s" % (filename, plugincode.read()))
                    plugincode.close()
                    try:
                        if filename.replace("_repeat10s.py", "") not in pluginLoadedNameList:
                            pluginLoadedNum += 1
                            pluginLoadedNameList.append(filename.replace("_repeat10s.py", ""))
                    except Exception as err:
                        color("§4Ignored: %s, reason: %s\n" % (filename, err), replace = True)
                        pluginIgnoredNum += 1
                        pluginIgnoredNameList.append(filename+", 原因: "+str(err))
                elif filename[-12:-3]=="onopenrun":
                    color("§eNow loading: %s" % filename, replace = True)
                    plugincode = open("plugin/"+filename, "r", encoding = "utf-8")
                    if filename[0:4] == "enc_":
                        onopen_runcode.append(pluginDec(plugincode.read()))
                    else:
                        onopen_runcode.append("#%s\n%s" % (filename, plugincode.read()))
                    plugincode.close()
                    try:
                        if filename.replace("_onopenrun.py", "") not in pluginLoadedNameList:
                            pluginLoadedNum += 1
                            pluginLoadedNameList.append(filename.replace("_onopenrun.py", ""))
                    except Exception as err:
                        color("§4Ignored: %s, reason: %s\n" % (filename, err), replace = True)
                        pluginIgnoredNum += 1
                        pluginIgnoredNameList.append(filename+", 原因: "+str(err))
                elif filename[-6:-3]=="def":
                    color("§eNow loading: %s" % filename, replace = True)
                    plugincode = open("plugin/"+filename, "r", encoding = "utf-8")
                    try:
                        def_runcode.append("#%s\n%s" % (filename, plugincode.read()))
                        if filename.replace("_def.py", "") not in pluginLoadedNameList:
                            pluginLoadedNum += 1
                            pluginLoadedNameList.append(filename.replace("_def.py", ""))
                    except Exception as err:
                        color("§4Ignored: %s, reason: %s\n%s\n" % (filename, err, "§c"+traceback.format_exc()), replace = True)
                        pluginIgnoredNum += 1
                        pluginIgnoredNameList.append(filename+", 原因: "+str(err))
                elif filename[-10:-3]=="prejoin":
                    color("§eNow loading: %s" % filename, replace = True)
                    plugincode = open("plugin/"+filename, "r", encoding = "utf-8")
                    if filename[0:4] == "enc_":
                        prejoin_runcode.append(pluginDec(plugincode.read()))
                    else:
                        prejoin_runcode.append("#%s\n%s" % (filename, plugincode.read()))
                    plugincode.close()
                    try:
                        if filename.replace("_prejoin.py", "") not in pluginLoadedNameList:
                            pluginLoadedNum += 1
                            pluginLoadedNameList.append(filename.replace("_prejoin.py", ""))
                    except Exception as err:
                        color("§4Ignored: %s, reason: %s\n" % (filename, err), replace = True)
                        pluginIgnoredNum += 1
                        pluginIgnoredNameList.append(filename+", 原因: "+str(err))
                elif filename[-7:-3]=="join":
                    color("§eNow loading: %s" % filename, replace = True)
                    plugincode = open("plugin/"+filename, "r", encoding = "utf-8")
                    if filename[0:4] == "enc_":
                        join_runcode.append(pluginDec(plugincode.read()))
                    else:
                        join_runcode.append("#%s\n%s" % (filename, plugincode.read()))
                    plugincode.close()
                    try:
                        if filename.replace("_join.py", "") not in pluginLoadedNameList:
                            pluginLoadedNum += 1
                            pluginLoadedNameList.append(filename.replace("_join.py", ""))
                    except Exception as err:
                        color("§4Ignored: %s, reason: %s\n" % (filename, err), replace = True)
                        pluginIgnoredNum += 1
                        pluginIgnoredNameList.append(filename+", 原因: "+str(err))
                elif filename[-7:-3]=="left":
                    color("§eNow loading: %s" % filename, replace = True)
                    plugincode = open("plugin/"+filename, "r", encoding = "utf-8")
                    if filename[0:4] == "enc_":
                        left_runcode.append(pluginDec(plugincode.read()))
                    else:
                        left_runcode.append("#%s\n%s" % (filename, plugincode.read()))
                    plugincode.close()
                    try:
                        if filename.replace("_left.py", "") not in pluginLoadedNameList:
                            pluginLoadedNum += 1
                            pluginLoadedNameList.append(filename.replace("_left.py", ""))
                    except Exception as err:
                        color("§4Ignored: %s, reason: %s\n" % (filename, err), replace = True)
                        pluginIgnoredNum += 1
                        pluginIgnoredNameList.append(filename+", 原因: "+str(err))
                elif filename[-8:-3]=="death":
                    color("§eNow loading: %s" % filename, replace = True)
                    plugincode = open("plugin/"+filename, "r", encoding = "utf-8")
                    if filename[0:4] == "enc_":
                        death_runcode.append(pluginDec(plugincode.read()))
                    else:
                        death_runcode.append("#%s\n%s" % (filename, plugincode.read()))
                    plugincode.close()
                    try:
                        if filename.replace("_death.py", "") not in pluginLoadedNameList:
                            pluginLoadedNum += 1
                            pluginLoadedNameList.append(filename.replace("_death.py", ""))
                    except Exception as err:
                        color("§4Ignored: %s, reason: %s\n" % (filename, err), replace = True)
                        pluginIgnoredNum += 1
                        pluginIgnoredNameList.append(filename+", 原因: "+str(err))
                elif filename[-9:-3]=="packet":
                    color("§eNow loading: %s" % filename, replace = True)
                    plugincode = open("plugin/"+filename, "r", encoding = "utf-8").read()
                    try:
                        int(plugincode.split("\n")[0].split("# packet: ")[1])
                    except:
                        raise Exception("packet setting error")
                    if filename[0:4] == "enc_":
                        packet_runcode.append(pluginDec(plugincode))
                    else:
                        packet_runcode.append("#%s\n%s" % (filename, plugincode))
                    try:
                        if filename.replace("_packet.py", "") not in pluginLoadedNameList:
                            pluginLoadedNum += 1
                            pluginLoadedNameList.append(filename.replace("_packet.py", ""))
                    except Exception as err:
                        color("§4Ignored: %s, reason: %s\n" % (filename, err), replace = True)
                        pluginIgnoredNum += 1
                        pluginIgnoredNameList.append(filename+", 原因: "+str(err))
                elif filename.endswith(".py"):
                    pass
                else:
                    color("§4Ignored: %s, reason: Wrong filename type.\n" % filename, replace = True)
                    pluginIgnoredNum += 1
                    pluginIgnoredNameList.append(filename+", 原因: 命名不规范.")
            except Exception as err:
                color("§4Ignored: %s, reason: %s\n%s\n" % (filename, err, "§c"+traceback.format_exc()), replace = True)
                pluginIgnoredNum += 1
                pluginIgnoredNameList.append(filename+", 原因: "+str(err))
            finally:
                pass
                # time.sleep(0.05)
        
        color("§eStep 0: Formatting old plugins.")
        needRestart = False
        pluginToTurn = [def_runcode, cmds_runcode, onopen_runcode, repeat1s_runcode, repeat10s_runcode, join_runcode, prejoin_runcode, left_runcode, death_runcode, packet_runcode]
        for i in pluginToTurn:
            for j in i:
                pluginFileName = j.split("\n", 1)[0][1:]
                pluginFileCode = j.split("\n", 1)[1]
                if pluginFileName.startswith("basic_"):
                    pluginName = "".join(pluginFileName.split("_")[:-1])
                    pluginType = pluginFileName.split("_")[-1].replace(".py", "")
                else:
                    pluginName = pluginFileName.split("_", 1)[0]
                    pluginType = pluginFileName.split("_", 1)[-1].replace(".py", "")
                if pluginType == "def":
                    pluginType = "def"
                elif pluginType == "onopenrun":
                    pluginType = "init"
                elif pluginType == "repeat1s":
                    pluginType = "repeat 1s"
                elif pluginType == "repeat10s":
                    pluginType = "repeat 10s"
                elif pluginType == "cmdsrun":
                    pluginType = "player message"
                elif pluginType == "join":
                    pluginType = "player join"
                elif pluginType == "left":
                    pluginType = "player leave"
                elif pluginType == "prejoin":
                    pluginType = "player prejoin"
                elif pluginType == "death":
                    pluginType = "player death"
                elif pluginType == "packet":
                    pluginFileName = j.split("\n", 2)[0][1:]
                    pluginFileCode = j.split("\n", 2)[2]
                    pluginType = j.split("\n", 2)[1][2:].split("_", 1)[-1].replace(".py", "")
                    pluginType = pluginType.replace(":", "")
                os.remove("plugin/%s" % pluginFileName)
                needRestart = True
                if not os.path.isfile("plugin/%s.py" % pluginName):
                    with open("plugin/%s.py" % pluginName, "w", encoding = "utf-8") as file:
                        file.write("# Author: unknown\nDescription: unknown\n\n\n\n")
                with open("plugin/%s.py" % pluginName, "a", encoding = "utf-8") as file:
                    file.write("# PLUGIN TYPE: %s\n%s\n\n\n" % (pluginType, pluginFileCode))


        if needRestart:
            exitChatbarMenu(delay = 0.01, reason = "plugin format finished.")

        color("§eStep 1: Reading plugins.")
        pluginlist = []
        for filename in os.listdir("plugin"):
            if filename.endswith(".py"):
                pluginlist.append(filename)

        for i in range(len(pluginlist)):
            filename = pluginlist[i]
            color("§e[Step 1/2][Plugin %d/%d] Now loading: %s" % (i+1, len(pluginlist), filename), replace = True, replaceByNext = True)
            with open("plugin/"+filename, "r", encoding = "utf-8") as file:
                pluginCodeList = file.read().split("# PLUGIN TYPE: ")[1:]
                pluginCodeDict = {}
                for i in pluginCodeList:
                    pluginCodeDict[i.split("\n", 1)[0]] = i.split("\n", 1)[1]
                plugin(filename, pluginCodeDict)
            time.sleep(0.1)

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
                exitChatbarMenu(delay = 60, reason = "Load plugin %s error in step 2.")
            time.sleep(0.1)
        color("§aLoaded all plugins.")

        # 启动FB
        runFB()
        timeStartFBRun = time.time()

        # 开始尝试连接
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
            revMsg()
        except Exception as err:
            color("§4连接失败, 信息:\n"+str(err))
            color("§c"+traceback.format_exc())
        finally:
            pass

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
