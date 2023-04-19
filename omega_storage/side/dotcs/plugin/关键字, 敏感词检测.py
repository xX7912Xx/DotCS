# Author: unknown
Description: unknown



# PLUGIN TYPE: player message
if "这里是敏感词" in msg:
    tellrawText(playername, "§l§4Warning§r", "§c已检测到关键字/敏感词: 敏感词.")
    ban(playername, 120, "已检测到关键字/敏感词: 敏感词.")



