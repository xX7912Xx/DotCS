# Author: unknown
Description: unknown



# PLUGIN TYPE: player message
if msg == ".help":
    tellrawText(playername, text = "输入§e.shop help§r查看商店帮助")
if msg == ".shop help":
    tellrawText(playername, "§l§6Ritle§aBlock§r", "\n商店命令 帮助菜单\n§r输入§e.shop coin §r查询金币数\n§r输入§e.shop trans tobank <存金币数> §r可将金币存入银行\n§r输入§e.shop trans frombank <取金币数> §r可将金币从银行取出")
if msg == ".shop coin":
    tellrawText(playername, "§l§6Ritle§aBlock§r", "金币数量: §l§e%d§r, 银行金币存款: §l§e%d§r" % (getScore("coin", playername), getPlayerData("coin", playername, writeNew = "0")))
if ".shop " in msg:
    shop_txt = msg.split(".shop ")[1]
    if shop_txt[0:6] == "trans ":
        trans_txt = shop_txt.split(" ")[1]
        if trans_txt == "tobank":
            coinToTrans = int(shop_txt.split(" ")[2])
            if coinToTrans > 0 and coinToTrans <= 10000000:
                coinInScore = getScore("coin", playername)
                coinInBank = getPlayerData("coin", playername, writeNew = "0")
                if coinInScore >= coinToTrans:
                    sendcmd("/scoreboard players remove %s coin %d" % (playername, coinToTrans))
                    addPlayerData("coin", playername, coinToTrans)
                    sendcmd("/tellraw "+playername+r""" {"rawtext":[{"text":"<§l§6Ritle§aBlock§r> 存金币成功, 银行余额: §l%d§r, 金币剩余余额: %d"}]}""" % (coinInBank+coinToTrans, coinInScore-coinToTrans))
                else:
                    sendcmd("/tellraw "+playername+r""" {"rawtext":[{"text":"<§l§4ERROR§r> §c金币不足, 无法存款. 你的金币余额: §l%d"}]}""" % coinInScore)
            else:
                tellrawText(playername, "§l§4ERROR§r", "§c金币数量不正确.")
        if trans_txt == "frombank":
            coinToTrans = int(shop_txt.split(" ")[2])
            if coinToTrans > 0 and coinToTrans <= 10000000:
                coinInScore = getScore("coin", playername)
                coinInBank = getPlayerData("coin", playername, writeNew = "0")
                if coinInBank >= coinToTrans:
                    addPlayerData("coin", playername, coinToTrans*(-1))
                    sendcmd("/scoreboard players add %s coin %d" % (playername, coinToTrans))
                    sendcmd("/tellraw "+playername+r""" {"rawtext":[{"text":"<§l§6Ritle§aBlock§r> 取金币成功, 银行剩余余额: §l%d§r, 金币余额: %d"}]}""" % (coinInBank-coinToTrans, coinInScore+coinToTrans))
                else:
                    sendcmd("/tellraw "+playername+r""" {"rawtext":[{"text":"<§l§4ERROR§r> §c银行余额不足, 无法取款. 你的银行余额: §l%s"}]}""" % coinInBank)
            else:
                tellrawText(playername, "§l§4ERROR§r", "§c金币数量不正确.")




