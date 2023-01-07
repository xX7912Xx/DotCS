class PluginSkip(Exception):
    __doc__=\
    """
    插件报错跳过
    ---
    当插件抛出此错误时,DotCS 将无视此错误并运行其他插件。
    """