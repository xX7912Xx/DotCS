import time
class ExpireDict(dict):
    """
    一个支持key过期的类似的字典的数据结构
    1.创建一个过期字典对象 obj = ExpireDict()
    2.设置全局的key的过期时间 obj.exprie_time = 120 默认的过期时间为60秒
    3.添加key,并重新设置过期时间: obj['a'] =1;obj.set_key_expired('a',30);
    4.获取key的值 obj['a'];obj.get('a')
    5.不支持的字典内置方法:fromkeys,update,不支持工厂方法和字典推导式创建字典;
    """

    def __init__(self):
        """
        默认的超时60s
        """
        self.__expired = 60
        super(ExpireDict, self).__init__()

    @property
    def expire_time(self):
        return self.__expired

    @expire_time.setter
    def expire_time(self, value):
        self.__expired = value

    def __setitem__(self, key, value):
        """
        赋值
        :param key:
        :param value:
        :return:
        """
        begin_time = time.time()
        super(ExpireDict, self).__setitem__(
            key, [begin_time, begin_time + self.__expired, value])

    def __getitem__(self, key):
        """
        每次获取值是调用过期处理方法，只返回真实值
        :param itme
        :return:
        """
        if self.check_key(key) is False:
            return None
        super(ExpireDict, self).__getitem__(key)[1]=time.time() + self.__expired
        return super(ExpireDict, self).__getitem__(key)[-1]

    def set_key_expired(self, key, expired):
        """
        设置指定key的过期时间：过期时间等于最后一次写入的时间与expired的和
        :param key:
        :param expired 过期时间
        :return:
        """
        value_list = super(ExpireDict, self).__getitem__(key)
        value_list[1] = value_list[0] + expired
        super(ExpireDict, self).__setitem__(key, value_list)

    def get(self, key):
        if self.check_key(key) is False:
            return None
        return super(ExpireDict, self).get(key)[-1]

    def setdefault(self, key, value):
        # self.del_expired_key()
        super(ExpireDict, self).setdefault(
            key, [time.time(), time.time() + self.__expired, value])

    def values(self):
        self.del_expired_key()
        value_list = list(super(ExpireDict, self).values())
        new_values = map(lambda i: i[-1], value_list)
        return new_values

    def items(self):
        self.del_expired_key()
        itmes_list = list(super(ExpireDict, self).items())
        itmes = map(lambda i: (i[0], i[1][-1]), itmes_list)
        return itmes

    def pop(self, key):
        self.del_expired_key()
        return super(ExpireDict, self).pop(key)[-1]

    def popitem(self):
        self.del_expired_key()
        item = super(ExpireDict, self).popitem()
        return item[0], item[1][-1]

    def __get_expired(self, key):
        """
        获取指定元素的写入时间
        :param item:
        :return:
        """
        return super(ExpireDict, self).__getitem__(key)[1]

    def check_key(self, key):
        """
        判断key是否过期，过期后执行删除动作
        :param key:
        :return:
        """
        end_time = self.__get_expired(key)
        if time.time() >= end_time:
            self.__delitem__(key)
            return False
        else:
            return True

    def del_expired_key(self):
        """
        删除过期的key
        :return:
        """
        itmes_list = list(super(ExpireDict, self).items())
        sorted(itmes_list, key=lambda i: i[1][1])
        end_time = time.time()
        for k, v in itmes_list:
            if v[1] < end_time:
                self.__delitem__(k)

