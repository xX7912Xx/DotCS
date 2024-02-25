import logging
from typing import Any, Coroutine, List
import edotcs 
class Plugin(edotcs.EDotCS):
    async def Player_Message(self, player: str, msg: str) -> Coroutine[Any, Any, None]:
        print(await self.Get_Player_List())
    async def Menu(self, player: str, menu: list[str]):
        await self.Say_To(player,f"真香")
    async def System_Message(self, NeedsTranslation: bool, SourceName: str, Message: str, Parameters: List[str], XUID: str, PlatformChatID: str, PlayerRuntimeID: str):
        print(NeedsTranslation, SourceName, Message, Parameters, XUID, PlatformChatID, PlayerRuntimeID)
if __name__ == "__main__":
    # EDotCS 插件端的日志级别,这个日志在EDotCS 没有启动 DEBUG 模式的情况下是无法看到的。(除非你在使用插件api模拟器)
    plugin = Plugin("饼",author="我不是art",version=[1,0,0],description="饼插件",menu_key="eat",menu_tip="有关吃大饼的功能")
    while(1):
        plugin.run()
        
        
async def Load_config(self,version:str,author:str,data:Any):
    "读取配置文件(无需担心创建文件,文件不存在会默认创建)"
    pass
async def Update_config(self,version:str,author:str,data:Any):
    "更新配置文件(无需担心创建文件,文件不存在会默认创建)"
    pass
async def Del_config(self):
    "删除配置文件(无需担心删除后无法创建,文件不存在会在调用 Load_config 时创建)"
    pass

class Data:
    def __init__(self,edotcs:edotcs.EDotCS):
        self.edotcs = edotcs
        
import os
os.listdir()
    