import ctypes
import os,sys
import platform
import colorama
colorama.init(autoreset=True)

def color(text: str, output: bool = True, end: str = "\n", replace: bool = False, replaceByNext: bool = False, info = " 信息 "):
    print(text.replace("§0","\033[0;37;30m")
    .replace("§1", "\033[0;37;34m").replace("§2", "\033[0;37;32m").replace("§3", "\033[0;37;36m")
    .replace("§4", "\033[0;37;31m").replace("§5", "\033[0;37;35m").replace("§6", "\033[0;37;33m")
    .replace("§7", "\033[0;37;90m").replace("§8", "\033[0;37;2m").replace("§9", "\033[0;37;94m")
    .replace("§a", "\033[0;37;92m").replace("§b", "\033[0;37;96m").replace("§c", "\033[0;37;91m")
    .replace("§d", "\033[0;37;95m").replace("§e", "\033[0;37;93m").replace("§f", "\033[0; 37; 1m")
    .replace("§r", "\033[0m")+"\033[0m",end=end)