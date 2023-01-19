import multiprocessing
import threading
import subprocess
import platform
import time
from typing import IO

import psutil
def run(server:str="",password:str="",port:str=""):
    "启动"
    match platform.system():
        case "Windows":
            out = subprocess.Popen(["phoenixbuilder.exe",f"--code={server}",f"--password={password}","--no-update-check",f"--listen-external=0.0.0.0:{str(port)}"],stdout=subprocess.PIPE,stdin=subprocess.PIPE,stderr=subprocess.PIPE)
        case _:
            pass
    return out
    # 对游戏内容进行监听
def running(server:str="",password:str="",port:str=""):
    "启动 DotCS 的进程"
    match platform.system():
        case "Windows":
            out = subprocess.Popen(["phoenixbuilder.exe",f"--code={server}",f"--password={password}","--no-update-check",f"--listen-external=0.0.0.0:{str(port)}","--no-readline"],stdout=subprocess.PIPE,stdin=subprocess.PIPE,stderr=subprocess.PIPE)
        case _:
            pass

    pid = out.pid
    listens = threading.Thread(target=listen,args=(out,), daemon=True)
    error_listens = threading.Thread(target=error_listen,args=(out,), daemon=True)
    listens.start()
    error_listens.start()
    while(1):
        time.sleep(1)
        if psutil.pid_exists(pid)==False:
            match platform.system():
                case "Windows":
                    out = subprocess.Popen(["phoenixbuilder.exe",f"--code={server}",f"--password={password}","--no-update-check",f"--listen-external=0.0.0.0:{str(port)}","--no-readline"],stdout=subprocess.PIPE,stdin=subprocess.PIPE,stderr=subprocess.PIPE)
                case _:
                    pass
                
            pid = out.pid
            listens = threading.Thread(target=listen,args=(out,), daemon=True)
            error_listens = threading.Thread(target=error_listen,args=(out,), daemon=True)
            listens.start()
            error_listens.start()
def listen(p:subprocess.Popen[bytes]):
    import subprocess
    from . import color
    while p.poll() is None:
        line=p.stdout.readline().decode("utf8")
        if line=="":
            color.color("§4FB已退出,正在重启",end="",info="§b  FB  §r",word_wrapping=False)
            p.kill()
            break
        else:
            color.color(line,end="",info="§b  FB  §r",word_wrapping=False)

def error_listen(p:subprocess.Popen[bytes]):
    import subprocess
    from . import color
    while p.poll() is None:
        line=p.stderr.readline().decode("utf8")
        color.color(line,end="",info="§4  FB  §r",word_wrapping=False)
        p.stdin.write(b"\n")
        p.stdin.flush()
        break