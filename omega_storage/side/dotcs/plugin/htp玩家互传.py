# Author: unknown
Description: unknown



# PLUGIN TYPE: def
for i in range(1, 100):
    exec('''global tp_%d\ntp_%d = "当前位无人"''' % (i, i))
    exec('''global tp_%d_time\ntp_%d_time = 0''' % (i, i))
    exec('''global tp_%d_time_use\ntp_%d_time_use = False''' % (i, i))



# PLUGIN TYPE: player message
if msg == ".help":
    tellrawText(playername, text = "输入§a.htp§r 查看玩家互传帮助")
if msg == ".htp":
    tellrawText(playername, "§l§6Ritle§aBlock§r", "\n玩家互传  帮助菜单\n输入§a.htp list §r查询目前的玩家互传列表\n输入§a.htp tp <数字> §r传送到目标玩家\n输入§a.htp totp §r发起传送命令\n输入§a.htp detotp §r取消发起传送命令")
if msg[0:5] == ".htp " and msg != ".htp ":
    htp_txt=""
    for i in msg[5:]:
        if i == "" or i == " ":
            break
        else:
            htp_txt += i
    if htp_txt == "tp": #执行tp传送命令
        htp_txt=""
        for i in msg[8:]:
            if i == "":
                break
            elif i ==" ":
                break
            else:
                htp_txt+=i
        match htp_txt:
            case x:
                if int(x) >= 1 or int(x) <= 100:
                    if eval("tp_"+x) == "当前位无人":
                        sendcmd("/tellraw "+playername+r""" {"rawtext":[{"text":"<§l§4ERROR§r> §c当前互传位暂无玩家, 请检查对方是否重置或正好倒计时结束."}]}""")
                    else:
                        sendcmd("/tp "+playername+" "+eval("tp_"+x))
                        sendcmd("""/tellraw @a {"rawtext":[{"text":"<§l§6Ritle§aBlock§r> §l"""+playername+"""§r 传送到了 §l"""+eval("tp_"+x)+"""§r 身边."}]}""")
                else:
                    sendcmd("/tellraw "+playername+r""" {"rawtext":[{"text":"<§l§4ERROR§r> §c该栏位不存在."}]}""")
    elif htp_txt =="totp":
        发过互传 = False
        for i in range(1, 100):
            if eval("tp_"+str(i)) == playername:
                sendcmd("/tellraw "+playername+r""" {"rawtext":[{"text":"<§l§4ERROR§r> §c你已经发送过玩家互传了!"}]}""")
                发过互传 = True
                break
        if not 发过互传:
            互传位已满 = True
            for i in range(1, 100):
                if eval("tp_"+str(i)) == "当前位无人":
                    exec("global tp_"+str(i)+"\ntp_"+str(i)+" = playername")
                    exec("global tp_"+str(i)+"_time"+"\ntp_"+str(i)+"_time = 60")
                    exec("global tp_"+str(i)+"_time_use"+"\ntp_"+str(i)+"_time_use = True")
                    sendcmd("/tellraw "+playername+r""" {"rawtext":[{"text":"<§l§6Ritle§aBlock§r> 玩家互传§l发起成功§r，你的互传位：§l"""+str(i)+"""§r，有效时间：60s"}]}""")
                    sendcmd("""/tellraw @a[name=!"""+playername+"""] {"rawtext":[{"text":"<§l§6Ritle§aBlock§r> §l"""+playername+""" §r发起了§l玩家互传§r，他的互传位：§l"""+str(i)+"""§r，有效时间:60s\\n输入§a.htp tp """+str(i)+"""§r进行传送"}]}""")
                    互传位已满 = False
                    break
            if 互传位已满:
                sendcmd("/tellraw "+playername+r""" {"rawtext":[{"text":"<§l§4ERROR§r> §c玩家互传当前位已满, 请稍后再试."}]}""")
    elif htp_txt =="detotp":
        取消成功 = False
        for i in range(1, 100):
            if eval("tp_"+str(i)) == playername:
                exec('''global tp_'''+str(i)+'''\ntp_'''+str(i)+''' = "当前位无人"''')
                exec("global tp_"+str(i)+"_time"+"\ntp_"+str(i)+"_time = 0")
                sendcmd("/tellraw "+playername+r""" {"rawtext":[{"text":"<§l§6Ritle§aBlock§r> 已取消玩家互传."}]}""")
                取消成功 = True
                break
        if not 取消成功:
            sendcmd("/tellraw "+playername+r""" {"rawtext":[{"text":"<§l§4ERROR§r> §c取消失败, 你可能没有发送过玩家互传, 或者是刚好重置了."}]}""")

    elif htp_txt =="list":
        sendcmd("/tellraw "+playername+r""" {"rawtext":[{"text":"<§l§6Ritle§aBlock§r> "}]}""")
        显示成功 = False
        for i in range(1, 100):
            if eval("tp_"+str(i)) != "当前位无人":
                sendcmd("/tellraw "+playername+r""" {"rawtext":"""+"""[{"text":"输入§a.htp tp """+str(i)+"""§r传送到玩家 §l"""+eval("tp_"+str(i))+"§r (剩余有效时间: §l"+str(eval("tp_"+str(i)+"_time"))+" §rs)"+""""}]}""")
                显示成功 = True
        if not 显示成功:
            sendcmd("/tellraw "+playername+r""" {"rawtext":[{"text":"暂时无传送请求."}]}""")
    elif htp_txt =="help":
        sendcmd("/tellraw "+playername+r""" {"rawtext":[{"text":"<§l§6Ritle§aBlock§r> \n玩家互传  帮助菜单\n输入§a.htp list §r查询目前的玩家互传列表\n输入§a.htp tp <数字> §r传送到目标玩家\n输入§a.htp totp §r发起传送命令\n输入§a.htp detotp §r取消发起传送命令"}]}""")
    else:
        sendcmd("/tellraw "+playername+""" {"rawtext":[{"text":"<§l§4ERROR§r> §c语法错误! 目标命令"""+htp_txt+"""不存在"}]}""")



# PLUGIN TYPE: repeat 1s
#玩家互传剩余有效时间计时.
for i in range(1, 100):
    exec("global tp_%d, tp_%d_time, tp_%d_time_use" % (i, i, i))
    if eval("tp_"+str(i)+"_time") > 0:
        exec("global tp_"+str(i)+"_time"+"\ntp_"+str(i)+"_time -= 1")
    if eval("tp_"+str(i)+"_time") <= 0 and eval("tp_"+str(i)+"_time_use") == True:
        sendcmd("""/tellraw """+eval("tp_"+str(i))+""" {"rawtext":[{"text":"<§l§6Ritle§aBlock§r> §c你发起的玩家互传时间已到，如需继续，请重新发起"}]}""")
        exec("global tp_"+str(i)+"\ntp_"+str(i)+" = '当前位无人'")
        exec("global tp_"+str(i)+"_time_use"+"\ntp_"+str(i)+"_time_use = False")



