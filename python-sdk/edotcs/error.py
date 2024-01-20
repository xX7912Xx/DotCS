class EDotCS_Get_Port_Error(Exception):
    "EDotCS 获取端口错误"
class EDotCS_Not_Find_Client_Error(Exception):
    "EDotCS 客户端不存在"
class EDotCS_Plugin_Name_Error(Exception):
    "EDotCS 插件命名错误"

class EDotCS_Plugin_No_Use_Say_To(Exception):
    "EDotCS API Say_To 接口未启用却使用引起的问题"