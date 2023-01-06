import os,json
from .. import color
from .. import tool
def update_server(self:dict):
    "更新 server.txt 的信息到新版的 config.json 文件中"
    if self.config["fb_config"]["dotcs_connect_mode"]:
        if os.path.isfile("server.txt"):
            try:
                with open("server.txt","r",encoding="utf-8") as f:
                    config = json.load(f)
            except:
                config = {}
    
        else:
            config = {}
    
        # 开始准备数据迁移
        if "server" not in self.config.keys():
            if "code" not in config.keys():
                while(1):
                    self.config["server"] = tool.input_output.input_int("[green]请输入租赁服号:[/]")
                    if self.config["server"][0]:
                        self.config["server"] = self.config["server"][1]
                        break
                    else:
                        color.color("§4租赁服号设置错误!租赁服号应当为纯数字的!",info="§4 警告 §4")
                color.color("§a已成功设置租赁服号!",info="§a 提示 ")
            else:
                self.config["server"] = config["code"]
        
        if "password" not in self.config.keys():
            if "password" not in config.keys():
                while(1):
                    self.config["password"] = tool.input_output.input_int("[green]请输入租赁服密码(没有就输入123456):[/]")
                    if self.config["password"][0]:
                        self.config["password"] = self.config["password"][1]
                        break
                    else:
                        color.color("§4租赁服密码设置错误!租赁服号应当为纯数字的!",info="§4 警告 §4")
                color.color("§a已成功设置租赁服密码!",info="§a 提示 ")
            else:
                self.config["password"] = config["password"]
    
    self.update()