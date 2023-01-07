windows = "windows"
linux = "linux"
darwin = "darwin"
import platform

class _system:
    "有关当前操作系统 的快捷判定变量"
    __version__ = "0.1.0"  # 该类的版本

    def __init__(self):

        self.windows = False
        self.linux = False
        self.darwin = False
        self.system_type = platform.system()

        match self.system_type:
            case "Windows":
                # Windows 操作系统
                self.windows = True
            case "Linux":
                self.linux = True
            case "Darwin":
                self.darwin = True

    def is_windows(self) -> bool:
        "判定当前的操作系统是否为 windows"
        return self.windows

    def is_linux(self) -> bool:
        "判定当前的操作系统是否为 linux"
        return self.linux

    def is_darwin(self) -> bool:
        "判定当前的操作系统是否为 darwin"
        return self.darwin

    def system(self) -> str:
        "获取当前的操作系统的名字"
        return self.system_type