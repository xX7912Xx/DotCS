import dataclasses
import queue
class Api_Queue:
    is_use = False
    queue = []
class Api:
    Say_To = Api_Queue()
    SendCmd = Api_Queue()
    SendWSCmd = Api_Queue()
    Log = Api_Queue()
    Ban = Api_Queue()

class edotcs_app:
    Api = Api()

