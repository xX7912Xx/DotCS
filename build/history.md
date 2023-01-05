# v0.11.0 更新日志
1. 重构了 color 函数, 现在 color 函数 支持了 print 的标准语法(python3.10版本)
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
def color(*values, output: bool = True, end: str = '\n', replace: bool = False, replaceByNext: bool = False, info:str | bool=" 信息 ", sep=' ', file: TextIO = sys.stdout, flush=False,word_wrapping : bool = True, **date) -> None | str:
    """
    在命令系统控制台输出信息
    默认情况下，将值打印到流或 sys.stdout。可选关键字参数：
    ---

    参数:
        values: 要输出的内容.
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
    返回: None | str
    """
```
2. 修改了 countdown 函数,现在 countdown 函数 增加了 countdown 以及 delay_color参数,countdown 参数增加了指定是倒计时的数字的颜色,默认黄色.并且增加了倒计时完成后的提示语.delay_color 则是指定了 倒计时的秒表的颜色
3. 重构了 DotCS 导入库的步骤,现在可以更加清晰的看到导入的是什么类型的库导致的导入失败
4. DotCS 社区版 工程文件 robot.py 改名为 __init__.py,现在 DotCS 社区版支持以库的形式直接导入使用