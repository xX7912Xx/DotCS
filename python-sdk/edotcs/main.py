import asyncio
from typing import Any
from . import error
import grpc
from edotcs import log
from edotcs.grpc import edotcs_plugin_pb2_grpc
from edotcs.server.server import _configure_health_server
from edotcs.types import player
from . import path as _path
from . import grpc as edotcs_grpc
class EDotCS:
    def __init__(self,name:str,author:str,ip:str="[::]",port:int=8080,is_sky:bool=False):
        """
        启动 EDotCS 插件(建议继承EDotCS类来修改函数)
        ================
        ip: 插件ip(默认0.0.0.0)
        port: 插件端口(在不是由EDotCS启动的场景下,端口默认为8080)
        is_sky: 是否为云端插件(如果是,则在客户端连接插件时的错误改为断开连接而不是结束程序)(默认 False)
        """
        self.author = author
        self.name = name
        self.ip = ip
        self.port = _path._get_port()
        self.port = port if self.port==0 else self.port
        self.log = log.log()
        self.loop: asyncio.AbstractEventLoop = asyncio.get_event_loop()
        self.Initialize :Initialize = Initialize(self)
        self.listen :listen = listen(self)
        self.Api :Api = Api(self)
        self.server = grpc.aio.server()
        self.is_key = is_sky
        self.edotcs_dict = {}
        if self.name =="":
            raise error.EDotCS_Plugin_Name_Error("插件必须要有名字!!!")
    def run(self, *args: Any, **kwargs: Any) -> None:
        """
        插件启动

        注意:
          这个函数必须是最后一个调用的函数，因为它是阻塞的。这意味着事件的注册或在此函数调用之后调用的任何内容在它返回之前不会执行。
          如果想获取协程对象，可以使用`start`方法执行服务, 如:
        ```
        async with Client as c:
            c.start()
        ```
        """

        async def runner():
            async with self:
                await self.start(*args, **kwargs)
                # print("测试正常运行")

        try:
            self.loop.run_until_complete(runner())
        except KeyboardInterrupt:
            return
    async def start(self):
        "EDotCS 插件启动"
        
        # 插件SDK 初始化
        edotcs_plugin_pb2_grpc.add_InitializeServicer_to_server(self.Initialize,self.server)
        edotcs_plugin_pb2_grpc.add_ApiServicer_to_server(self.Api,self.server)
        edotcs_plugin_pb2_grpc.add_listenServicer_to_server(self.listen,self.server)
        _configure_health_server(self.server)
        # helloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
        # listen_addr = "[::]:50051"
        self.server.add_insecure_port("%s:%s"%(self.ip,self.port))
        # logging.info("Starting server on %s", listen_addr)
        await self.server.start()
        await self.server.wait_for_termination()
    async def say_to(self,player:player,message:str):
        "在租赁服中对玩家发送一条消息"
        pass
    async def __aenter__(self):
        print('entering context')

    async def __aexit__(self, exc_type, exc, tb):
        print('exiting context')

class Initialize(edotcs_grpc.edotcs_plugin_pb2_grpc.InitializeServicer):
    def __init__(self,edotcs:EDotCS):
        self.edotcs = edotcs
    async def Plugin_Name(self, request, context):
        if context in self.edotcs.edotcs_dict:
            print("同1用户")
        else:
            print("非同1用户")
            print(context)
            self.edotcs.edotcs_dict[context] = {}
        return edotcs_grpc.edotcs_plugin_pb2.Plugin_Name_Reply(name=self.edotcs.name,author=self.edotcs.author)
    async def License(self, request, context):
        if context in self.edotcs.edotcs_dict:
            print("同1用户")
        else:
            print("非同1用户")
            print(context)
            self.edotcs.edotcs_dict[context] = {}
        return edotcs_grpc.edotcs_plugin_pb2.License_Reply(license=1)
class listen(edotcs_grpc.edotcs_plugin_pb2_grpc.listenServicer):
    def __init__(self,edotcs:EDotCS):
        self.edotcs = edotcs
class Api(edotcs_grpc.edotcs_plugin_pb2_grpc.ApiServicer):
    def __init__(self,edotcs:EDotCS):
        self.edotcs = edotcs

