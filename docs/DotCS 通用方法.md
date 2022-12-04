# 变量
VERSION : DotCS 版本

# 函数


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
await function_cmd.sendcmd("/say 你好,世界")
```
# 类


# 库