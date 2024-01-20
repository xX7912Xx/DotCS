from uuid import UUID


class player(object):
    "EDotCS 玩家属性"
    uuid:UUID
    name:str
    def __init__(self,uuid:UUID,name:str):
        self.uuid=uuid
        self.name=name
    