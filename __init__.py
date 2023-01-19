# DotCS 社区版的主入口文件
import os
import json
import platform
import ctypes

import rich

from config import settings
try:
    import dotcs_ex
except:
    from . import dotcs_ex


rich.print("[green]DotCS 社区版[/]")
rich.print("[green]作者:万载县互联网服务工作室[/]")
rich.print(f"[yellow]版本:{dotcs_ex.date.version}[/]")

# 登录 DotCS 用户中心
pass

# 初始化配置文件
rich.print("[yellow]租赁服号:[/]",settings.server,sep="")
