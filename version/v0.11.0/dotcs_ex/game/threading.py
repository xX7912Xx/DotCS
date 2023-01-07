import threading
import ctypes
import traceback
from .. import color
from .. import tool


class createThread(threading.Thread):
    def __init__(self, name, data = {}, func = "", output = True):
        threading.Thread.__init__(self)
        self.name = name
        self.data = data
        self.func = func
        self.stopping = False
        self.daemon = True
        self.output = output
        self.setDaemon(True)
        self.start()
    def run(self):
        try:
            if self.output:
                color.color("§e启动线程 %s." % self.name, info = "§e 线程 ")
            if tool.getType(self.func) != "str":
                self.func(self)
            else:
                exec("%s(self)" % self.func)
        except Exception as err:
            errmsg = ("线程 %s 报错, 信息:\n" % self.name)+str(err)
            color("§c"+traceback.format_exc(), info = "§c 错误 ")
            log("§c" + errmsg, sendtogamewithERROR = True, info = "§c 错误 ")
        except SystemExit as err:
            pass
            # color("§eThread %s has been terminated forcely." % self.name)
        finally:
            if self.output:
                color("§e终止线程 %s." % self.name, info = "§e 线程 ")
    def get_id(self):
        if hasattr(self, '_thread_id'):
            return self._thread_id
        for id, thread in threading._active.items():
            if thread is self:
                return id
    def stop(self):
        self.stopping = True
        # color("§eTerminating thread %s." % self.name)
        thread_id = self.get_id()
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, ctypes.py_object(SystemExit))
        if res > 1:
            ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, 0)
            color("§c终止线程失败", info = "§c 错误 ")