import asyncio
import time
from typing import Any
import uuid

from edotcs.types.api import edotcs_app
from . import error
import grpc
from edotcs import log, tool
from edotcs.grpc import edotcs_plugin_pb2_grpc
from edotcs.server.server import _configure_health_server
from edotcs.types import player
from . import path as _path
from . import grpc as edotcs_grpc
import queue
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
        self.raw_Initialize :raw_Initialize = raw_Initialize(self)
        self.raw_listen :raw_listen = raw_listen(self)
        self.raw_Api :raw_Api = raw_Api(self)
        self.server = grpc.aio.server()
        self.is_key = is_sky
        self.edotcs_dict = tool.ExpireDict()
        self.edotcs_dict.expire_time = 360
        self.ids = 0

        self.Api = Api(self)
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
        edotcs_plugin_pb2_grpc.add_InitializeServicer_to_server(self.raw_Initialize,self.server)
        edotcs_plugin_pb2_grpc.add_ApiServicer_to_server(self.raw_Api,self.server)
        edotcs_plugin_pb2_grpc.add_listenServicer_to_server(self.raw_listen,self.server)
        _configure_health_server(self.server)
        # helloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
        # listen_addr = "[::]:50051"
        self.server.add_insecure_port("%s:%s"%(self.ip,self.port))
        # logging.info("Starting server on %s", listen_addr)
        await self.server.start()
        await self.server.wait_for_termination()
    def say_to(self,edotcs_id,player:player,message:str):
        "在租赁服中对玩家发送一条消息"
        # 然而这不是异步函数,因为他的作用只是发送个命令而已

    async def __aenter__(self):
        print('entering context')

    async def __aexit__(self, exc_type, exc, tb):
        print('exiting context')
class raw_Initialize(edotcs_grpc.edotcs_plugin_pb2_grpc.InitializeServicer):
    def __init__(self,edotcs:EDotCS):
        self.edotcs = edotcs
    async def EDotCS_Client_New(self, request, context):
        if request.id == 0:
            self.edotcs.ids +=1
            id = self.edotcs.ids
            self.edotcs.edotcs_dict[id] = edotcs_app()
        else:
            if self.edotcs.ids > request.id:
                self.edotcs.ids = request.id+1
            id = request.id
            self.edotcs.edotcs_dict[id] = edotcs_app()
        return edotcs_grpc.edotcs_plugin_pb2.EDotCS_Client_New_Reply(id=id)
    async def Plugin_Name(self, request, context):
        if request.id == 0:
            await context.abort(grpc.StatusCode.INVALID_ARGUMENT, "未完成edotcs客户端初始化认证")
        elif request.id not in self.edotcs.edotcs_dict:
            await context.abort(grpc.StatusCode.INVALID_ARGUMENT, "未完成edotcs客户端初始化认证")
        return edotcs_grpc.edotcs_plugin_pb2.Plugin_Name_Reply(name=self.edotcs.name,author=self.edotcs.author)
    async def License(self, request, context):
        if request.id == 0:
            await context.abort(grpc.StatusCode.INVALID_ARGUMENT, "未完成edotcs客户端初始化认证")
        elif request.id not in self.edotcs.edotcs_dict:
            await context.abort(grpc.StatusCode.INVALID_ARGUMENT, "未完成edotcs客户端初始化认证")
        return edotcs_grpc.edotcs_plugin_pb2.License_Reply(license=1)

count = 0
start_time = time.time()
class raw_listen(edotcs_grpc.edotcs_plugin_pb2_grpc.listenServicer):
    def __init__(self,edotcs:EDotCS):
        self.edotcs = edotcs
    async def Player_Message(self, request, context):
        global count,start_time
        count += 1
        if count ==1:
            start_time = time.time()
        if count % 1000 ==0:
            print(count,time.time()-start_time,"秒")
        if request.id == 0:
            await context.abort(grpc.StatusCode.INVALID_ARGUMENT, "未完成edotcs客户端初始化认证")
        elif request.id not in self.edotcs.edotcs_dict:
            await context.abort(grpc.StatusCode.INVALID_ARGUMENT, "未完成edotcs客户端初始化认证")
        await self.edotcs.player_message(id=request.id,player=player(uuid= uuid.UUID(request.player.uuid),name=request.player.name),message=request.message)
        return edotcs_grpc.edotcs_plugin_pb2.Player_Message_Reply()
class raw_Api(edotcs_grpc.edotcs_plugin_pb2_grpc.ApiServicer):
    def __init__(self,edotcs:EDotCS):
        self.edotcs = edotcs
    async def Say_To(self, request, context):
        app:edotcs_app=self.edotcs.edotcs_dict[request.id]
        app.Api.Say_To.is_use=True
        while(1):
            if app.Api.Say_To.queue!=[]:
                yield app.Api.Say_To.queue.pop(0)
            else:
                await asyncio.sleep(0.1)
        # return super().Say_To(request, context)


class Api:
    def __init__(self,edotcs:EDotCS):
        self.edotcs = edotcs
    def Say_To(self,id:int,player:player,message:str):
        if id not in self.edotcs.edotcs_dict:
            raise error.EDotCS_Not_Find_Client_Error("此EDotCS客户端未连接到此插件")
        app:edotcs_app=self.edotcs.edotcs_dict[id]
        if app.Api.Say_To.is_use==False:
            raise error.EDotCS_Plugin_No_Use_Say_To("此edotcs客户端未启用该接口。")
        app.Api.Say_To.queue.append(edotcs_grpc.edotcs_plugin_pb2.Say_To_Reply(Player=edotcs_grpc.edotcs_plugin_pb2.Player(uuid=str(player.uuid),name=player.name),message = message))
