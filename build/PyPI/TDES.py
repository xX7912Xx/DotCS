import base64
import Crypto.Cipher.DES3
import hashlib

def md5(data, times = 1):
    for i in range(times):
        data = hashlib.md5(data.encode(encoding = "UTF-8")).hexdigest()
    return data

def PKCSpadding(data, block_size = 8):
    pl = block_size - (len(data) % block_size)
    return data + bytearray([pl for i in range(pl)])

def encrypt(data, key = "", b64 = True, times = 1):
    if data.__class__.__name__ == "str":
        data = data.encode("utf-8")
    for i in range(times):
        if b64:
            data = base64.b64encode(Crypto.Cipher.DES3.new(key = md5(key)[0:24], mode = Crypto.Cipher.DES3.MODE_ECB).encrypt(PKCSpadding(data)))
        else:
            data = Crypto.Cipher.DES3.new(key = md5(key)[0:24], mode = Crypto.Cipher.DES3.MODE_ECB).encrypt(PKCSpadding(data))
    if b64:
        return data.decode("utf-8")
    else:
        return data

def decrypt(data, key = "", b64 = True, times = 1):
    if data.__class__.__name__ == "str":
        data = data.encode("utf-8")
    for i in range(times):
        if b64:
            data = Crypto.Cipher.DES3.new(key = md5(key)[0:24], mode = Crypto.Cipher.DES3.MODE_ECB).decrypt(base64.b64decode(data))
        else:
            data = Crypto.Cipher.DES3.new(key = md5(key)[0:24], mode = Crypto.Cipher.DES3.MODE_ECB).decrypt(data)
    if b64:
        return data[:-data[-1]].decode("utf-8")
    else:
        return data[:-data[-1]]

