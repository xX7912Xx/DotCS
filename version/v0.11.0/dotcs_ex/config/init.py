import os,json
from .. import color
class config:
    def __init__(self,path,encoding="utf-8"):
        "读取配置文件"
        self.path = path
        self.encoding = encoding
        self.config = {}
        self.function = []
        # 读取配置文件
        if os.path.isfile(path) == False:
            with open(path, "w", encoding=encoding) as f:
                f.write("{}")
        try:
            with open(path, "r", encoding=encoding) as f:
                self.config = json.load(f)
        except:
            color.color(f"§4配置文件损坏!已重新创建 §e{path}",info="§e警告")
            with open(path, "w", encoding=encoding) as f:
                f.write("{}")
            self.config = {}
    def init(self):
        "运行配置文件"
        for i in self.function:
            i(self)
    
    def get_return(self):
        return self.config

    def append_function(self,function):
        self.function.append(function)
    
    def update(self):
        with open(self.path, "w", encoding=self.encoding) as f:
            json.dump(self.config,f,ensure_ascii=False)
