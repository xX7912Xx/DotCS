from . import color
import os

class date:
    "DotCS 社区版更新信息存储(仅限社区版)"
    version = "v0.11.0"
    PyPIthird = [
            {"name": "bdx_work_shop", "author": "2401PT, SuperScript", "link": "https://github.com/CMA2401PT/BDXWorkShop"},
            {"name": "FastBuilder connector", "author": "2401PT", "link": "https://github.com/CMA2401PT/FastBuilder"},
            {"name": "TDES encrypt", "author": "7912", "link": "None"},
            {"name": "Space Rectangular Coordinate System", "author": "7912", "link": "None"}
        ]
    group_number = "467443403"
    welcome_text = """§b".命令"系统社区版 - 租赁服聊天栏菜单\n".Dot" Command System Community(DotCS)\nDotCS基于FastBuilder.\n社区版作者: 7912\n其官方插件作者: 7912, Pomelo"""

if os.path.isdir("player")==False:
    os.makedirs("player")
    color.color("§a配置文件夹 §eplayer§a 缺失,已重新生成",info=" 信息 ")

def getPlayerData(dataName: str, playerName: str, writeNew: str = "") -> (str | int | float):
    """
    获取玩家本地数据的函数
    读取文件: player\playerName\dataName.txt
    参数:
        dataName: str -> 数据名称
        playerName: str -> 玩家名称
        writeNew: str -> 若数据不存在, 写入的数据
    返回: str | int | float -> 文件读取结果
    """
    dataName = dataName.replace("\\", "/")
    fileDir = "player/%s/%s.txt" % (playerName, dataName)
    pathDir = ""
    pathAll = ("player/%s/%s" % (playerName, dataName)).split("/")
    pathAll.pop(-1)
    for i in pathAll:
        pathDir += "%s/" % i
    if not os.path.isdir(pathDir):
        pathToCreate = ""
        for i in pathDir.split("/"):
            try:
                pathToCreate += "%s/" % i
                os.mkdir(pathToCreate)
            except:
                pass
    if not os.path.isfile(fileDir):
        with open(fileDir, "w", encoding = "utf-8", errors = "ignore") as file:
            file.write(writeNew)
    with open(fileDir, "r", encoding = "utf-8", errors = "ignore") as file:
        data = file.read()
    if "." not in data:
        try:
            data = int(data)
        except:
            pass
    else:
        try:
            data = float(data)
        except:
            pass
    return data
def setPlayerData(dataName: str, playerName: str, dataValue, writeNew: str = ""):
    """
    设置玩家本地数据的函数
    写入文件: player\playerName\dataName.txt
    参数:
        dataName: str -> 数据名称
        playerName: str -> 玩家名称
        dataValue: Any -> 要设置的数据, 写入前会自动转化为str
        writeNew: str -> 若数据不存在, 写入的数据
    返回: dataValue: Any -> 设置结果
    """
    dataName = dataName.replace("\\", "/")
    fileDir = "player/%s/%s.txt" % (playerName, dataName)
    pathDir = ""
    pathAll = ("player/%s/%s" % (playerName, dataName)).split("/")
    pathAll.pop(-1)
    for i in pathAll:
        pathDir += "%s/" % i
    if not os.path.isdir(pathDir):
        pathToCreate = ""
        for i in pathDir.split("/"):
            try:
                pathToCreate += "%s/" % i
                os.mkdir(pathToCreate)
            except:
                pass
    if not os.path.isfile(fileDir):
        with open(fileDir, "w", encoding = "utf-8", errors = "ignore") as file:
            file.write(writeNew)
    with open(fileDir, "w", encoding = "utf-8", errors = "ignore") as file:
        file.write(str(dataValue))
    return dataValue
def addPlayerData(dataName: str, playerName: str, dataValue, dataType: str = "int", writeNew: str = ""):
    """
    增加/追加玩家本地数据的函数
    写入文件: player\playerName\dataName.txt
    参数:
        dataName: str -> 数据名称
        playerName: str -> 玩家名称
        dataValue: Any -> 要设置的数据, 写入前会自动转化为str
        dataType: "int" | "add" -> 设置类型
            add: 在文件末尾追加
            int: 数学计算, 加上新值
        writeNew: str -> 若数据不存在, 写入的数据
    返回: dataValue: Any -> 设置结果
    """
    if dataType == "int":
        return setPlayerData(dataName, playerName, getPlayerData(dataName, playerName, writeNew)+dataValue, writeNew)
    elif dataType == "add":
        dataName = dataName.replace("\\", "/")
        fileDir = "player/%s/%s.txt" % (playerName, dataName)
        pathDir = ""
        pathAll = ("player/%s/%s" % (playerName, dataName)).split("/")
        pathAll.pop(-1)
        for i in pathAll:
            pathDir += "%s/" % i
        if not os.path.isdir(pathDir):
            pathToCreate = ""
            for i in pathDir.split("/"):
                try:
                    pathToCreate += "%s/" % i
                    os.mkdir(pathToCreate)
                except:
                    pass
        with open(fileDir, "a", encoding = "utf-8", errors = "ignore") as file:
            file.write("%s\n" % str(dataValue))
        return dataValue
    else:
        raise Exception("dataType error")
