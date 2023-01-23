import multiprocessing
from multiprocessing.connection import PipeConnection
import threading
import subprocess
import platform
import time
from typing import IO
from . import color
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
def running(server:str="",password:str="",port:str="",Pipe:multiprocessing.Pipe=(None,None),color:str=""):
    "启动 DotCS 的进程"
    out_pipe, in_pipe = Pipe
    match platform.system():
        case "Windows":
            out = subprocess.Popen(["phoenixbuilder.exe",f"--code={server}",f"--password={password}","--no-update-check",f"--listen-external=0.0.0.0:{str(port)}","--no-readline"],stdout=subprocess.PIPE,stdin=subprocess.PIPE,stderr=subprocess.PIPE)
        case _:
            pass
    color = f"{color} {server}"
    pid = out.pid
    listens = threading.Thread(target=listen,args=(out,color,out_pipe), daemon=True)
    error_listens = threading.Thread(target=error_listen,args=(out,color), daemon=True)
    listen_input = threading.Thread(target= input_fb,args=(out,out_pipe,pid,color), daemon=True)
    listens.start()
    error_listens.start()
    listen_input.start()
    while(1):
        time.sleep(1)
        if psutil.pid_exists(pid)==False:
            match platform.system():
                case "Windows":
                    out = subprocess.Popen(["phoenixbuilder.exe",f"--code={server}",f"--password={password}","--no-update-check",f"--listen-external=0.0.0.0:{str(port)}","--no-readline"],stdout=subprocess.PIPE,stdin=subprocess.PIPE,stderr=subprocess.PIPE)
                case _:
                    pass
                
            pid = out.pid
            listens = threading.Thread(target=listen,args=(out,color), daemon=True)
            error_listens = threading.Thread(target=error_listen,args=(out,color), daemon=True)
            listens.start()
            error_listens.start()
def listen(p:subprocess.Popen[bytes],server:str="",out_pipe:PipeConnection=None):
    while p.poll() is None:
        line=p.stdout.readline().decode("utf8")
        if line=="":
            color.color(color.info_repalce(f"{server} §r"),"§4FB已退出,正在重启",info="§b   FB   §r",word_wrapping=False)
            p.kill()
            try:
                out_pipe.send({"type":"reload","message":"FB已退出"})
            except Exception as err:
                color.color(color.info_repalce(f"{server} §r"),"§4通讯引擎退出命令失败",info="§b   FB   §r",word_wrapping=False)
            break
        elif "\x1b[40;31m\x1b[40;31m ERROR \x1b[0m\x1b[0m \x1b[91m\x1b[91m"in line:
            color.color(color.info_repalce(f"{server} §r"),line,end="",info="§4   FB   §r",word_wrapping=False)
            try:
                p.stdin.write(b"\n")
            except:pass
            try:
                p.stdin.flush()
            except:pass
        else:
            color.color(color.info_repalce(f"{server} §r"),line,end="",info="§b   FB   §r",word_wrapping=False)

def error_listen(p:subprocess.Popen[bytes],server:str=""):
    while p.poll() is None:
        line=p.stderr.readline().decode("utf8")
        color.color(color.info_repalce(f"{server} §r"),line,end="",info="§b   FB   §r",word_wrapping=False)
        try:
            p.stdin.write(b"\n")
        except:pass
        try:
            p.stdin.flush()
        except:pass
        break
def input_fb(p:subprocess.Popen[bytes],out_pipe:PipeConnection,pid:int,server:str=""):
    
    while True:
        try:
            msg = out_pipe.recv()
            if psutil.pid_exists(pid)==False:
                color.color("§4尝试输入到FB中失败,原因§7:§eFB已经关闭§4,§7输入内容§7:§r",msg,info="§4   FB   §r",word_wrapping=False)
                break
            else:
                try:
                    p.stdin.write(msg.encode('utf-8'))
                    p.stdin.write(b"\r\n")
                    p.stdin.flush()
                    color.color(color.info_repalce(f"{server} §r"),msg,info="§e  FB  §r",word_wrapping=False)
                except Exception as err:
                    color.color(color.info_repalce(f"{server} §r"),f"§4尝试输入到FB中失败,原因§7:§e{err}§7:§r",info="§4   FB   §r",word_wrapping=False)
        except EOFError:
            # 当out_pipe接受不到输出的时候且输入被关闭的时候，会抛出EORFError，可以捕获并且退出子进程
            break