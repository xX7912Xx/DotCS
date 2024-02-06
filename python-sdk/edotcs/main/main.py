import asyncio
import os
from typing import Any
from loguru import logger
import aiohttp
from .. import grpc
from . import path as _path
from .. import type
class EDotCS:
    def __init__(self,name:str,author:str,ip:str="127.0.0.1:8080",menu_key="",menu_tip="",version=[1,0,0],description="",*tuple,**kwargs):
        """
        插件初始化

        :param name: 插件名称
        :param author: 插件作者
        :param ip: 插件IP地址
        :param menu_key: 插件菜单快捷键
        :param menu_tip: 插件菜单提示信息
        :param version: 插件版本
        :param description: 插件介绍
        :param tuple: 插件运行所需的其他参数
        :param kwargs: 插件运行所需的其他参数
        """

        # 定义插件名称、作者、IP、端口、菜单快捷键、菜单提示信息
        self.name = name
        self.author = author
        self.ip = _path._get_ip_port()
        self.ip  = ip if self.ip =="" else self.ip 
        self.menu_key = menu_key
        self.menu_tip = menu_tip
        self.version = version
        self.description = description

        # 定义插件运行状态
        self.running = False

        # 定义插件运行所需的其他参数
        self.args = tuple
        self.kwargs = kwargs

        self.loop = asyncio.get_event_loop()
        # 接口初始化部分
        self.logger = logger

        self.session = aiohttp.ClientSession("http://{ip}".format(ip=self.ip))
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
        await self.sendcmd("你好")
        await self.listen()
    def log_init(self):
        "初始化日志"
        self.logger.info("初始化日志接口")
        LOG_DIR = os.path.expanduser("./logs/%s"% self.name)
        LOG_FILE = os.path.join(LOG_DIR, "%s_runlog_{time}.log" % self.name)
        if os.path.isdir(LOG_DIR)==False:
            self.logger.info("日志文件夹缺失,已自动创建")
            os.makedirs(LOG_DIR)
        logger.add(LOG_FILE, rotation = "16MB")
        self.logger.success("日志初始化成功")
    async def __aenter__(self):
        self.log_init()

    async def __aexit__(self, exc_type, exc, tb):
        await self.session.close()
        self.logger.info("插件退出")
    # 应用接口
    async def Player_Message(self,player:str,msg:str)->None:
        "接收MC消息"
        # self.logger.info("<%s> %s"%(player,msg))
    async def Player_join(self,player:str)->None:
        "接收MC加入服务器消息"
        #self.logger.info("加入服务器数据包",str(player))
    async def Player_Left(self,player:str)->None:
        "接收MC退出服务器消息"
    async def Menu(self,player:str,menu:list[str]):
        "接受MC菜单消息"
        pass
        #self.logger.info("退出服务器数据包",str(player))
    # 接口
    async def sendcmd(self,cmd:str)->aiohttp.ClientResponse:
        "发送MC指令,目前没有返回值"
        async with self.session.post("/dotcs/v8/cmd",data=grpc.edotcs_pb2.SendCmd(Command=cmd).SerializeToString()) as response:
            return response
    async def sendwscmd(self,cmd:str)->aiohttp.ClientResponse:
        "发送MC指令(ws方式),目前没有返回值"
        async with self.session.post("/dotcs/v8/wscmd",data=grpc.edotcs_pb2.SendCmd(Command=cmd).SerializeToString()) as response:
            return response
    async def Say_To(self,player:str,msg:str)->aiohttp.ClientResponse:
        "发送MC私聊消息"
        async with self.session.post("/dotcs/v8/sayto",data=grpc.edotcs_pb2.Say_To(Player=player,Message=msg).SerializeToString()) as response:
            return response
    async def Say_To_All(self,msg:str)->aiohttp.ClientResponse:
        "发送MC全体消息"
        async with self.session.post("/dotcs/v8/sayto",data=grpc.edotcs_pb2.Say_To(Player="@a",Message=msg).SerializeToString()) as response:
            return response
    async def Get_Player_List(self)->type.get_player.GetPlayerList:
        "获取MC玩家列表"
        async with self.session.post("/dotcs/v8/getplayerlist",data=grpc.edotcs_pb2.Get_Online_Player_Info().SerializeToString()) as response:
            data = await response.read()
            message = grpc.edotcs_pb2.Return_Online_Player_Info()
            message.ParseFromString(data)
            player_list = []
            if message.Is_True:
                for player in message.Players:
                    player_list.append(type.get_player.Player(name=player.Player,uuid=player.UUID))
            return_data = type.get_player.GetPlayerList(success=message.Is_True,message=message.message,players=player_list)
            return return_data
    async def Get_Player(self,player:str)->type.get_player.GetPlayer:
        "获取玩家信息"
        async with self.session.post("/dotcs/v8/getplayer",data=grpc.edotcs_pb2.Get_Player_Info(Player=player).SerializeToString()) as response:
            data = await response.read()
            message = grpc.edotcs_pb2.Return_Player_Info()
            message.ParseFromString(data)
            return_data = type.get_player.GetPlayer(success=message.Is_True,message=message.message,player=type.get_player.Player(name=message.Player.Player,uuid=message.Player.UUID))
            return return_data
    
    async def listen(self):
        "监听 EDotCS 客户端 发送的数据包"

        async with self.session.ws_connect("/dotcs/v8/") as ws:
            #---gtj 一定注意中文发送前要采用ensure_ascii=False
            # jsondata=json.dumps(params,ensure_ascii=False)
            # print('send jsondata:',type(jsondata),jsondata,type(params),params)
            # await ws.send_json(jsondata)
            # message Plugin {
            #     string Name =1;// 插件名称
            #     string Author =2;//插件作者
            #     Version Version=3;//插件版本
            #     optional string recommendation=4;//插件介绍
            #     optional string menu_word=5;// 插件菜单关键词(以htp为例, .htp )
            #     optional string menu_recommendation=6;// 插件菜单关键词介绍
            # }           
            init_packet = grpc.edotcs_pb2.Plugin(Name=self.name,Author=self.author,Version=grpc.edotcs_pb2.Version(Major=self.version[0],Minor=self.version[1],Patch=self.version[2]),recommendation=self.description,menu_word=self.menu_key,menu_recommendation=self.menu_tip)
            await ws.send_bytes(b'\x00'+init_packet.SerializeToString())
            self.logger.info("开始监听消息")
            async for msg in ws:
                # print( msg)
                if msg.type == aiohttp.WSMsgType.BINARY:
                    match msg.data[0]:
                        case 1:
                            message = grpc.edotcs_pb2.Player_Message()
                            message.ParseFromString(msg.data[1:],)
                            self.logger.info("<%s> %s"%(message.Player,message.Message))
                            await self.Player_Message(message.Player,message.Message)
                        case 2:
                            message = grpc.edotcs_pb2.Player_join()
                            message.ParseFromString(msg.data[1:])
                            await self.Player_join(message.Player)
                            self.logger.info("%s 加入了服务器"%(message.Player))
                        case 3:
                            message = grpc.edotcs_pb2.Player_Left()
                            message.ParseFromString(msg.data[1:])
                            await self.Player_Left(message.Player)
                            self.logger.info("%s 退出了服务器"%(message.Player))
                        case 4:
                            message = grpc.edotcs_pb2.Menu()
                            message.ParseFromString(msg.data[1:])
                            if message.word[0]== self.menu_key:
                                await self.Menu(message.Player,message.word[1:])
                        case _:
                            self.logger.error("未知数据包类型:",msg.data[0])
                    # self.logger.info(msg.data)
                    # await callback(msg.data)
                elif msg.type == aiohttp.WSMsgType.CLOSED:
                    break
                elif msg.type == aiohttp.WSMsgType.ERROR:
                    break
            await ws.close()
        # a = grpc.edotcs_pb2.SendCmd(Command=cmd).SerializeToString() # 序列化
        # b = a
        # c = str(a)
        # # print(b,c)
        # 
        # LogLogGroupList = grpc.edotcs_pb2.SendCmd()
        # LogLogGroupList.ParseFromString(b)
        # print(str(LogLogGroupList))