import logging
from typing import Any, Coroutine
import edotcs 
class Plugin(edotcs.EDotCS):
    async def Player_Message(self, player: str, msg: str) -> Coroutine[Any, Any, None]:
        print(await self.Get_Player_List())
    async def Menu(self, player: str, menu: list[str]):
        await self.Say_To(player,f"真香")
if __name__ == "__main__":
    # EDotCS 插件端的日志级别,这个日志在EDotCS 没有启动 DEBUG 模式的情况下是无法看到的。(除非你在使用插件api模拟器)
    plugin = Plugin("饼",author="我不是art",version=[1,0,0],description="饼插件",menu_key="eat",menu_tip="有关吃大饼的功能")
    plugin.run()