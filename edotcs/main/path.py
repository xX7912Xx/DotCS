# EDotCS 处理启动参数的问题
import sys

from .error import EDotCS_Get_Port_Error
def _get_ip_port()->int:
    "获取EDotCS主动启动时的端口,如果没有则返回0"
    if len(sys.argv)<2:
        return 0
    else:
        return sys.argv[1]
