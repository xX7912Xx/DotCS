# Author: unknown
Description: unknown



# PLUGIN TYPE: player message
if msg == ".admin" or msg == ".admin ":
    sendcmd("/tellraw "+playername+r''' {"rawtext":[{"text":"§r输入§b.admin tp <玩家名> §r传送到该玩家(仅管理可用)"}]}''')
if ".admin tp " in msg and msg[0:4] == ".adm":
    if playername in adminnorm or playername in adminhigh: #若玩家有协管及以上权限.
        playerTotp = msg.split(".admin tp ")[1]
        sendcmd("/tp %s %s" % (playername, playerTotp))
        tellrawText(playername, "§l§6Ritle§aBlock§r", "成功传送.")
    else: #如果玩家权限不足.
        tellrawText(playername, "§l§4ERROR§r", "§c权限组级别不够.")



