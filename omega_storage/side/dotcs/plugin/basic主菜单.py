# Author: unknown
Description: unknown



# PLUGIN TYPE: player message
match msg:
        case ".help" | "help" | ".帮助": #帮助命令.
            sendcmd("/tellraw "+playername+r''' {"rawtext":[{"text":"<§l§6Ritle§aBlock§r> \n帮助菜单  命令系统社区版(DotCS Community)作者: §l7912 §r"}]}''')
            sendcmd("/tellraw "+playername+r''' {"rawtext":[{"text":"输入§l.kill§r返回重生点,\n输入§l.rtp§r随机传送,\n输入§l.main§r返回主城\n输入§l.shop§r去商店\n输入§l.dp§r去地皮区\n输入§l.gm0§r改为生存模式\n输入§l.surArea§r去生存区\n输入.setsp设置重生点"}]}''')
        case ".ver" | ".version": #查看当前辅助程序版本号
            sendcmd("/tellraw "+playername+r""" {"rawtext":[{"text":"<§l§6Ritle§aBlock§r> %s"}]}""" % version)
        case ".rtp" | ".rtp " | ".随机传送": #随机传送
            x = random.randint(-100000, 100000)
            z = random.randint(-100000, 100000)
            sendcmd("/tp "+playername+" "+str(x)+" 80 "+ str(z))
            sendcmd("/tellraw "+playername+""" {"rawtext":[{"text":"<§l§6Ritle§aBlock§r> 已传送到"""+" "+str(x)+" 80 "+str(z)+""""}]}""")
        case ".dp": #去地皮
            sendcmd("/tp "+playername+ " 250250 125 250250")
            sendcmd("/tellraw "+playername+r""" {"rawtext":[{"text":"<§l§6Ritle§aBlock§r> 已传送到地皮"}]}""")
        case ".kill" | ".kill ": #自杀
            sendcmd("/kill "+playername)
        case ".main": #回主城
            sendcmd("/tp "+playername+" 14454 65 114631")
            sendcmd("/tellraw "+playername+r""" {"rawtext":[{"text":"<§l§6Ritle§aBlock§r> 传送成功."}]}""")
        case ".shop": #商店
            sendcmd("/tp "+playername+" 150003 14 150003")
            sendcmd("/tellraw "+playername+r""" {"rawtext":[{"text":"<§l§6Ritle§aBlock§r> 已传送至商店."}]}""")
        case ".gm0": #改生存模式
            sendcmd("/gamemode 0 "+playername)
            sendcmd("/tellraw "+playername+r""" {"rawtext":[{"text":"<§l§6Ritle§aBlock§r> 你的游戏模式已刷新."}]}""")
        case ".surArea": #去生存区
            sendcmd("/tp "+playername+ " 7000 202 7000")
            sendcmd("/tellraw "+playername+r""" {"rawtext":[{"text":"<§l§6Ritle§aBlock§r> 已传送"}]}""")
        case ".setsp": #重新设置出生点
            sendcmd("""/tellraw @a[name=%s, tag=mainCity] {"rawtext":[{"text":"<§l§4ERROR§r> §c主城无法设置重生点."}]}""" % playername)
            sendcmd("/execute @a[name=%s, tag=!mainCity] ~ ~ ~ /spawnpoint" % playername)
            sendcmd("""/tellraw @a[name=%s, tag=!mainCity] {"rawtext":[{"text":"<§l§6Ritle§aBlock§r> 已设置"}]}""" % playername)
        case ".restart": #退出
            if playername in adminhigh:
                tellrawText("@a", "§l§6System§r", "§6''.命令''系统正在重启.")
                exitChatbarMenu()
            else:
                tellrawText(playername, "§l§4ERROR§r", "§c权限不足.")



