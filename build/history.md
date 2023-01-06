# v0.11.0 更新日志
1. 重构了 color 函数, 现在 color 函数 支持了 print 的标准语法(python3.10版本)。
```python
# 旧版 color 函数 定义
def color(text: str, output: bool = True, end: str = "\n", replace: bool = False, replaceByNext: bool = False, info=" 信息 ") -> str:
    """
    在命令系统控制台输出信息
    ---
    参数:
        text: str -> 要输出的内容.
        output: bool -> 是否输出.
        end: str -> 输出时末尾的字符, 同print()中的.
        replace: bool -> 是否被下次输出覆盖.
            True: 若下次输出时 replace还是为True, 则这次输出将被下次输出覆盖, 否则不会被覆盖.
            False: 普通的输出.
        replaceByNext: bool -> 是否一定被下次输出覆盖.
            True : 这次输出将被下次输出覆盖.
            False: 普通的输出.
        info: str -> 输出内容前的反色信息.
    返回: str -> 输出
    """

# 此版本更新后的 color 函数定义
def color(*values, output: bool = True, end: str = '\n', replace: bool = False, replaceByNext: bool = False, info: str | bool = " 信息 ", sep=' ', file: TextIO = sys.stdout, flush=False, word_wrapping: bool = True, text: str = None, is_time: bool = True, end_not_replace: bool = False, no_color: int = 0, title_time: str = "[%H:%M:%S] ", **date) -> None | str:
    """
    在命令系统控制台输出信息
    默认情况下，将值打印到流或 sys.stdout。可选关键字参数：
    ---

    参数:
        values: 要输出的内容.
        text: 要输出的内容(旧版),默认不使用,如果使用就当作 只有一个参数的 values 进行处理
        file: 类似文件的对象（流）;默认为 sys.stdout。
        sep: 在值之间插入字符串，默认为空格。
        end: 字符串追加在最后一个值之后，默认换行符。
        output: bool -> 是否输出.(返回的值是 values 拼接后的值)
        replace: bool -> 将 end 值修改为 "" 并返回行首(首个输出改成了 \\r )
            True: 若下次输出时 replace 还是为True, 则这次输出将被下次输出覆盖, 否则不会被覆盖.
            False: 普通的输出.
        replaceByNext: bool -> 是否一定被下次输出覆盖.(作用与 replace 相同,权限级别更高)
            True : 将 replace 的值改为 True
            False: 不做任何影响
        info: str -> 输出内容前的反色信息.(默认使用 文本的第一个彩色字符)
        flush: 是否强制冲刷流(如果output值为 True,则会在 end 输出后执行)
        word_wrapping : bool -> 是否自动换行输出(会将所有的\n进行处理)(默认为 True)
        is_time : 是否在终端显示时间(默认为 False)
        end_not_replace : 输出的内容结尾是否不添加彩色字的重置符(默认False)
        no_color : 是否直接移除彩色字的效果(默认值为0)
            0 : 不移除
            1 : 只移除 info 
            2 : 只移除 values
            3 : 都移除
        title_time: 格式化时间 ,默认值 "[%H:%M:%S] "
    返回: None | str
```
2. 修改了 countdown 函数,现在 countdown 函数 增加了 countdown 以及 delay_color参数,countdown 参数增加了指定是倒计时的数字的颜色,默认黄色.并且增加了倒计时完成后的提示语.delay_color 则是指定了 倒计时的秒表的颜色
3. 重构了 DotCS 导入库的步骤,现在可以更加清晰的看到导入的是什么类型的库导致的导入失败
4. DotCS 社区版 工程文件 robot.py 改名为 __init__.py,现在 DotCS 社区版支持以库的形式直接导入使用
5. DotCS 社区版 现在更新源已修改成 https://uc.mcppl.art 了。
6. DotCS 社区版 使用库导入的模式所运行的不会进行更新检测
7. DotCS 社区版 现在 不再内置 bdx_work_shop 库了,现在需要使用pip install bdx_work_shop 的方式进行使用。
8. pypi版本移除了 bdx_work_shop 对7912的限制了。
9. DotCS 社区版 现在大部分与租赁服无关的函数都迁移到 dotcs_ex 库中了
10. QRcode 函数现在不再能在租赁服输出了,只保留在终端输出的功能
11. 新增 removeColorMC 函数,参数: text:str。作用:移除彩色字
12. 更新了配置文件,增加了debug模式
13. 现在 FB 的启动,DotCS 不再强制对fb的启动进行管理.您可以通过配置文件启用这一设定
14. 现在 配置文件 server.txt 已废除,server.txt 的配置将会丢到 config.json 中