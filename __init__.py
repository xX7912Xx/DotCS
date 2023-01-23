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
import dotcsex
import traceback, socket, datetime, time, json, random, sys, urllib, urllib.parse, platform, sqlite3, threading, struct, hashlib, shutil, base64, ctypes, collections, types, itertools, inspect, _thread as thread
sys.path.append(os.getcwd())
if os.path.join(os.getcwd(),"site-packages")==False:
    os.makedirs(os.path.join(os.getcwd(),"site-packages"))
sys.path.append(os.path.join(os.getcwd(),"site-packages"))
from config import settings




if __name__ =="__main__":
    multiprocessing.freeze_support()
    rich.print("[green]DotCS 社区版[/]")
    rich.print("[green]作者:万载县幻梦互联网服务工作室[/]")
    rich.print(f"[yellow]版本:{dotcsex.date.version}[/]")

    # 登录 DotCS 用户中心
    pass

    # 获取启动
    dotcsex.color.color("§e正在启动FB中",info="§b   FB   §r",word_wrapping=False)
    fb_out_pipe, fb_in_pipe = multiprocessing.Pipe(True)
    fb_= multiprocessing.Process(target=dotcsex.fb.running, args=(settings.server,settings.password,settings.port,(fb_out_pipe, fb_in_pipe),settings.color),daemon = True)
    fb_.start()
    # 开始管理插件文件夹
    os.makedirs("plugin") if os.path.isdir("plugin")==False else ""

    # 开始运行插件
    run = multiprocessing.Process(target = dotcsex._old_plugin.plugin,args=(settings.server,f"127.0.0.1:{settings.port}",settings.color,(fb_out_pipe, fb_in_pipe)))
    run.start()
    time.sleep(0.5)

    # 开始启动 插件进程
    while(1):
        time.sleep(1)
