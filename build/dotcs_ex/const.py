class _const():
    def __init__(self):
        object.__setattr__(self, "__dict_hidden__", {})
    def __delattr__(self, key):
        if key in object.__getattribute__(self, "__dict_hidden__"):
            raise Exception("You can not delete a const variable.")
        else:
            raise AttributeError(key)
    def __getattribute__(self, key):
        result = object.__getattribute__(self, "__dict_hidden__")
        if key not in object.__getattribute__(self, "__dict_hidden__"):
            raise KeyError(key)
        return result[key]
    def __dir__(self):
        raise Exception("You can not access this.")