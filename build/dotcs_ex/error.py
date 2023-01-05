from . import mc_color
class _error:#错误抛出错误
    def __init__(self):pass
    def __call__(self,text=""):
        if type(text).__name__ ==  'NoneType': text == 'None'
        try:
            mc_color.color("""§4ERROR §r §c{}""".format(text))
        except:
            mc_color.color("""§4ERROR §r §c未知错误""")
import sys

sys.modules[__name__] = _error()