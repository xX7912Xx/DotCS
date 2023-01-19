# DotCS 社区版的主入口文件
import os
import json
import platform
import ctypes
import multiprocessing
import time
import rich

from config import settings
try:
    import dotcs_ex
except:
    from . import dotcs_ex




if __name__ =="__main__":
    rich.print("[green]DotCS 社区版[/]")
    rich.print("[green]作者:万载县互联网服务工作室[/]")
    rich.print(f"[yellow]版本:{dotcs_ex.date.version}[/]")

    # 登录 DotCS 用户中心
    pass

    # 初始化配置文件
    rich.print("[yellow]租赁服号:[/]",settings.server,sep="")
    rich.print("[yellow]租赁服密码:[/]",settings.password,sep="")

    # 获取启动
    fb_= multiprocessing.Process(target=dotcs_ex.fb.running, args=(settings.server,settings.password,settings.port))
    fb_.start()

    # 开始管理插件文件夹
    os.makedirs("plugin") if os.path.isdir("plugin")==False else ""

    # 开始启动插件
    
    while(1):
        time.sleep(1)