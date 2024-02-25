from typing import Any, Coroutine
import edotcs
class Plugin(edotcs.EDotCS):
    async def Player_Message(self, player: str, msg: str) -> Coroutine[Any, Any, None]:
        if msg == "你好":
            await self.Say_To(player, "你好呀！")
        
if __name__ == "__main__":
    # EDotCS 插件端的日志级别,这个日志在EDotCS 没有启动 DEBUG 模式的情况下是无法看到的。(除非你在使用插件api模拟器)
    plugin = Plugin("你好",author="我不是art",version=[1,0,0])
    plugin.run()

    # 在服内有玩家说 "你好" 这个消息时，插件端会自动回复 "你好呀！"
    