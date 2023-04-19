# Author: unknown
Description: unknown



# PLUGIN TYPE: def
tpaRequests = []
class tpa():
    def __init__(self, playersend, playerrecv, time):
        self.playersend = playersend
        self.playerrecv = playerrecv
        self.time = time
        self.start()
    def start(self):
        tellrawText(self.playersend, "§l§6Ritle§aBlock§r", "已向玩家 §l%s§r 发起传送请求, 对方有 §l%d§r 秒的时间接受请求." % (self.playerrecv, self.time))
        tellrawText(self.playerrecv, "§l§6Ritle§aBlock§r", "收到 §l%s§r 发来的传送请求, 你有 §l%d§r 秒的时间接受请求." % (self.playersend, self.time))
        tpaRequests.append(self)
    def accept(self):
        sendcmd("/tp %s %s" % (self.playersend, self.playerrecv))
        tellrawText(self.playersend, "§l§6Ritle§aBlock§r", "§l%s§r 已接受你的传送请求." % self.playerrecv)
        tellrawText(self.playerrecv, "§l§6Ritle§aBlock§r", "你已接受 §l%s§r 的传送请求." % self.playersend)
        tpaRequests.remove(self)
    def decline(self):
        tellrawText(self.playersend, "§l§6Ritle§aBlock§r", "§c§l%s§r§c 已拒绝你的传送请求." % self.playerrecv)
        tellrawText(self.playerrecv, "§l§6Ritle§aBlock§r", "§c你已拒绝 §l%s§r§c 的传送请求." % self.playersend)
        tpaRequests.remove(self)
    def outdate(self):
        tellrawText(self.playersend, "§l§6Ritle§aBlock§r", "§c你发给 §l%s§r§c 的传送请求已过期." % self.playerrecv)
        tellrawText(self.playerrecv, "§l§6Ritle§aBlock§r", "§c§l%s§r§c 发来的传送请求已过期." % self.playersend)
        tpaRequests.remove(self)



# PLUGIN TYPE: player message
if msg == ".help" or msg == ".help ":
    sendcmd("/tellraw "+playername+r''' {"rawtext":[{"text":"输入§c.tpa§r查看玩家互传(选人版)帮助"}]}''')
if msg[0:4] == ".tpa":
    if msg == ".tpa" or msg == ".tpa ":
        sendcmd("/tellraw "+playername+r""" {"rawtext":[{"text":"<§l§6Ritle§aBlock§r> \n玩家互传(选人版)  帮助菜单\n输入§c.tpa list §r查询目前的玩家传送请求\n输入§c.tpa <玩家名称> §r向对方发起传送请求\n输入§c.tpa acc §r接受对方请求, 将对方传来\n输入§c.tpa dec §r拒绝对方请求"}]}""")
    elif msg == ".tpa list" or msg == ".tpa list ":
        if len(tpaRequests) == 0:
            tellrawText(playername, "§l§6Ritle§aBlock§r", "暂无请求.")
        else:
            tpaIndex = 1
            for i in tpaRequests:
                tellrawText(playername, "§l§6Ritle§aBlock§r", "请求§l§c%d§r: §l%s§r 发送给 §l%s§r, 剩余时间: §l%d§r s" % (tpaIndex, i.playersend, i.playerrecv, i.time))
                tpaIndex += 1
    elif msg == ".tpa acc" or msg == ".tpa acc ":
        tpaBeRequested = False
        for i in tpaRequests:
            if playername == i.playerrecv:
                tpaBeRequested = True
                i.accept()
                break
        if not(tpaBeRequested):
            tellrawText(playername, "§l§4ERROR§r", "§c你没有待处理的请求.")
    elif msg == ".tpa dec" or msg == ".tpa dec ":
        tpaBeRequested = False
        for i in tpaRequests:
            if playername == i.playerrecv:
                tpaBeRequested = True
                i.decline()
                break
        if not(tpaBeRequested):
            tellrawText(playername, "§l§4ERROR§r", "§c你没有待处理的请求.")
    else:
        playerTpaFound = []
        playerTpaToSearch = msg.split(".tpa ")[1]
        for i in allplayers:
            if playerTpaToSearch == i:
                playerTpaFound = []
                playerTpaFound.append(i)
                break
            elif playerTpaToSearch in i:
                playerTpaFound.append(i)
        print(playerTpaFound)
        if len(playerTpaFound) == 0:
            tellrawText(playername, "§l§4ERROR§r", "§c未找到名称包含 §l%s§r§c 的玩家, 无法发起请求." % playerTpaToSearch)
        elif len(playerTpaFound) >= 2:
            tellrawText(playername, "§l§4ERROR§r", "§c有多名玩家名称包含 §l%s§r§c, 无法发起请求:" % playerTpaToSearch)
            playerTpaFoundIndex = 1
            for i in playerTpaFound:
                tellrawText(playername, "§l§4ERROR§r", "§l§c%d§r§c. §l%s§r§c" % (playerTpaFoundIndex, i))
                playerTpaFoundIndex += 1
        else:
            tpaSentRequest = False
            tpaRecvedRequest = False
            for i in tpaRequests:
                if playername == i.playersend:
                    tpaSentRequest = True
                if playerTpaFound[0] == i.playerrecv:
                    tpaRecvedRequest = True
            if tpaSentRequest:
                tellrawText(playername, "§l§4ERROR§r", "§c你已发过请求, 请等对方处理后或等请求过期后再试.")
            elif tpaRecvedRequest:
                tellrawText(playername, "§l§4ERROR§r", "§c对方有未处理的请求, 请等对方处理后或等请求过期后再试.")
            else:
                tpa(playername, playerTpaFound[0], 60)


# PLUGIN TYPE: repeat 1s
for i in tpaRequests:
    i.time -= 1
    #sendcmd("/titie %s actionbar 剩余时间: %d" % (i.playersend, i.time))
    if i.time <= 0:
        i.outdate()


