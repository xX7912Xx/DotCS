from typing import List
from dataclasses import dataclass

@dataclass
class Player:
    name:str
    uuid:str
@dataclass
class GetPlayer:
    player:Player
    success:bool
    message:str
@dataclass
class GetPlayerList:
    players: List[Player]
    success:bool
    message:str

