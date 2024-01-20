import random
from threading import Thread
import time
import uuid
import grpc

import logging

import grpc
import edotcs.grpc.edotcs_plugin_pb2
import edotcs.grpc.edotcs_plugin_pb2_grpc

def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    print("Will try to greet world ...")
    with grpc.insecure_channel("localhost:8080") as channel:
        Init = edotcs.grpc.edotcs_plugin_pb2_grpc.InitializeStub(channel=channel)# 初始化
        # 初始化插件权限认证
        response =Init.EDotCS_Client_New(edotcs.grpc.edotcs_plugin_pb2.EDotCS_Client_New_Request(id=0))
        new_id = response.id
        response =Init.Plugin_Name(edotcs.grpc.edotcs_plugin_pb2.Plugin_Name_Request(id=new_id))
        response =Init.License(edotcs.grpc.edotcs_plugin_pb2.License_Request(id=new_id))
        if response.license>4:
            print("插件要求过分离谱。停止运行(哪有要求代理许可证的插件啊。就现在的接口,你要代理许可证是想盗号是把)")
            return
        
        # 初始化菜单选项,这里就不测试了


        # 初始化EDotCS APi,这里需要注意:Api系列接口比listen先初始化
        Api = edotcs.grpc.edotcs_plugin_pb2_grpc.ApiStub(channel=channel)
        
        # 下面的获取 输出的应该多线程函数或者异步处理,而不是直接这么for,这里是测试
        
        def func(Say_To_Responses):
            for Say_To in Say_To_Responses:
                print("插件请求向玩家 %s 发送消息 %s",Say_To.Player.name,Say_To.message)
        
        # 创建 Thread 实例
        t1 = Thread(target=func, args=(Api.Say_To(edotcs.grpc.edotcs_plugin_pb2.Say_To_Request(id=new_id)),))
        # 初始化 listen 系列接口
        listen = edotcs.grpc.edotcs_plugin_pb2_grpc.listenStub(channel=channel)
        while(1):
            response = listen.Player_Message(edotcs.grpc.edotcs_plugin_pb2.Player_Message_Request(
                player=edotcs.grpc.edotcs_plugin_pb2.Player(uuid=str(uuid.uuid4()),name="我不是art%d" % random.randint(0,1400000)),
                message="你好,我是你女朋友%d" % random.randint(0,1400000),
                id=new_id)
                )
            
        # 完成
        # 日常运行,

if __name__ == "__main__":
    # logging.basicConfig()
    run()