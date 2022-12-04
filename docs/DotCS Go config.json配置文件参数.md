DotCS Go 版本的 config 为 json 格式,下面为 配置文件的参数以及介绍

## fbtoken_path 
**FBtoken** 文件所在路径
> 该参数被写死为 **fbtoken**

## DotCStoken
**DotCStoken** 文件所在路径
> 该参数被写死为 **DotCStoken**

## FB_UPDate
FB版本获取链接,具体效果受到 **FB_UPDate_Mode** 参数影响
| FB_UPDate_Mode 参数值  | 介绍 |
|------|------|
|0|使用 旧版本 FastBuilder网站自动更新(直接读取 version.txt) |
|1|使用 api.github.com 的方法获取最新版本 |

## FB_Download
FB软件的下载链接,具体效果受到 **FB_Download_Mode** 参数影响
| FB_Download_Mode 参数值  | 介绍 |
|------|------|
|0|使用 旧版本 FastBuilder网站自动更新(直接读取 version.txt) |
|1|使用 api.github.com 的方法获取最新版本(链接中需带有 {{version}}) |

## FB_Download_v8 
FB软件的v8版本启用性。当此参数为 `true`时，将默认下载 v8版本。
v8版本的软件体积相对非v8版本更大,对于下载速度慢的网站来说,下载时间更久
> 此参数的启用不代表一定下载 v8 版本,仅在更新时自动下载v8版本
## FB_Connect
DotCS 链接FB的链接,受 **FB_Connect_Mode** 参数影响
| FB_Connect_Mode 参数值  | 介绍 | 备注 |
|------|------| -|
|1| 免下载 FastBuilder DotCS DLL 链接模式 | 相对 `0` 来说,`DotCS` 不影响 `FB` 的启动|
|3| 免下载 FastBuilder Omega 旁加载 http 链接模式 | 该模式免下载 `DLL` 文件,但是 `url` 需自行在 **Omega** 配置文件中设置,Omega 的此参数的默认数值 `localhost:24011` |
|5| 免下载 FastBuilder FastBuilder JavaScript 链接模式 | 该模式免下载 **FastBuilder** 以及 `DLL`文件,但是对 **FastBuilder** 有`v8`版本限制<br/>同时还对 `FB_Download_v8` 有参数要求,此参数要求 `true`,要求自备 v8的ws服务端插件 |
