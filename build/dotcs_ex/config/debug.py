import os,json
from .. import color
from .. import tool
def update_debug(self:dict):
    "更新 server.txt 的信息到新版的 config.json 文件中"
    if "debug" not in self.config.keys():
        self.config["debug"] = tool.input_output.is_bool("[green]是否启用 [red]DEBUG[green] 模式(Y/n):[/]")
        color.color("§a已成功设置DEBUG模式!",info="§a 提示 ")

    self.update()