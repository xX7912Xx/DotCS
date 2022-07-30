version = "0.4.6"
print("robot.exe is running.")
import os
os.system("echo Loading colorful output.")
lastOutputLen = 0
lastReplace = False
connected = False
def color(text, output = True, end = "\n", replace = False):
    global lastOutputLen, lastReplace
    text = text.replace("§1", "\033[0;37;34m").replace("§2", "\033[0;37;32m").replace("§3", "\033[0;37;36m").replace("§4", "\033[0;37;31m").replace("§5", "\033[0;37;35m").replace("§6", "\033[0;37;33m").replace("§7", "\033[0;37;90m").replace("§8", "\033[0;37;2m").replace("§9", "\033[0;37;94m").replace("§a", "\033[0;37;92m").replace("§b", "\033[0;37;96m").replace("§c", "\033[0;37;91m").replace("§d", "\033[0;37;95m").replace("§e", "\033[0;37;93m").replace("§f", "\033[0;37;1m").replace("§r", "\033[0m")+"\033[0m"
    if output:
        if replace:
            text = "\r"+text+" "*(lastOutputLen-len(text))
            end = ""
            lastReplace = True
        else:
            if lastReplace:
                text = "\n"+text
            lastReplace = False
        print(text, end = end)
        l = text.replace("\r", "").replace("\n", "")
        while l[-1] == " ":
            l = l[:-1]
        lastOutputLen = len(l)+(len(l.encode())-len(l))//2
    else:
        return text
def exitChatbarMenu(killFB = True):
    global game, connected
    if connected:
        game.ws.close()
    if killFB:
        os.system("taskkill /f /im phoenixbuilder.exe 2>nul")
    sys.exit()
    exit()
color('§b".命令"系统 - 租赁服聊天栏菜单\n感谢CLP大佬提供的修改版FastBuilder程序.\n辅助处理脚本编写者: art, 7912')
color('§b用户交流群: 467443403')
import time
time.sleep(2)
print("Importing.")
import socket
import datetime
import json
import random
import websocket
import requests
from websocket import WebSocketApp
import _thread as thread
import sys
import urllib
import urllib.parse
def updateCheck():
    if not(connected):
        color("§eChecking Updates. Your version: %s" % version)
    status = requests.get("http://chatbarmenu.com/status.txt", timeout=2)
    status.encoding = "GBK"
    status = status.text.split("\r\n")
    newversion = status[0].split("version: ")[1]
    allow = status[1].split("allow: ")[1]
    if newversion != version:
        color("§eLatest version: %s, downloading." % newversion)
        time.sleep(1)
        os.system("curl --output robot_new.exe http://chatbarmenu.com/robot.exe")
        color("§aFinished, restarting.")
        exitChatbarMenu()
    else:
        if not(connected):
            color("§aYou are running the latest version.")
    if allow == "false":
        reason = status[2].split("msg: ")[1].replace(r"\n", "\n")
        color("§4%s" % reason)
        exitChatbarMenu(killFB = False)
updateCheck()
color("§eLoading plugins.")
time.sleep(0.2)
pluginlist = os.listdir("plugin")
cmds_runcode = []
onopen_runcode = []
repeat1s_runcode = []
repeat10s_runcode = []
pluginLoadedNum = 0
pluginLoadedNameList = []
pluginIgnoredNum = 0
pluginIgnoredNameList = []
for filename in pluginlist:
    try:
        if filename[-10:-3]=="cmdsrun":
            color("§eNow loading: %s" % filename, replace = True)
            plugincode = open("plugin\\"+filename, "r", encoding = "utf-8")
            cmds_runcode.append(plugincode.read())
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
            plugincode = open("plugin\\"+filename, "r", encoding = "utf-8")
            repeat1s_runcode.append(plugincode.read())
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
            plugincode = open("plugin\\"+filename, "r", encoding = "utf-8")
            repeat10s_runcode.append(plugincode.read())
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
            plugincode = open("plugin\\"+filename, "r", encoding = "utf-8")
            onopen_runcode.append(plugincode.read())
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
            plugincode = open("plugin\\"+filename, "r", encoding = "utf-8")
            code = plugincode.read()
            plugincode.close()
            try:
                exec(code)
                if filename.replace("_def.py", "") not in pluginLoadedNameList:
                    pluginLoadedNum += 1
                    pluginLoadedNameList.append(filename.replace("_def.py", ""))
            except Exception as err:
                color("§4Ignored: %s, reason: %s\n" % (filename, err), replace = True)
                pluginIgnoredNum += 1
                pluginIgnoredNameList.append(filename+", 原因: "+str(err))
        else:
            color("§4Ignored: %s, reason: Wrong filename type.\n" % filename, replace = True)
            pluginIgnoredNum += 1
            pluginIgnoredNameList.append(filename+", 原因: 命名不规范.")
    except Exception as err:
        color("§4Ignored: %s, reason: %s\n" % (filename, err), replace = True)
        pluginIgnoredNum += 1
        pluginIgnoredNameList.append(filename+", 原因: "+str(err))
    finally:
        time.sleep(0.05)
color("§aLoaded all plugins.", replace = True)
time.sleep(0.2)
color("Loading defs.")
def log(filename, text, mode = "a", encoding = None, errors = None, output = True, sendtogamewithRitBlk = False, sendtogamewithERROR = False, sendtogrp = False):#日志类
    #便捷写入文本到文件的方法, 传入文件名和要写入的文本即可, 详细参数可以参考python官方的open()的参数说明.
    #若output = True, 则在控制台中输出.
    #若sendtogamewithRitBlk = True, 则将文本发到服务器. (带有<RitleBlock> )
    #若sendtogamewithERROR = True, 则将文本发到服务器. (带有<ERROR> )
    global QQgroup
    if text[-1:] == "\n":
        text = text[:-1]
    text = text.replace("§1", "\033[0;37;34m").replace("§2", "\033[0;37;32m").replace("§3", "\033[0;37;36m").replace("§4", "\033[0;37;31m").replace("§5", "\033[0;37;35m").replace("§6", "\033[0;37;33m").replace("§7", "\033[0;37;90m").replace("§8", "\033[0;37;2m").replace("§9", "\033[0;37;94m").replace("§a", "\033[0;37;92m").replace("§b", "\033[0;37;96m").replace("§c", "\033[0;37;91m").replace("§d", "\033[0;37;95m").replace("§e", "\033[0;37;93m").replace("§f", "\033[0;37;1m").replace("§r", "\033[0m")
    if output:
        print("["+datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+"] "+text+"\033[0m")
    text = text.replace("\033[0;37;34m", "§1").replace("\033[0;37;32m", "§2").replace("\033[0;37;36m", "§3").replace("\033[0;37;31m", "§4").replace("\033[0;37;35m", "§5").replace("\033[0;37;33m", "§6").replace("\033[0;37;90m", "§7").replace("\033[0;37;2m", "§8").replace("\033[0;37;94m", "§9").replace("\033[0;37;92m", "§a").replace("\033[0;37;96m", "§b").replace("\033[0;37;91m", "§c").replace("\033[0;37;95m", "§d").replace("\033[0;37;93m", "§e").replace("\033[0;37;1m", "§f").replace("\033[0m", "§r")
    try:
        file = open(filename, mode, encoding = encoding, errors = errors)
        file.write("["+datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+"] "+text+"\n")
    except Exception as err:
        print("写入日志错误, 信息:\n"+str(err))
    finally:
        file.close()
    if sendtogamewithRitBlk:
        try:
            sendcmd(r'''/tellraw @a {"rawtext":[{"text":"<§l§6Ritle§aBlock§r> %s"}]}''' % text.replace('"', '’’').replace("'", '’'))
        except Exception as err:
            errmsg = "log()方法中sendcmd()报错, 信息:\n"+str(err)
            log("serverMsg\\"+datetime.datetime.now().strftime("%Y-%m-%d.txt"), errmsg, encoding = "gbk", errors = "ignore")
    if sendtogamewithERROR:#如果报错则执行
        try:
            sendcmd('''/tellraw @a {"rawtext":[{"text":"<§l§4ERROR§r> §c'''+text.replace('"', '’’').replace("'", '’')+'''"}]}''')
        except Exception as err:
            errmsg = "log()方法中sendcmd()报错, 信息:\n"+str(err)
            log("serverMsg\\"+datetime.datetime.now().strftime("%Y-%m-%d.txt"), errmsg, encoding = "gbk", errors = "ignore")
    if sendtogrp:
        try:
            sendtogroup("group", QQgroup, text)
        except Exception as err:
            errmsg = "log()方法中sendtogroup()报错, 信息:\n"+str(err)
            log("serverMsg\\"+datetime.datetime.now().strftime("%Y-%m-%d.txt"), errmsg, encoding = "gbk", errors = "ignore")
def tellrawText(who, dispname, text):
    #便捷执行tellraw, 传入向谁显示, 显示的玩家名, 文本即可.
    sendcmd(r'''/tellraw %s {"rawtext":[{"text":"<%s> %s"}]}''' % (who, dispname.replace('"', '’’').replace("'", '’'), text.replace('"', '’’').replace("'", '’')))
def tellrawScore(scoreboardname, targetname):
    #scoreboardname:玩家名
    #targetname ：计分板名字
    return '{"score":{"name":"%s","objective":"%s"}}' % (targetname, scoreboardname)
def repeating():
    #每秒执行一次的代码.
    print("Starting repeating thread.")
    global banlist
    while True:
        try:
            for i in repeat1s_runcode:
                try:
                    exec(i)
                except Exception as err:
                    errmsg = "repeat1s插件报错, 信息:\n"+str(err)
                    log("serverMsg\\"+datetime.datetime.now().strftime("%Y-%m-%d.txt"), errmsg, encoding = "gbk", errors = "ignore", sendtogamewithERROR = True)
        except Exception as err:
            errmsg = "repeating()方法报错, 信息:\n"+str(err)
            log("serverMsg\\"+datetime.datetime.now().strftime("%Y-%m-%d.txt"), errmsg, encoding = "gbk", errors = "ignore", sendtogamewithERROR = True)
        finally:
            time.sleep(1)
def repeating3():
    #每10秒执行一次的代码.
    print("Starting repeating3 thread.")
    while True:
        try:
            for i in repeat10s_runcode:
                try:
                    exec(i)
                except Exception as err:
                    errmsg = "repeat10s插件报错, 信息:\n"+str(err)
                    log("serverMsg\\"+datetime.datetime.now().strftime("%Y-%m-%d.txt"), errmsg, encoding = "gbk", errors = "ignore", sendtogamewithERROR = True)
            for i in allplayers:
                try:
                    int(i)
                    sendcmd('/kick "%s" §c抱歉, 因指令师技术不足, 暂不允许纯数字玩家进服.' % i)
                except:
                    pass
        except Exception as err:
            errmsg = "repeating3()方法报错, 信息:\n"+str(err)
            log("serverMsg\\"+datetime.datetime.now().strftime("%Y-%m-%d.txt"), errmsg, encoding = "gbk", errors = "ignore", sendtogamewithERROR = True)
        finally:
            time.sleep(10)
def repeating4():
    #每60秒执行一次的代码.
    print("Starting repeating4 thread.")
    while True:
        try:
            updateCheck()
        except Exception as err:
            errmsg = "repeating4()方法报错, 信息:\n"+str(err)
            log("serverMsg\\"+datetime.datetime.now().strftime("%Y-%m-%d.txt"), errmsg, encoding = "gbk", errors = "ignore", sendtogamewithERROR = True)
        finally:
            time.sleep(60)
def getTarget(sth):
    #获取对应选择器并返回列表.
    #例:
    #   a = getTarget("@a")
    #   print(a)
    #输出:
    #   ["player1", "player2", ...]
    global needToGet, target, playername, playername2
    timeStartGet = time.time()
    playername2 = playername
    target = sth
    needToGet = True
    sendcmd("/tell @s getting "+target)
    while True:
        if int(time.time() - timeStartGet) > 5:
            return ["获取超时"]
        if not(needToGet):
            playername = playername2
            return target
        time.sleep(0.2)
def loadFunc(filename, playername):
    file = open(filename, "r", encoding = "utf-8")
    ori = file.readlines()
    for i in ori:
        if i[0] == "/":
            sendcmd(i.replace("\n", "").replace("playername", playername))
        if "delay: " in i:
            time.sleep(float(i.replace("\n", "").split("delay: ")[1]))
def getStatus(statusname):
    try:
        file = open("status\\%s.txt" % statusname, "r", encoding = "utf-8", errors = "ignore")
        status = file.read()
    except:
        status = "获取失败"
        errmsg = "getStatus()方法报错, 信息:\n"+str(err)
        log("serverMsg\\"+datetime.datetime.now().strftime("%Y-%m-%d.txt"), errmsg, encoding = "gbk", errors = "ignore", sendtogamewithERROR = True)
    finally:
        try:
            file.close()
        except:
            pass
        finally:
            return status
def setStatus(statusname, status):
    try:
        file = open("status\\%s.txt" % statusname, "w", encoding = "utf-8", errors = "ignore")
        file.write(str(status))
    except Exception as err:
        status = "设置失败"
        errmsg = "setStatus()方法报错, 信息:\n"+str(err)
        log("serverMsg\\"+datetime.datetime.now().strftime("%Y-%m-%d.txt"), errmsg, encoding = "gbk", errors = "ignore", sendtogamewithERROR = True)
    finally:
        try:
            file.close()
        except:
            pass
        finally:
            return status
def cmds():
    #处理玩家使用".命令"系统的方法.
    global processing, cmds_run
    processing = True
    try:
        for i in range(1, 100):
            exec("global tp_%d, tp_%d_time, tp_%d_time_use" % (i, i, i))
        for i in cmds_runcode:
            try:
                exec(i)
            except Exception as err:
                errmsg = "cmdsrun插件报错, 信息:\n"+str(err)
                log("serverMsg\\"+datetime.datetime.now().strftime("%Y-%m-%d.txt"), errmsg, encoding = "gbk", errors = "ignore", sendtogamewithERROR = True)
        if playername in adminhigh:
            if ".exec " in msg:
                #游戏内执行Python代码
                #格式: .exec <语句>
                #例:
                #   .exec print("art")
                #后台:
                #   art
                try: #分割字符串并执行
                    exec(msg.split(".exec ")[1].replace(r"\n", "\n"))
                    tellrawText(playername, "§l§6Python§r", "已尝试执行.")
                except Exception as err:
                    errmsg = "游戏内Python报错, 信息:\n"+str(err)
                    log("serverMsg\\"+datetime.datetime.now().strftime("%Y-%m-%d.txt"), errmsg, encoding = "gbk", errors = "ignore", sendtogamewithERROR = True)
            if ".getvar " in msg: #提示游戏内的变量
                try:
                    varr = msg.split(".getvar ")[1]
                    sendmsg = "变量 "+str(varr)+" 的值是: "+str(eval(varr))
                    print(sendmsg)
                    sendcmd(r'''/tellraw @a {"rawtext":[{"text":"<§l§6Python§r> '''+sendmsg+'''"}]}''')
                except Exception as err:
                    errmsg = "游戏内Python报错, 信息:\n"+str(err)
                    log("serverMsg\\"+datetime.datetime.now().strftime("%Y-%m-%d.txt"), errmsg, encoding = "gbk", errors = "ignore", sendtogamewithERROR = True)
    except Exception as err: #程序报错了
        errmsg = "cmds()方法报错, 信息:\n"+str(err)
        log("serverMsg\\"+datetime.datetime.now().strftime("%Y-%m-%d.txt"), errmsg, encoding = "gbk", errors = "ignore", sendtogamewithERROR = True)
    finally:
        processing = False
def sendcmd(cmd):
    #租赁服执行命令的方法, 传入命令即可.
    global game
    try:
        game.ws.send('''{"post_type": "message", "message": "'''+cmd.replace('"', r'\"').replace("'", r"\'").replace('\n', r'\n').replace("\r", "").replace(r"\r", "")+'''", "message_type": "", "sender": {}}''')
    except Exception as err:
        errmsg = "sendcmd()方法报错, 信息:\n"+str(err)
        log("serverMsg\\"+datetime.datetime.now().strftime("%Y-%m-%d.txt"), errmsg, encoding = "gbk", errors = "ignore")
        exitChatbarMenu()
print("Loading classes.")
class NeteaseServerWS(object):
    #连接到FB程序.
    def __init__(self):
        print("Initing WebSocket connection.")
        super(NeteaseServerWS, self).__init__()
        self.url = "ws://127.0.0.1:5555/fastbuilder/chatlogger"
        self.ws = None

    def on_message(self, obj, revOri):
        global rev, time_old, playername, msg, needToGet, target, server, connected, processing
        rev_old = rev
        try: 
            rev = json.loads(revOri)["params"]["message"].replace("\n", "").replace("\r", "")
        except Exception as err:
            errmsg = "json.loads(revOri)报错, 信息:\n"+str(err)
            log("serverMsg\\"+datetime.datetime.now().strftime("%Y-%m-%d.txt"), errmsg, encoding = "gbk", errors = "ignore", sendtogamewithERROR = True)
        if rev != rev_old or "executing" in rev or "getting" in rev:
            if not processing:
                playername = rev.split(" ")[0].replace("[", "").replace("]", "")
                server = rev.split(" ")[-1].replace("[", "").replace("]", "")
                msg = rev.replace("["+playername+"] ", "").replace(" ["+server+"]", "")
                try:
                    playername = playername.replace(">§r", "").split("><")[1]
                except:
                    pass
                if "executing" in rev:
                    spent = time.time()-time_old
                    time_old = time.time()
                    if spent != 0:
                        tps = int(20/spent)
                        if tps <= 30:
                            sendcmd("/scoreboard players set tps main "+str(tps))
                elif "getting" in rev:
                    targString = msg.split("getting ")[1]
                    if ", " in targString:
                        target = targString.split(", ")
                    else:
                        target = []
                        target.append(targString)
                    needToGet = False
                else:
                    processing = True
                    log("serverMsg\\"+datetime.datetime.now().strftime("%Y-%m-%d.txt"), "<"+playername+">"+" "+msg, encoding = "gbk", errors = "ignore")
                    thread.start_new_thread(cmds, ())
            else:
                playername1 = rev.split(" ")[0].replace("[", "").replace("]", "")
                server1 = rev.split(" ")[-1].replace("[", "").replace("]", "")
                msg1 = rev.replace("["+playername1+"] ", "").replace(" ["+server1+"]", "")
                try:
                    playername1 = playername1.replace(">§r", "").split("><")[1]
                except:
                    pass
                if "executing" in rev:
                    spent = time.time()-time_old
                    time_old = time.time()
                    if spent != 0:
                        tps = int(20/spent)
                        if tps <= 30:
                            sendcmd("/scoreboard players set tps main "+str(tps))
                elif "getting" in rev:
                    targString = msg1.split("getting ")[1]
                    if ", " in targString:
                        target = targString.split(", ")
                    else:
                        target = []
                        target.append(targString)
                    needToGet = False
                else:
                    log("serverMsg\\"+datetime.datetime.now().strftime("%Y-%m-%d.txt"), "<"+playername1+">"+" "+msg1, encoding = "gbk", errors = "ignore")
                    tellrawText(playername1, "§l§4ERROR§r", "§c正在处理上一条信息, 请稍后重试.")

    def on_error(self, obj, err):
        if connected:
            errmsg = "WebSocket连接错误, 信息: "+str(err)
            log("serverMsg\\"+datetime.datetime.now().strftime("%Y-%m-%d.txt"), errmsg, encoding = "gbk", errors = "ignore")
            exitChatbarMenu()

    def on_close(self, obj, b, c):
        pass

    def on_open(self, obj):
        global connected
        color("§aConnected to FB program.")
        color("§eApplying onopen plugins.")
        if not(connected):
            for i in onopen_runcode:
                try:
                    exec(i)
                except Exception as err:
                    errmsg = "onopenrun插件报错, 信息:\n"+str(err)
                    log("serverMsg\\"+datetime.datetime.now().strftime("%Y-%m-%d.txt"), errmsg, encoding = "gbk", errors = "ignore")
        connected = True
        thread.start_new_thread(repeating4, ())
        time.sleep(1)
        tellrawText("@a", "§l§6System§r", "§6''.命令''系统重启完成.")
        tellrawText("@a", "§l§6System§r", "§6共加载 §l%d§r§6 个插件/函数:" % pluginLoadedNum)
        FinishedLoadingNum = 1
        for i in pluginLoadedNameList:
            tellrawText("@a", "§l§6System§r", "§6%d. %s" % (FinishedLoadingNum, i))
            FinishedLoadingNum += 1
            time.sleep(0.02)
        if pluginIgnoredNum >= 1:
            tellrawText("@a", "§l§4ERROR§r", "§c共忽略 §l%d§r§c 个插件/函数:" % pluginIgnoredNum)
            FinishedLoadingNum = 1
            for i in pluginIgnoredNameList:
                tellrawText("@a", "§l§4ERROR§r", "§c%d. %s" % (FinishedLoadingNum, i))
                FinishedLoadingNum += 1
                time.sleep(0.02)
        color("§aChatbar Menu program started successfully.")
    def console(self, *args):
        print("Starting console thread.")
        while True:
            try:
                time.sleep(1)
                input_msg = input("")
                if input_msg == "exit":
                    exitChatbarMenu()
                    break
                elif input_msg[0] == "/":
                    sendcmd(input_msg)
                elif input_msg == "list":
                    print(getTarget("@a"))
                else:
                    exec(input_msg)
            except Exception as err:
                errmsg = "console()报错, 信息:\n"+str(err)
                log("serverMsg\\"+datetime.datetime.now().strftime("%Y-%m-%d.txt"), errmsg, encoding = "gbk", errors = "ignore", sendtogamewithERROR = True)

    def start(self):
        websocket.enableTrace(False)

        self.ws = WebSocketApp(self.url,
                               on_open=self.on_open,
                               on_message=self.on_message,
                               on_error=self.on_error,
                               on_close=self.on_close)
        self.ws.run_forever()
if __name__ == '__main__':
    #初始化, 启动脚本时执行一次.
    #这里会在文件开头执行完后才会执行.
    print("Loading main.")
    global game
    print("Setting varribles.")
    rev = ""
    processing = False
    playername = ""
    target = ""
    needToGet = False
    allplayers = []
    allplayers_old = []
    print("Setting game varr.")
    game = NeteaseServerWS()
    color("§eConnecting to FB program, please wait.")
    connected = False
    retries = 1
    while not(connected) and retries <= 10:
        game.start()
        if not(connected):
            color("§4Retrying: "+str(retries)+"/10, Is it that FB program is still starting, not connected to the Netease Minecraft Server?", replace = True)
            retries += 1
    if not(connected):
        color("§4Cannot connect to FB program.")
        color("§eMaybe FB is outdated, updating FB.")
        os.system("curl --output cheat https://www.ritleblock.com/RitleBlock/others/python/NeteaseServerRobot/update/cheat.exe")
        color("§aFinished, restarting in 1800 sec.")
        os.system("timeout /t 1800")
        exitChatbarMenu()
    print("Exiting.")
    exitChatbarMenu()
