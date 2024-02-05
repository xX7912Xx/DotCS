import logging
from typing import Any, Coroutine
import edotcs 
class Plugin(edotcs.EDotCS):
    async def Player_Message(self, player: str, msg: str) -> Coroutine[Any, Any, None]:
        pass
        
    async def Menu(self, player: str, menu: list[str]):
        # print(player,menu)
        await self.Say_To(player,f"真香")
        # return await super().Menu(player, menu)
        # return super().Player_Message(player, msg)
    # 不准改初始化!!!
    # def Player_Message(self,id:int,player:edotcs.player,message:str,*kwargs,**target):
    #     # ID: EDotCS 的客户端id
    #     # 如果你想在EDotCS里面显示你的日志,就需要使用self.log方法
    #     # EDotCS 插件软件本体里面的任何消息都不会在EDotCS里面
    #     # print("<%s> %s" %(player.name,message))
    #     self.log.info("<%s> %s" %(player.name,message))
    #     print("测试")
    #     self.Api.Say_To(id,player,"你啥玩意?有资格说这话?")
    # def Player_Join(self,id:int,player:edotcs.player):
    #     self.log.info("<%s> 加入了游戏" %(player.name,))
    # def Player_Left(self,id:int,player:edotcs.player):
    #     self.log.info("<%s> 退出了游戏" %(player.name,))
    # def menu(self,id:int,plauer:edotcs.player,menu:tuple[str]):
    #     self.Api.Say_To(id,player,"你啥玩意?有资格说这话?")
if __name__ == "__main__":
    # EDotCS 插件端的日志级别,这个日志在EDotCS 没有启动 DEBUG 模式的情况下是无法看到的。(除非你在使用插件api模拟器)
    plugin = Plugin("饼",author="我不是art",version=[1,0,0],description="饼插件",menu_key="eat",menu_tip="有关吃大饼的功能")
    plugin.run()