import collections
import itertools
import sys

def dictOnly(dict):
    result = {"_total": 0}
    for i in dict:
        result[i] = {"total": 0}
        result[i]["key"] = sys.getsizeof(i)
        result[i]["value"] = sys.getsizeof(dict[i])
        result[i]["total"] = result[i]["key"] + result[i]["value"]
        result["_total"] += result[i]["total"]
    return result


def total(o, handlers={}, verbose = False):
    dict_handler = lambda d: itertools.chain.from_iterable(d.items())
    all_handlers = {tuple: iter,
                    list: iter,
                    collections.deque: iter,
                    dict: dict_handler,
                    set: iter,
                    frozenset: iter,
                }
    all_handlers.update(handlers)
    seen = set()
    default_size = sys.getsizeof(0)
    def sizeof(o):
        if id(o) in seen:
            return 0
        seen.add(id(o))
        s = sys.getsizeof(o, default_size)
        if verbose:
            print(s, type(o))
        for typ, handler in all_handlers.items():
            try:
                if isinstance(o, typ):
                    s += sum(map(sizeof, handler(o)))
                    break
            except Exception as err:
                pass
        return s
    return sizeof(o)

# print(total(globals(), verbose = True))

