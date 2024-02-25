import importlib
import pip
try:
    importlib.import_module("aiohttp")
except:
    pip.main(['install', 'aiohttp'])
    importlib.import_module("aiohttp")
try:
    importlib.import_module("loguru")
except:
    pip.main(['install', 'loguru'])
    importlib.import_module("loguru")
try:
    importlib.import_module("google.protobuf")
except:
    pip.main(['install', 'protobuf'])
    importlib.import_module("google.protobuf")
try:
    importlib.import_module("orjson")
except:
    pip.main(['install', 'orjson'])
    try:
        importlib.import_module("orjson")
    except:
        import json
from .main.main import EDotCS
from . import grpc
from . import type