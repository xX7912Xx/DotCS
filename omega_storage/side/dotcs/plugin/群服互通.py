# Author: unknown
Description: unknown



# PLUGIN TYPE: def
QQgroup = "12345678" #你的QQ群号
def sendtogroup(where, number, message):
    #使用QQ群机器人程序的api发送信息.
    if len(message) >= 200:
        message = message[:200]+"...消息长度大于200, 已省去剩余部分"
    if where == "group":
        requests.get("http://127.0.0.1:5700/send_group_msg?group_id="+str(number)+"&message="+urllib.parse.quote(message), timeout=2).text.replace("true", "True").replace("false", "False").replace("null", "None")



# PLUGIN TYPE: player message
if msg == ".help":
    tellrawText(playername, text = "输入§l.sendtogrp <信息>§r可将信息转发到§6Qgroup§r")
if ".sendtogrp " in msg: #转发文本到QQ群
    if "发到服务器" in msg: #禁止套娃
        sendcmd("/tellraw "+playername+r""" {"rawtext":[{"text":"<§l§4ERROR§r> §c禁止套娃."}]}""")
    else: #使用方法在群里发送消息.
        sendtogroup("group", QQgroup, "<"+playername+"> "+msg.split(".sendtogrp ")[1])



