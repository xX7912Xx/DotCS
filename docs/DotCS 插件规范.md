# DotCS 插件规范(适配 DotCS Go 5.0.0及其以上版本(社区版未知))
> 作者: DotCS 开发组

# 插件命名规范
插件的命名要遵守python库的命名规范
下面是不合法的插件命名:
1.py
3d.py

# 插件导入机制说明
插件的导入机制是按照命名顺序导入的

# 如果插件有前置插件咋办
请使用 from . import 文件名(没有后缀) 的方式导入前置插件

# 插件的主类应该用什么?
```python
import __main__ # 这个是必须要在开头导入的,要不然导入会失效
@__main__.plugin_load # 必写,作用是导入插件
class __init__(__main__.plugin):
    __version__             = "1.0" # 版本号,默认值是 1.0
    __doc__                 = "插件帮助文档" # 帮助文档,默认值 :""
    __author__              = "作者名" # 作者名,默认值: "未知的作者"
    __update_url__          = None # 更新链接,默认值是 None
    __license_agreement__   = "见帮助文档" # 许可协议,默认值: "见帮助文档" 
    
    def __init__(self,Name:str,Version:str,Mode:int):# 初始化操作函数!!!
        # 上述参数均是写死的模板!!!
        # Name:用户名
        # Version: DotCS 版本
        # Mode:启动模式(见文档)
        
        "初始化操作" # 这个文档帮助定义可以不写
        pass
    
    # 下面是监听 IDText 数据包的示范(均是异步处理)
    async def IDText(self,packets):#传递的是解析后的dump对象
        # 参数格式是固定的.
        pass # 监听到对应数据包后的操作
```

# 插件的API
制定中

# 示范插件: Hello World
```python
import __main__ # 这个是必须要在开头导入的,要不然导入会失效
function_cmd = __main__.function_cmd
@__main__.plugin_load # 必写,作用是导入插件
class __init__(__main__.plugin):
    __version__             = "1.0" # 版本号,默认值是 1.0
    __doc__                 = "检测到 .help 就返回信息" # 帮助文档,默认值 :""
    __author__              = "我不是Art" # 作者名,默认值: "未知的作者"
    __update_url__          = None # 更新链接,默认值是 None
    __license_agreement__   = "见帮助文档" # 许可协议,默认值: "见帮助文档" 
    
    def __init__(self,Name:str,Version:str,Mode:int):# 初始化操作函数!!!
        # 上述参数均是写死的模板!!!
        # Name:用户名
        # Version: DotCS 版本
        # Mode:启动模式(见文档)
        
        "初始化操作" # 这个文档帮助定义可以不写
        pass
    
    # 下面是监听 IDText 数据包的示范
    async def IDText(self,packets:dict):#传递的是解析后的dump对象
        # 参数格式是固定的.
        print("数据包:",packets)
        print(packets.keys())
        if packets["TextType"] ==1:
            await function_cmd.sendcmd(f"say :{packets['SourceName']}")
```
