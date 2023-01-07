import os
import json
from .. import color
from .. import tool
import platform


def update_fb_set(self: dict):
    "更新 server.txt 的信息到新版的 config.json 文件中"
    if "fb_config" not in self.config.keys():
        self.config["fb_config"] = tool.input_output.is_bool(
            "[green]是否使用[red]默认FB配置[green](Y/n):[/]")
        if self.config["fb_config"]:
            self.config["fb_config"] = {
                "fb_update_url": "https://api.github.com/repos/LNSSPsd/PhoenixBuilder/releases/latest",
                "fb_update_mode_old": False,
                "fb_ws_connect": "wss://api.fastbuilder.pro:2053/",
                "fb_token_mode": True,
                "fb_token_path": "fbtoken",
                "fb_token": "",
                "fb_path": "phoenixBuilder.exe" if platform.system() == "Windows" else "phoenixBuilder",
                "dotcs_connect_mode": True,
                "fb_connect_url": "127.0.0.1:8000",
                "No_update_fb_auto": False
            }
            color.color("§4记得前往FB用户中心下载 fbtoken 丢到此目录哦")
            tool.countdown(10, msg="§e请阅读说明", delay_color="§4")
        else:
            self.config["fb_config"] = {}
            if "dotcs_connect_mode" not in self.config["fb_config"].keys():
                self.config["fb_config"]["dotcs_connect_mode"] = tool.input_output.is_bool(
                    "[green]是否由 DotCS 管理 FB 的启动?(Y/n):[/]")
                if self.config["fb_config"]["dotcs_connect_mode"]:
                    if "fb_update_url" not in self.config["fb_config"].keys():
                        self.config["fb_config"]["fb_update_url"] = tool.input_output.is_bool(
                            "[green]是否使用默认的FB更新连接模式(Y/n):[/]")
                        if self.config["fb_config"]["fb_update_url"]:
                            self.config["fb_config"]["fb_update_url"] = "https://api.github.com/repos/LNSSPsd/PhoenixBuilder/releases/latest"
                            self.config["fb_config"]["fb_update_mode_old"] = False
                        else:
                            self.config["fb_config"]["fb_update_mode_old"] = tool.input_output.is_bool(
                                "[green]是否使用传统的FB版本更新链接(Y/n):[/]")
                            if self.config["fb_config"]["fb_update_mode_old"]:
                                while (1):
                                    self.config["fb_config"]["fb_update_url"] = tool.input_output.input_re(
                                        "[green]请输入FB版本检测连接:[/]", pattern=r"[a-zA-z]+://[^\s]*")
                                    if self.config["fb_config"]["fb_update_url"][0]:
                                        self.config["fb_config"]["fb_update_url"] = self.config["fb_config"]["fb_update_url"][0]
                                        break
                                    else:
                                        color.color(
                                            "§4您输入的url不合法!请重新输入", info="§4 错误 ")
                            else:
                                while (1):
                                    self.config["fb_config"]["fb_update_url"] = tool.input_output.input_re(
                                        "[green]请输入FB版本检测连接:[/]", pattern=r"[a-zA-z]+://[^\s]*")
                                    if self.config["fb_config"]["fb_update_url"][0]:
                                        self.config["fb_config"]["fb_update_url"] = self.config["fb_config"]["fb_update_url"][0]
                                        break
                                    else:
                                        color.color(
                                            "§4您输入的url不合法!请重新输入", info="§4 错误 ")
                    if "No_update_fb_auto" not in self.config["fb_config"].keys():
                        self.config["fb_config"]["No_update_fb_auto"] = tool.input_output.is_bool(
                            "[green]是否使用禁用FB自动更新(Y/n):[/]")
                    if "fb_ws_connect" not in self.config["fb_config"].keys():
                        self.config["fb_config"]["fb_ws_connect"] = tool.input_output.is_bool(
                            "[green]是否使用默认的FB验证服务器(Y/n):[/]")
                        if self.config["fb_config"]["fb_ws_connect"]:
                            self.config["fb_config"]["fb_ws_connect"] = "wss://api.fastbuilder.pro:2053/"
                        else:
                            while (1):
                                self.config["fb_config"]["fb_ws_connect"] = tool.input_output.input_re(
                                    "[green]请输入FB验证服务器连接(通常是ws或wss协议):[/]", pattern=r"[a-zA-z]+://[^\s]*")
                                if self.config["fb_config"]["fb_ws_connect"][0]:
                                    self.config["fb_config"]["fb_ws_connect"] = self.config["fb_config"]["fb_ws_connect"][0]
                                    break
                                else:
                                    color.color(
                                        "§4您输入的url不合法!请重新输入", info="§4 错误 ")
                    if "fb_token_mode" not in self.config["fb_config"].keys():
                        self.config["fb_config"]["fb_token_mode"] = tool.input_output.is_bool(
                            "[green]是否使用默认的fb账号设置(Y/n):[/]")
                        if self.config["fb_config"]["fb_token_mode"]:
                            color.color("§4记得前往FB用户中心下载 fbtoken 丢到此目录哦")
                            tool.countdown(10, msg="§e请阅读说明", delay_color="§4")
                            self.config["fb_config"]["fb_token_mode"] = True
                            self.config["fb_config"]["fb_token_path"] = "fbtoken"
                        else:
                            self.config["fb_config"]["fb_token_mode"] = tool.input_output.is_bool(
                                "[green]使用 路径搜索模式 还是 直接输入 fbtoken?(Y/n):[/]")
                            if self.config["fb_config"]["fb_token_mode"]:
                                self.config["fb_config"]["fb_token_path"] = tool.input_output.input(
                                    "[green]请输入 fbtoken 所在路径:")
                            else:
                                self.config["fb_config"]["fb_token"] = tool.input_output.input(
                                    "[green]请输入 fbtoken:")
                    if "fb_path" not in self.config["fb_config"].keys():
                        self.config["fb_config"]["fb_path"] = tool.input_output.is_bool(
                            "[green]是否使用默认的fb程序路径(Y/n):[/]")
                        if self.config["fb_config"]["fb_path"]:
                            self.config["fb_config"]["fb_path"] = "phoenixBuilder.exe" if platform.system(
                            ) == "Windows" else "phoenixBuilder"
                        else:
                            self.config["fb_config"]["fb_path"] = tool.input_output.input(
                                "[green]请输入fb程序路径:[/]")
                else:
                    if "fb_connect_url" not in self.config["fb_config"].keys():
                        self.config["fb_config"]["fb_connect_url"] = tool.input_output.is_bool(
                            "[green]是否使用默认的fb连接地址(Y/n):[/]")
                        if self.config["fb_config"]["fb_connect_url"]:
                            self.config["fb_config"]["fb_connect_url"] = "127.0.0.1:8000"
                        else:
                            self.config["fb_config"]["fb_connect_url"] = tool.input_output.input(
                                "[green]请输入fb连接地址:[/]")
    else:
        if "dotcs_connect_mode" not in self.config["fb_config"].keys():
            self.config["fb_config"]["dotcs_connect_mode"] = tool.input_output.is_bool(
                "[green]是否由 DotCS 管理 FB 的启动?(Y/n):[/]")
            if self.config["fb_config"]["dotcs_connect_mode"]:
                if "fb_update_url" not in self.config["fb_config"].keys():
                    self.config["fb_config"]["fb_update_url"] = tool.input_output.is_bool(
                        "[green]是否使用默认的FB更新连接模式(Y/n):[/]")
                    if self.config["fb_config"]["fb_update_url"]:
                        self.config["fb_config"]["fb_update_url"] = "https://api.github.com/repos/LNSSPsd/PhoenixBuilder/releases/latest"
                        self.config["fb_config"]["fb_update_mode_old"] = False
                    else:
                        self.config["fb_config"]["fb_update_mode_old"] = tool.input_output.is_bool(
                            "[green]是否使用传统的FB版本更新链接(Y/n):[/]")
                        if self.config["fb_config"]["fb_update_mode_old"]:
                            while (1):
                                self.config["fb_config"]["fb_update_url"] = tool.input_output.input_re(
                                    "[green]请输入FB版本检测连接:[/]", pattern=r"[a-zA-z]+://[^\s]*")
                                if self.config["fb_config"]["fb_update_url"][0]:
                                    self.config["fb_config"]["fb_update_url"] = self.config["fb_config"]["fb_update_url"][0]
                                    break
                                else:
                                    color.color(
                                        "§4您输入的url不合法!请重新输入", info="§4 错误 ")
                        else:
                            while (1):
                                self.config["fb_config"]["fb_update_url"] = tool.input_output.input_re(
                                    "[green]请输入FB版本检测连接:[/]", pattern=r"[a-zA-z]+://[^\s]*")
                                if self.config["fb_config"]["fb_update_url"][0]:
                                    self.config["fb_config"]["fb_update_url"] = self.config["fb_config"]["fb_update_url"][0]
                                    break
                                else:
                                    color.color(
                                        "§4您输入的url不合法!请重新输入", info="§4 错误 ")
                if "fb_ws_connect" not in self.config["fb_config"].keys():
                    self.config["fb_config"]["fb_ws_connect"] = tool.input_output.is_bool(
                        "[green]是否使用默认的FB验证服务器(Y/n):[/]")
                    if self.config["fb_config"]["fb_ws_connect"]:
                        self.config["fb_config"]["fb_ws_connect"] = "wss://api.fastbuilder.pro:2053/"
                    else:
                        while (1):
                            self.config["fb_config"]["fb_ws_connect"] = tool.input_output.input_re(
                                "[green]请输入FB验证服务器连接(通常是ws或wss协议):[/]", pattern=r"[a-zA-z]+://[^\s]*")
                            if self.config["fb_config"]["fb_ws_connect"][0]:
                                self.config["fb_config"]["fb_ws_connect"] = self.config["fb_config"]["fb_ws_connect"][0]
                                break
                            else:
                                color.color("§4您输入的url不合法!请重新输入",
                                            info="§4 错误 ")
                if "No_update_fb_auto" not in self.config["fb_config"].keys():
                    self.config["fb_config"]["No_update_fb_auto"] = tool.input_output.is_bool(
                        "[green]是否使用禁用FB自动更新(Y/n):[/]")
                if "fb_token_mode" not in self.config["fb_config"].keys():
                    self.config["fb_config"]["fb_token_mode"] = tool.input_output.is_bool(
                        "[green]是否使用默认的fb账号设置(Y/n):[/]")
                    if self.config["fb_config"]["fb_token_mode"]:
                        color.color("§4记得前往FB用户中心下载 fbtoken 丢到此目录哦")
                        tool.countdown(10, msg="§e请阅读说明", delay_color="§4")
                        self.config["fb_config"]["fb_token_mode"] = True
                        self.config["fb_config"]["fb_token_path"] = "fbtoken"
                    else:
                        self.config["fb_config"]["fb_token_mode"] = tool.input_output.is_bool(
                            "[green]使用 路径搜索模式 还是 直接输入 fbtoken?(Y/n):[/]")
                        if self.config["fb_config"]["fb_token_mode"]:
                            self.config["fb_config"]["fb_token_path"] = tool.input_output.input(
                                "[green]请输入 fbtoken 所在路径:")
                        else:
                            self.config["fb_config"]["fb_token"] = tool.input_output.input(
                                "[green]请输入 fbtoken:")
                if "fb_path" not in self.config["fb_config"].keys():
                    self.config["fb_config"]["fb_path"] = tool.input_output.is_bool(
                        "[green]是否使用默认的fb程序路径(Y/n):[/]")
                    if self.config["fb_config"]["fb_path"]:
                        self.config["fb_config"]["fb_path"] = "phoenixBuilder.exe" if platform.system(
                        ) == "Windows" else "phoenixBuilder"
                    else:
                        self.config["fb_config"]["fb_path"] = tool.input_output.input(
                            "[green]请输入fb程序路径:[/]")
            else:
                if "fb_connect_url" not in self.config["fb_config"].keys():
                    self.config["fb_config"]["fb_connect_url"] = tool.input_output.is_bool(
                        "[green]是否使用默认的fb连接地址(Y/n):[/]")
                    if self.config["fb_config"]["fb_connect_url"]:
                        self.config["fb_config"]["fb_connect_url"] = "127.0.0.1:8000"
                    else:
                        self.config["fb_config"]["fb_connect_url"] = tool.input_output.input(
                            "[green]请输入fb连接地址:[/]")
        else:
            if self.config["fb_config"]["dotcs_connect_mode"]:
                if "fb_update_url" not in self.config["fb_config"].keys():
                    self.config["fb_config"]["fb_update_url"] = tool.input_output.is_bool(
                        "[green]是否使用默认的FB更新连接模式(Y/n):[/]")
                    if self.config["fb_config"]["fb_update_url"]:
                        self.config["fb_config"]["fb_update_url"] = "https://api.github.com/repos/LNSSPsd/PhoenixBuilder/releases/latest"
                        self.config["fb_config"]["fb_update_mode_old"] = False
                    else:
                        self.config["fb_config"]["fb_update_mode_old"] = tool.input_output.is_bool(
                            "[green]是否使用传统的FB版本更新链接(Y/n):[/]")
                        if self.config["fb_config"]["fb_update_mode_old"]:
                            while (1):
                                self.config["fb_config"]["fb_update_url"] = tool.input_output.input_re(
                                    "[green]请输入FB版本检测连接:[/]", pattern=r"[a-zA-z]+://[^\s]*")
                                if self.config["fb_config"]["fb_update_url"][0]:
                                    self.config["fb_config"]["fb_update_url"] = self.config["fb_config"]["fb_update_url"][0]
                                    break
                                else:
                                    color.color(
                                        "§4您输入的url不合法!请重新输入", info="§4 错误 ")
                        else:
                            while (1):
                                self.config["fb_config"]["fb_update_url"] = tool.input_output.input_re(
                                    "[green]请输入FB版本检测连接:[/]", pattern=r"[a-zA-z]+://[^\s]*")
                                if self.config["fb_config"]["fb_update_url"][0]:
                                    self.config["fb_config"]["fb_update_url"] = self.config["fb_config"]["fb_update_url"][0]
                                    break
                                else:
                                    color.color(
                                        "§4您输入的url不合法!请重新输入", info="§4 错误 ")
                if "No_update_fb_auto" not in self.config["fb_config"].keys():
                    self.config["fb_config"]["No_update_fb_auto"] = tool.input_output.is_bool(
                        "[green]是否使用禁用FB自动更新(Y/n):[/]")
                if "fb_ws_connect" not in self.config["fb_config"].keys():
                    self.config["fb_config"]["fb_ws_connect"] = tool.input_output.is_bool(
                        "[green]是否使用默认的FB验证服务器(Y/n):[/]")
                    if self.config["fb_config"]["fb_ws_connect"]:
                        self.config["fb_config"]["fb_ws_connect"] = "wss://api.fastbuilder.pro:2053/"
                    else:
                        while (1):
                            self.config["fb_config"]["fb_ws_connect"] = tool.input_output.input_re(
                                "[green]请输入FB验证服务器连接(通常是ws或wss协议):[/]", pattern=r"[a-zA-z]+://[^\s]*")
                            if self.config["fb_config"]["fb_ws_connect"][0]:
                                self.config["fb_config"]["fb_ws_connect"] = self.config["fb_config"]["fb_ws_connect"][0]
                                break
                            else:
                                color.color(
                                    "§4您输入的url不合法!请重新输入", info="§4 错误 ")
                if "fb_token_mode" not in self.config["fb_config"].keys():
                    self.config["fb_config"]["fb_token_mode"] = tool.input_output.is_bool(
                        "[green]是否使用默认的fb账号设置(Y/n):[/]")
                    if self.config["fb_config"]["fb_token_mode"]:
                        color.color("§4记得前往FB用户中心下载 fbtoken 丢到此目录哦")
                        tool.countdown(10, msg="§e请阅读说明", delay_color="§4")
                        self.config["fb_config"]["fb_token_mode"] = True
                        self.config["fb_config"]["fb_token_path"] = "fbtoken"
                    else:
                        self.config["fb_config"]["fb_token_mode"] = tool.input_output.is_bool(
                            "[green]使用 路径搜索模式 还是 直接输入 fbtoken?(Y/n):[/]")
                        if self.config["fb_config"]["fb_token_mode"]:
                            self.config["fb_config"]["fb_token_path"] = tool.input_output.input(
                                "[green]请输入 fbtoken 所在路径:")
                        else:
                            self.config["fb_config"]["fb_token"] = tool.input_output.input(
                                "[green]请输入 fbtoken:")
                if "fb_path" not in self.config["fb_config"].keys():
                    self.config["fb_config"]["fb_path"] = tool.input_output.is_bool(
                        "[green]是否使用默认的fb程序路径(Y/n):[/]")
                    if self.config["fb_config"]["fb_path"]:
                        self.config["fb_config"]["fb_path"] = "phoenixBuilder.exe" if platform.system(
                        ) == "Windows" else "phoenixBuilder"
                    else:
                        self.config["fb_config"]["fb_path"] = tool.input_output.input(
                            "[green]请输入fb程序路径:[/]")
            else:
                if "fb_connect_url" not in self.config["fb_config"].keys():
                    self.config["fb_config"]["fb_connect_url"] = tool.input_output.is_bool(
                        "[green]是否使用默认的fb连接地址(Y/n):[/]")
                    if self.config["fb_config"]["fb_connect_url"]:
                        self.config["fb_config"]["fb_connect_url"] = "127.0.0.1:8000"
                    else:
                        self.config["fb_config"]["fb_connect_url"] = tool.input_output.input(
                            "[green]请输入fb连接地址:[/]")
    self.update()
