from . import tool
from . import color
from . import date

def welcome():
    color.color(date.date.welcome_text, info = "§b 信息 ")
    color.color(f'§b用户交流群: {date.date.group_number}', info = "§b 信息 ")