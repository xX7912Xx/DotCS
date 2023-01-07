from . import mc_color
class _warning:#警告抛出
    def __init__(self):pass
    def __call__(self,text=""):
        if type(text).__name__ ==  'NoneType': text == 'None'
        try:
            mc_color.color("""§6Warning §r §e{}""".format(text))
        except:
            mc_color.color("""§6Warning §r §e未知警告""")
import sys

sys.modules[__name__] = _warning()