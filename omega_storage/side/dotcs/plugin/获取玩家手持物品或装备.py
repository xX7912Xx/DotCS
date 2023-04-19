# Author: unknown
Description: unknown



# PLUGIN TYPE: def
itemNetworkIDprofile = getStatus("itemNetworkID").replace("\r", "").split("\n")
if "获取失败" in itemNetworkIDprofile:
    raise Exception("§4无法读取物品ID表, 文件位置: status\\itemNetworkID.txt")
color("§e不要修改/删除 status\\itemNetworkID.txt, 否则会出问题")
itemNetworkID2NameDict = {}
itemNetworkID2NameEngDict = {}
for i in itemNetworkIDprofile:
    itemNetworkID2NameDict[i.split(" ")[0]] = i.split(" ")[2]
    itemNetworkID2NameEngDict[i.split(" ")[0]] = i.split(" ")[1]


# 获取玩家手持物品名称并返回.
entityRuntimeID2playerName = {}
needToGetMainhandItem = False
needToGetArmorItem = False
needToGetMainhandAndArmorItem = False
targetMainhandAndArmor = ""
itemMainhandAndArmor = ""
targetArmor = ""
targetMainhand = ""
def getMainhandItem(targetName):
    global needToGetMainhandItem, itemMainhand, targetMainhand
    if targetName not in allplayers:
        raise Exception("player not found")
    timeStartGetMainhandItem = time.time()
    itemMainhand = {}
    targetMainhand = targetName
    needToGetMainhandItem = True
    sendcmd("/tp @s @a[name=%s]" % targetName)
    time.sleep(0.1)
    sendcmd("/tp 100000 100000 100000")
    time.sleep(0.1) 
    while True:
        if int(time.time() - timeStartGetMainhandItem) > 1:
            targetMainhand = ""
            needToGetMainhandItem = False
            raise Exception("timed out")
        if not(needToGetMainhandItem):
            targetMainhand = ""
            return itemMainhand
        time.sleep(0.01)

# 获取玩家装备名称并返回.
def getArmorItem(targetName):
    global needToGetArmorItem, itemArmor, targetArmor
    if targetName not in allplayers:
        raise Exception("player not found")
    timeStartGetArmorItem = time.time()
    itemArmor = {}
    targetArmor = targetName
    needToGetArmorItem = True
    sendcmd("/tp @s @a[name=%s]" % targetName)
    time.sleep(0.1)
    sendcmd("/tp 100000 100000 100000")
    time.sleep(0.1)
    while True:
        if int(time.time() - timeStartGetArmorItem) > 1:
            targetArmor = ""
            needToGetArmorItem = False
            raise Exception("timed out")
        if not(needToGetArmorItem):
            targetArmor = ""
            return itemArmor
        time.sleep(0.01)



# PLUGIN TYPE: packet on another thread 12
global needToGetMainhandItem, itemMainhand, targetMainhand, needToGetArmorItem, itemArmor, targetArmor
try:
    entityRuntimeID2playerName[jsonPkt["EntityRuntimeID"]] = jsonPkt["Username"]
except:
    pass
if needToGetMainhandItem and targetMainhand == jsonPkt["Username"]:
    itemMainhand = jsonPkt["HeldItem"]["Stack"]
    try:
        itemMainhand["itemName"] = itemNetworkID2NameDict[str(jsonPkt["HeldItem"]["Stack"]["NetworkID"])]
        itemMainhand["itemCmdName"] = itemNetworkID2NameEngDict[str(jsonPkt["HeldItem"]["Stack"]["NetworkID"])]
    except:
        itemMainhand["itemName"] = "未知"
        itemMainhand["itemCmdName"] = "unknown"
    needToGetMainhandItem = False
if needToGetMainhandAndArmorItem and targetMainhandAndArmor == jsonPkt["Username"]:
    itemMainhandAndArmor["mainHand"] = jsonPkt["HeldItem"]["Stack"]
    try:
        itemMainhandAndArmor["mainHand"]["itemName"] = itemNetworkID2NameDict[str(jsonPkt["HeldItem"]["Stack"]["NetworkID"])]
        itemMainhandAndArmor["mainHand"]["itemCmdName"] = itemNetworkID2NameEngDict[str(jsonPkt["HeldItem"]["Stack"]["NetworkID"])]
    except:
        itemMainhandAndArmor["mainHand"]["itemName"] = "未知"
        itemMainhandAndArmor["mainHand"]["itemCmdName"] = "unknown"

# PLUGIN TYPE: packet on another thread 32
global needToGetMainhandItem, itemMainhand, targetMainhand, needToGetArmorItem, itemArmor, targetArmor
if needToGetArmorItem and targetArmor == entityRuntimeID2playerName[jsonPkt["EntityRuntimeID"]]:
    itemArmor["Helmet"] = jsonPkt["Helmet"]["Stack"]
    itemArmor["Chestplate"] = jsonPkt["Chestplate"]["Stack"]
    itemArmor["Leggings"] = jsonPkt["Leggings"]["Stack"]
    itemArmor["Boots"] = jsonPkt["Boots"]["Stack"]
    for i in itemArmor:
        try:
            itemArmor[i]["itemName"] = itemNetworkID2NameDict[str(jsonPkt[i]["Stack"]["NetworkID"])]
            itemArmor[i]["itemCmdName"] = itemNetworkID2NameEngDict[str(jsonPkt[i]["Stack"]["NetworkID"])]
        except:
            itemArmor[i]["itemName"] = "未知"
            itemArmor[i]["itemCmdName"] = "unknown"
    needToGetArmorItem = False
if needToGetMainhandAndArmorItem and targetMainhandAndArmor == entityRuntimeID2playerName[jsonPkt["EntityRuntimeID"]]:
    itemMainhandAndArmor["armor"] = {}
    itemMainhandAndArmor["armor"]["Helmet"] = jsonPkt["Helmet"]["Stack"]
    itemMainhandAndArmor["armor"]["Chestplate"] = jsonPkt["Chestplate"]["Stack"]
    itemMainhandAndArmor["armor"]["Leggings"] = jsonPkt["Leggings"]["Stack"]
    itemMainhandAndArmor["armor"]["Boots"] = jsonPkt["Boots"]["Stack"]
    for i in itemMainhandAndArmor["armor"]:
        try:
            itemMainhandAndArmor["armor"][i]["itemName"] = itemNetworkID2NameDict[str(jsonPkt[i]["Stack"]["NetworkID"])]
            itemMainhandAndArmor["armor"][i]["itemCmdName"] = itemNetworkID2NameEngDict[str(jsonPkt[i]["Stack"]["NetworkID"])]
        except:
            itemMainhandAndArmor["armor"][i]["itemName"] = "未知"
            itemMainhandAndArmor["armor"][i]["itemCmdName"] = "unknown"
    needToGetMainhandAndArmorItem = False

# PLUGIN TYPE: packet on another thread 203
global needToGetMainhandItem, itemMainhand, targetMainhand, needToGetArmorItem, itemArmor, targetArmor
if needToGetArmorItem:
    itemArmor = {}
    needToGetArmorItem = False
if needToGetMainhandAndArmorItem:
    itemMainhandAndArmor["armor"] = {}
    needToGetMainhandAndArmorItem = False


