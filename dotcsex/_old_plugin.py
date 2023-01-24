# DotCS Pro 旧版本插件
# 作者:去幻想乡的老art
import multiprocessing
import threading
import time
from . import conn
from . import color
import time
import json
import os

def plugin(server: str, ip: str, colors: str = "", PiPe: multiprocessing.Pipe = None):
    "DotCS 插件进程管理"

    # 检测 FB 是否启动完成
    servers = color.info_repalce(f"{colors} {server} §r")
    while (1):
        try:
            connect = conn.ConnectFB(f"{ip}")
            conn.ReleaseConnByID(connect)
            time.sleep(1)
            break
        except Exception as err:
            pass
    color.color(servers, "§aFB启动完成", info="§a plugin §r", word_wrapping=False)
    
    if os.path.isdir("plugin")==False:os.makedirs("plugin")
    if os.path.isdir(os.path.join("plugin",str(server)))==False:os.makedirs(os.path.join("plugin",str(server)))
    Plugin = _Plugin(ip, server, servers, PiPe)
    Plugin.run()
    
    # 读取插件
    while (1):
        # 获取通知,是否被堵塞
        # 如果被堵塞就结束进程
        date = Plugin.recv().recv()
        if date['type'] == "listen_error":
            Plugin.stop()
            color.color(servers, "§e正在重启插件引擎中", info="§a plugin §r")
            Plugin.run()


class _Plugin:
    "DotCS 插件系统基础类"

    def __init__(self, ip: str, server: str = None, cserver: str = None, PiPe: multiprocessing.Pipe = None):
        "插件初始化"
        self.plugins = {}
        self.ip = ip
        self.server = server
        self.conn = None
        self.conn_in_Pipe, self.conn_out_Pipe = multiprocessing.Pipe(True)
        self.cserver = cserver
        self.fb_PiPe = PiPe

    def run(self):
        "启动 conn 监听进程"
        from . import conn
        while (1):
            try:
                connect = conn.ConnectFB(f"{self.ip}")
                conn.ReleaseConnByID(connect)
                time.sleep(1)
                break
            except Exception as err:
                pass
        self.conn = multiprocessing.Process(target=listen, args=(
            self.ip, (self.conn_in_Pipe, self.conn_out_Pipe), self.cserver, self.fb_PiPe))
        self.conn.start()

    def load(self):
        "读取插件"


    def stop(self):
        self.conn.terminate()
        self.conn.join()

    def recv(self):
        return self.conn_out_Pipe


def listen(ip: str, Pipe, cserver: str, fb_Pipe: multiprocessing.Pipe = None):
    "获取 conn 的监听结果,解析由 DotCS 完成(由线程来解析 FB 的数据包的话,会出现cpu没有完全利用的情况)"

    packets_listen = [9]
    connect = ""
    last_packets_listen_time = time.time()

    def pipe_listen(conn_in_Pipe, conn_out_Pipe):
        nonlocal packets_listen, connect
        "输出获取"
        while (1):
            date = conn_in_Pipe.recv()
            match date["type"]:
                case "listen_add":  # {"type":"listen_add","id":监听数据包类型id:int}
                    if date["id"] in packets_listen:
                        conn_in_Pipe.send(
                            {"type": "error", "messags": f"{date[id]}数据包已被监听"})
                    else:
                        packets_listen.append(date["id"])
                        conn_in_Pipe.send(
                            {"type": "listen_add", "messags": f"{date[id]}数据包 已添加成功"})
                case "listen_update":
                    packets_listen = date["packets_listen"]
                    conn_in_Pipe.send(
                        {"type": "packets_listen_update", "messags": f"数据包列表信息已更新 已添加成功"})

    def fb_listen(conn_in_Pipe, fb_out_Pipe):
        while (1):
            date = fb_out_Pipe.recv()
            if date["type"] == "reload":
                conn_in_Pipe.send(
                    {"type": "listen_error", "messags": "FB进程关闭重启"})
                return

    def time_listen(conn_in_Pipe, conn_out_Pipe):
        # 引擎超时检测线程
        nonlocal last_packets_listen_time
        while time.time()-last_packets_listen_time < 30:
            time.sleep(1)
        color.color(cserver, "§4哎呀,FB是不是崩了?超时了呀,给爷重启",
                    info="§a plugin §r", word_wrapping=False)
        conn_in_Pipe.send({"type": "listen_error", "messags": "监听超时无反应"})

    pipe_listen_thread = threading.Thread(target=pipe_listen, args=Pipe)
    pipe_listen_thread.setDaemon(True)
    pipe_listen_thread.start()
    time_listen_thread = threading.Thread(target=time_listen, args=Pipe)
    time_listen_thread.setDaemon(True)
    time_listen_thread.start()
    fb_listen_thread = threading.Thread(
        target=fb_listen, args=(Pipe[0], fb_Pipe[1]))
    fb_listen_thread.setDaemon(True)
    fb_listen_thread.start()
    while (1):
        try:
            connect = conn.ConnectFB(f"{ip}")

            while True:
                try:
                    # 接收游戏数据包
                    bytesPkt = conn.RecvGamePacket(connect)
                    # 获得数据包的类型
                    packetType = conn.inspectPacketID(bytesPkt)
                    last_packets_listen_time = time.time()
                    if packetType in packets_listen:
                        load = json.loads(
                            conn.GamePacketBytesAsIsJsonStr(bytesPkt))
                        # color.color(cserver,"§a数据包内容§7:§b",load,info="§a plugin §r")
                        Pipe[0].send(
                            {"type": "new_packets", "id": packetType, "date": load})
                        del load
                        del bytesPkt
                        del packetType
                except Exception as err:
                    color.color(cserver, "§4DotCS 插件监听进程发生了问题:", str(
                        err), info="§a plugin §r", word_wrapping=False)
                    try:
                        conn.ReleaseConnByID(connect)
                    except Exception as errs:
                        color.color(cserver, "§4DotCS 在尝试释放监听接口出了问题,这可能导致内存益处:", str(
                            errs), info="§a plugin §r", word_wrapping=False)
                    # 处理两种数据包的示例,你可以自己选择要处理哪些数据包
                    Pipe[0].send({"type": "listen_error", "messags": "监听进程崩溃"})
                    return
        except Exception as err:
            color.color(cserver, "§4DotCS 插件监听进程发生了问题:", str(
                err), info="§a plugin §r", word_wrapping=False)
            Pipe[0].send({"type": "listen_error", "messags": "监听进程大崩"})
            return
