from . import mc_color
class _input:
    def __init__(self):pass
    def __call__(self,prompt:str =""):
        "以彩色字的形式输出"
        mc_color.color(prompt,end="")
        a =input()
        return a
import sys

sys.modules[__name__] = _input()