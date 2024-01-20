# EDotCS 处理启动参数的问题
import sys

from edotcs.error import EDotCS_Get_Port_Error
def _get_port()->int:
    "获取EDotCS主动启动时的端口,如果没有则返回0"
    if len(sys.argv)<2:
        return 0
    else:
        if sys.argv[1].isdecimal():
            return int(sys.argv[1])
        else:
            raise EDotCS_Get_Port_Error("EDotCS 插件启动失败,您传递的端口非数字")
