# Author: unknown
Description: unknown



# PLUGIN TYPE: def
def ban(banplayername, bantime, why = "无原因", operator = "命令系统"):
    banTime = int(bantime)
    banStartTime = int(time.time())
    banStartTimeFormat = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(banStartTime))
    banToTime = banStartTime+banTime
    banToTimeFormat = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(banToTime))
    banRemTime = banToTime-int(time.time())
    if banRemTime > 0:
        setPlayerData("ban", banplayername, "%d+%d, %s, %s, %s" % (banStartTime, banTime, server, operator, why))
        M, S = divmod(banRemTime, 60)
        H, M = divmod(M, 60)
        D, H = divmod(H, 24)
        banRemTimeFormat = "%sDays %sHours %sMinutes %sSeconds" % (D, H, M, S)
        tellrawText("@a", "§l§4Warning§r", "§c§l%s§r§c 已被 §l%s§r§c 在服 §l%s§r§c 封禁, 已踢出\n剩余时长: §l%s§r§c\n封禁时间: §l%s§r§c\n解封时间: §l%s§r§c\n原因: §l%s§r§c" % (banplayername, operator, server, banRemTimeFormat, banStartTimeFormat, banToTimeFormat, why))
        sendcmd("/kick %s §c§l你§r§c 已被 §l%s§r§c 在服 §l%s§r§c 封禁, 已踢出\n剩余时长: §l%s§r§c\n封禁时间: §l%s§r§c\n解封时间: §l%s§r§c\n原因: §l%s§r§c" % (banplayername, operator, server, banRemTimeFormat, banStartTimeFormat, banToTimeFormat, why))



# PLUGIN TYPE: player message
if msg == ".help":
    tellrawText(playername, text = "输入§b.admin§r查看管理员菜单帮助")
if msg == ".admin":
    tellrawText(playername, "§l§6Ritle§aBlock§r", "\n管理选项 帮助菜单\n§r输入§b.admin ban <玩家名> <时间> [理由] §r封禁玩家(仅管理可用)")
if len(msg) >= 120 and not((playername in adminnorm or playername in adminhigh)):
    ban(playername, 120, "刷屏")
if ".admin ban" in msg and msg[0:4] == ".adm": #管理命令：ban的执行的内容
    if playername in adminnorm or playername in adminhigh: #若玩家有协管及以上权限.
        playerbannowtext = msg.replace(".admin ban ", "").replace("<", "").replace(">", "").split(" ", 2)
        if len(playerbannowtext) == 3: #如果输入了理由.
            ban(playerbannowtext[0], playerbannowtext[1], playerbannowtext[2], playername)
        elif len(playerbannowtext) == 2 or (len(playerbannowtext) == 3 and playerbannowtext[3] == ""): #如果没有输入理由
            ban(playerbannowtext[0], playerbannowtext[1], "无原因.", playername)
        else: #若命令语法不正确.
            tellrawText(playername, "§l§4ERROR§r", "§c缺少参数")
    else: #如果玩家权限不足.
        tellrawText(playername, "§l§4ERROR§r", "§c权限组级别不够.")



# PLUGIN TYPE: init
global banPluginLoaded
banPluginLoaded = False


# PLUGIN TYPE: repeat 10s
global banPluginLoaded
if not(banPluginLoaded):
    for i in allplayers:
        banData = getPlayerData("ban", i, writeNew = "0")
        if banData != 0:
            banTime = int(banData.split("+")[1].split(", ")[0])
            banStartTime = int(banData.split("+")[0])
            banStartTimeFormat = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(banStartTime))
            banToTime = banStartTime+banTime
            banToTimeFormat = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(banToTime))
            banRemTime = banToTime-int(time.time())
            operator = banData.split(", ", 3)[2]
            server = banData.split(", ", 3)[1]
            why = banData.split(", ", 3)[3]
            if banRemTime > 0:
                M, S = divmod(banRemTime, 60)
                H, M = divmod(M, 60)
                D, H = divmod(H, 24)
                banRemTimeFormat = "%sDays %sHours %sMinutes %sSeconds" % (D, H, M, S)
                tellrawText("@a", "§l§4Warning§r", "§c§l%s§r§c 已被 §l%s§r§c 在服 §l%s§r§c 封禁, 已踢出\n剩余时长: §l%s§r§c\n封禁时间: §l%s§r§c\n解封时间: §l%s§r§c\n原因: §l%s§r§c" % (i, operator, server, banRemTimeFormat, banStartTimeFormat, banToTimeFormat, why))
                sendcmd("/kick %s §c§l你§r§c 已被 §l%s§r§c 在服 §l%s§r§c 封禁, 已踢出\n剩余时长: §l%s§r§c\n封禁时间: §l%s§r§c\n解封时间: §l%s§r§c\n原因: §l%s§r§c" % (i, operator, server, banRemTimeFormat, banStartTimeFormat, banToTimeFormat, why))
banPluginLoaded = True



# PLUGIN TYPE: player join
banData = getPlayerData("ban", playername, writeNew = "0")
if banData != 0:
    banTime = int(banData.split("+")[1].split(", ")[0])
    banStartTime = int(banData.split("+")[0])
    banStartTimeFormat = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(banStartTime))
    banToTime = banStartTime+banTime
    banToTimeFormat = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(banToTime))
    banRemTime = banToTime-int(time.time())
    operator = banData.split(", ", 3)[2]
    server = banData.split(", ", 3)[1]
    why = banData.split(", ", 3)[3]
    if banRemTime > 0:
        M, S = divmod(banRemTime, 60)
        H, M = divmod(M, 60)
        D, H = divmod(H, 24)
        banRemTimeFormat = "%sDays %sHours %sMinutes %sSeconds" % (D, H, M, S)
        tellrawText("@a", "§l§4Warning§r", "§c§l%s§r§c 已被 §l%s§r§c 在服 §l%s§r§c 封禁, 已踢出\n剩余时长: §l%s§r§c\n封禁时间: §l%s§r§c\n解封时间: §l%s§r§c\n原因: §l%s§r§c" % (playername, operator, server, banRemTimeFormat, banStartTimeFormat, banToTimeFormat, why))
        sendcmd("/kick %s §c§l你§r§c 已被 §l%s§r§c 在服 §l%s§r§c 封禁, 已踢出\n剩余时长: §l%s§r§c\n封禁时间: §l%s§r§c\n解封时间: §l%s§r§c\n原因: §l%s§r§c" % (playername, operator, server, banRemTimeFormat, banStartTimeFormat, banToTimeFormat, why))



