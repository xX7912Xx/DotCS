# DotCS 社区版的主入口文件
import os
import json
import platform
import ctypes
import multiprocessing
import time
import rich
import sys
import dynaconf
import psutil
sys.path.append(os.getcwd())
from config import settings
try:
    import dotcs_ex
except:
    from . import dotcs_ex




if __name__ =="__main__":
    multiprocessing.freeze_support()
    rich.print("[green]DotCS 社区版[/]")
    rich.print("[green]作者:万载县互联网服务工作室[/]")
    rich.print(f"[yellow]版本:{dotcs_ex.date.version}[/]")

    # 登录 DotCS 用户中心
    pass

    # 初始化配置文件
    rich.print("[yellow]租赁服号:[/]",settings.server,sep="")
    rich.print("[yellow]租赁服密码:[/]",settings.password,sep="")

    # 获取启动
    dotcs_ex.color.color("§e正在启动FB中",info="§b  FB  §r",word_wrapping=False)
    fb_= multiprocessing.Process(target=dotcs_ex.fb.running, args=(settings.server,settings.password,settings.port))
    fb_.start()

    # 开始管理插件文件夹
    os.makedirs("plugin") if os.path.isdir("plugin")==False else ""

    # 开始启动插件
    while(1):
        try:
            connect = dotcs_ex.conn.ConnectFB(f"127.0.0.1:{settings.port}")
            dotcs_ex.conn.ReleaseConnByID(connect)
            time.sleep(1)
            break
        except Exception as err:
            dotcs_ex.color.color("§e等待连接FB中",info="§b  FB  §r",word_wrapping=False)
    dotcs_ex.color.color("§aFB启动完成",info="§b  FB  §r",word_wrapping=False)
    while(1):
        time.sleep(1)

