# DotCS 插件事件 event 文档
> 配套 DotCS 版本: 社区版 0.12.1 专业版 5.1.0
>
> 文档作者: 去幻想乡的老art
>
> 温馨提示: DotCS 本体 python 版本是 3.10,请不要使用 3.11 及其以上版本的函数进行调试.本文档仅记录DotCS 官方的 event ,用户自定义的扩展 event 不再本文之内

| 事件名 | 解释 | 参数 |
| --- | --- | --- |
| player_say | 玩家在聊天框发言 | player : 玩家名(str类型),<br/>message : 玩家的消息(str类型)|
| player_join | 玩家加入了服务器 | player : 玩家名(str类型)|
| player_joined | 玩家即将加入服务器 | player : 玩家名(str类型)|
| player_dead | 玩家死亡 | player :玩家名(str类型),<br/>message : 死亡原因(默认不解析)(str类型)|
| reload_fb | 插件或用户主动请求重启FB时的事件 | 无参数 |
| reload_plugin | 插件或用户主动请求重启插件引擎时的事件 | 无参数 |
| reload_one_plugin | 插件主动请求重启自己的时候的事件 | name:插件路径(str) |
| cross_engine_renv | 此参数仅限pro有效,插件跨服时传递变量| 变量:未知(取决于插件发送时的变量),<br/>server: 服务器号(str类型)|
| cross_engine_player_join | 此参数仅限pro有效,其他服务器的玩家加入了服务器 | player : 玩家名(str类型),<br/>server : 服务器号(str类型)|
| cross_engine_player_joined | 此参数仅限pro有效,其他服务器的玩家即将加入服务器 | player : 玩家名(str类型),<br/>server : 服务器号(str类型)|
| cross_engine_player_dead | 此参数仅限pro有效,其他服务器的玩家死亡| player : 玩家名(str类型),<br/>message : 死亡原因(默认不解析)(str类型),<br/>server : 服务器号(str类型)|