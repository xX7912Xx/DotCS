# DotCS 社区版的主入口文件
from config import settings
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
import http
import traceback
import socket
import datetime
import time
import json
import random
import sys
import urllib
import urllib.parse
import platform
import sqlite3
import threading
import struct
import hashlib
import shutil
import base64
import ctypes
import collections
import types
import itertools
import inspect
import _thread as thread
import traceback
import socket
import datetime
import time
import json
import random
import sys
import urllib
import urllib.parse
import platform
import sqlite3
import threading
import struct
import hashlib
import shutil
import base64
import ctypes
import collections
import types
import itertools
import inspect
import _thread as thread
from typing import Union, List, Dict, Tuple, Set
import psutil
import requests
import pymysql
import qrcode
import websocket
import brotli
import PIL
import rich.console
import Crypto.Cipher.DES3
import rich
import requests


sys.path.append(os.getcwd())
if os.path.isdir(os.path.join(os.getcwd(), "site-packages")) == False:
    os.makedirs(os.path.join(os.getcwd(), "site-packages"))
sys.path.append(os.path.join(os.getcwd(), "site-packages"))


if __name__ == "__main__":
    multiprocessing.freeze_support()
    rich.print("[green]DotCS 社区版[/]")
    rich.print("[green]作者:万载县幻梦互联网服务工作室[/]")
    rich.print(f"[yellow]版本:{dotcsex.date.version}[/]")

    # 登录 DotCS 用户中心
    pass

    # 获取启动
    dotcsex.color.color("§e正在启动FB中", info="§b   FB   §r", word_wrapping=False)
    fb_out_pipe, fb_in_pipe = multiprocessing.Pipe(True)
    fb_ = multiprocessing.Process(target=dotcsex.fb.running, args=(
        settings.server, settings.password, settings.port, (fb_out_pipe, fb_in_pipe), settings.color), daemon=True)
    fb_.start()
    # 开始管理插件文件夹
    os.makedirs("plugin") if os.path.isdir("plugin") == False else ""

    # 开始运行插件
    run = multiprocessing.Process(target=dotcsex._old_plugin.plugin, args=(
        settings.server, f"127.0.0.1:{settings.port}", settings.color, (fb_out_pipe, fb_in_pipe)))
    run.start()
    time.sleep(0.5)

    # 开始启动 插件进程
    while (1):
        time.sleep(1)
