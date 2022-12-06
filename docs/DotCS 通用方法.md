# 变量
VERSION : DotCS 版本

# 函数

## sendcmd
```python
__main__.plugin_function.sendcmd(cmd, waitForResponse: bool = False, timeout: float | int = 1,get_return:bool=False)
```
> 执行我的世界指令,其中参数如下:
>
> cmd:执行的命令
>
> waitForResponse:(已废弃)
>
> timeout:(已废弃)
>
> get_return: 是否等待返回结果,bool类型,此参数默认为 False,此时返回的值会根据启动参数模式的影响并变化,并且返回值无意义

此方式为异步调用,例:(下面均是在异步函数内运行的,后面没声明是同步的默认异步)
```python
function_cmd = __main__.plugin_function
await d = function_cmd.sendcmd("/say 你好,世界")
print(d)
```


## sendwscmd

```python
__main__.plugin_function.sendwscmd(cmd, waitForResponse: bool = False,get_return:bool=False)
```
> 通过 ws 执行我的世界指令,其中参数如下:
>
> cmd:执行的命令
>
> waitForResponse:(已废弃)
> 
> get_return: 是否等待返回结果,bool类型,此参数默认为 False,此时返回的值会根据启动参数模式的影响并变化,并且返回值无意义

此方式为异步调用,例:(下面均是在异步函数内运行的,后面没声明是同步的默认异步)
```python
function_cmd = __main__.plugin_function
await d = function_cmd.sendwscmd("/say 你好,世界")
print(d)
```

## sendmulticmd
```python
__main__.plugin_function.sendmulticmd(cmds: list[str], waitForResponse: bool = False, timeout: float | int = 1,get_return:bool=False)
```
> sendwscmd的封装,执行多条ws命令,其中参数如下:
>
> cmds:执行的命令列表
>
> waitForResponse:(已废弃)
>
> timeout: (已废弃)
> 
> get_return: 是否等待返回结果,bool类型,此参数默认为 False,此时返回的值会根据启动参数模式的影响并变化,并且返回值无意义

此方式为异步调用,例:(下面均是在异步函数内运行的,后面没声明是同步的默认异步)
```python
function_cmd = __main__.plugin_function
await d = function_cmd.sendmulticmd(["/say 你好,世界","/say 你不好"])
for i in d:
    print(i)
```
# 类


# 库

# 事件

下面是插件的完整版模板

```python
import __main__  # 这个是必须要在开头导入的,要不然导入会失效


@__main__.plugin_load  # 必写,作用是导入插件
class __init__(__main__.plugin):
    __version__ = "1.0"  # 版本号,默认值是 1.0
    __doc__ = "插件帮助文档"  # 帮助文档,默认值 :""
    __author__ = "作者名"  # 作者名,默认值: "未知的作者"
    __update_url__ = None  # 更新链接,默认值是 None
    __license_agreement__ = "见帮助文档"  # 许可协议,默认值: "见帮助文档"

    def __init__(self, Name: str, Version: str, Mode: int):  # 初始化操作函数!!!
        # 上述参数均是写死的模板!!!
        # Name:用户名
        # Version: DotCS 版本
        # Mode:启动模式(见文档)
        "初始化操作"  # 这个文档帮助定义可以不写
        pass


    # 初始化启动后运行的函数
    async def Running(self):
        # 在 DotCS Go 初始加载插件时所运行的函数(建议不要执行有关其他插件的操作,以免 bug 发生)
        pass

    async def Dll_Mode_Running(self):
        # 在 DotCS Go 初始加载插件且为 DLL链接模式 时所运行的函数(建议不要执行有关其他插件的操作,以免 bug 发生)
        pass
    
    async def Omega_Mode_Running(self):
        # 在 DotCS Go 初始加载插件且为 omega 旁加载模式 时所运行的函数(建议不要执行有关其他插件的操作,以免 bug 发生)
        pass
    
    async def Node_js_Mode_Running(self):
        # 在 DotCS Go 初始加载插件且为 FBv8js 加载模式 时所运行的函数(建议不要执行有关其他插件的操作,以免 bug 发生)
        pass
    
    # 事件运行函数

    async def player_say(self,player,msg,title):
        # 在玩家说话时执行的数据包,其中参数如下
        # player:   玩家名
        # msg:      消息
        # title:    网易称号(如果没有就是"")
        pass

    async def Dll_Mode_player_say(self,player,msg,title):
        # 在 DotCS Go 启动模式为 DLL链接模式 时所运行的函数(建议不要执行有关其他插件的操作,以免 bug 发生)
        # 在玩家说话时执行的数据包,其中参数如下
        # player:   玩家名
        # msg:      消息
        # title:    网易称号(如果没有就是"")
        pass

    async def Omega_Mode_player_say(self,player,msg,title):
        # 在 DotCS Go 启动模式为 omega 旁加载模式 时所运行的函数(建议不要执行有关其他插件的操作,以免 bug 发生)
        # 在玩家说话时执行的数据包,其中参数如下
        # player:   玩家名
        # msg:      消息
        # title:    网易称号(如果没有就是"")
        pass

    async def Node_js_Mode_player_say(self,player,msg,title):
        # 在 DotCS Go 启动模式为 FBv8js 加载模式 时所运行的函数(建议不要执行有关其他插件的操作,以免 bug 发生)
        # 在玩家说话时执行的数据包,其中参数如下
        # player:   玩家名
        # msg:      消息
        # title:    网易称号(如果没有就是"")
        pass    




    
    # 原始数据包事件监听函数
    async def IDLogin(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDPlayStatus(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDServerToClientHandshake(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDClientToServerHandshake(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDDisconnect(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDResourcePacksInfo(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDResourcePackStack(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDResourcePackClientResponse(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDText(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDSetTime(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDStartGame(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDAddPlayer(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDAddActor(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDRemoveActor(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDAddItemActor(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDTakeItemActor(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDMoveActorAbsolute(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDMovePlayer(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDPassengerJump(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDUpdateBlock(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDAddPainting(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDTickSync(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDLevelEvent(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDBlockEvent(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDActorEvent(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDMobEffect(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDUpdateAttributes(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDInventoryTransaction(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDMobEquipment(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDMobArmourEquipment(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDInteract(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDBlockPickRequest(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDActorPickRequest(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDPlayerAction(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDHurtArmour(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDSetActorData(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDSetActorMotion(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDSetActorLink(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDSetHealth(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDSetSpawnPosition(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDAnimate(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDRespawn(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDContainerOpen(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDContainerClose(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDPlayerHotBar(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDInventoryContent(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDInventorySlot(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDContainerSetData(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDCraftingData(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDCraftingEvent(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDGUIDataPickItem(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDAdventureSettings(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDBlockActorData(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDPlayerInput(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDLevelChunk(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDSetCommandsEnabled(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDSetDifficulty(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDChangeDimension(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDSetPlayerGameType(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDPlayerList(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDSimpleEvent(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDEvent(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDSpawnExperienceOrb(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDClientBoundMapItemData(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDMapInfoRequest(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDRequestChunkRadius(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDChunkRadiusUpdated(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDItemFrameDropItem(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDGameRulesChanged(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDCamera(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDBossEvent(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDShowCredits(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDAvailableCommands(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDCommandRequest(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDCommandBlockUpdate(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDCommandOutput(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDUpdateTrade(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDUpdateEquip(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDResourcePackDataInfo(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDResourcePackChunkData(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDResourcePackChunkRequest(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDTransfer(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDPlaySound(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDStopSound(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDSetTitle(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDAddBehaviourTree(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDStructureBlockUpdate(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDShowStoreOffer(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDPurchaseReceipt(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDPlayerSkin(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDSubClientLogin(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDAutomationClientConnect(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDSetLastHurtBy(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDBookEdit(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDNPCRequest(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDPhotoTransfer(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDModalFormRequest(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDModalFormResponse(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDServerSettingsRequest(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDServerSettingsResponse(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDShowProfile(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDSetDefaultGameType(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDRemoveObjective(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDSetDisplayObjective(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDSetScore(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDLabTable(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDUpdateBlockSynced(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDMoveActorDelta(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDSetScoreboardIdentity(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDSetLocalPlayerAsInitialised(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDUpdateSoftEnum(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDNetworkStackLatency(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDScriptCustomEvent(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDSpawnParticleEffect(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDAvailableActorIdentifiers(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDNetworkChunkPublisherUpdate(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDBiomeDefinitionList(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDLevelSoundEvent(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDLevelEventGeneric(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDLecternUpdate(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDAddEntity(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDRemoveEntity(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDClientCacheStatus(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDOnScreenTextureAnimation(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDMapCreateLockedCopy(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDStructureTemplateDataRequest(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDStructureTemplateDataResponse(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDClientCacheBlobStatus(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDClientCacheMissResponse(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDEducationSettings(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDEmote(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDMultiPlayerSettings(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDSettingsCommand(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDAnvilDamage(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDCompletedUsingItem(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDNetworkSettings(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDPlayerAuthInput(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDCreativeContent(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDPlayerEnchantOptions(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDItemStackRequest(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDItemStackResponse(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDPlayerArmourDamage(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDCodeBuilder(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDUpdatePlayerGameType(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDEmoteList(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDPositionTrackingDBServerBroadcast(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDPositionTrackingDBClientRequest(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDDebugInfo(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDPacketViolationWarning(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDMotionPredictionHints(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDAnimateEntity(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDCameraShake(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDPlayerFog(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDCorrectPlayerMovePrediction(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDItemComponent(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDFilterText(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDClientBoundDebugRenderer(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDSyncActorProperty(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDAddVolumeEntity(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDRemoveVolumeEntity(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDSimulationType(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDNPCDialogue(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDEducationResourceURI(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDCreatePhoto(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDUpdateSubChunkBlocks(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDPhotoInfoRequest(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDSubChunk(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDSubChunkRequest(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDClientStartItemCooldown(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDScriptMessage(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDCodeBuilderSource(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

    async def IDPyRpc(self, packets):
        # 这是一个以数据包命名的函数,当监听到对应数据包时执行(尽管部分数据包不支持或者根本就不运行)
        pass

```
