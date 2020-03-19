# coding: utf-8
# 在计算哈希的时候，不能仅针对原始输入计算，需要增加一个salt来使得相同的输入也能得到不同的哈希   加盐值，防止黑客攻击
import hashlib
import hmac

# 计算
# 原始消息message，随机key，哈希算法，这里采用MD5
message = b'Hello, world!'
key = b'1235555456'
h = hmac.new(key, message, digestmod='MD5')
# 如果消息很长，可以多次调用h.update(msg)
print(h.hexdigest())

# 'fa4ee7d173f2d97ee79022d1a7355bcf'
print(hashlib.md5("Hello, world!".encode("utf-8")).hexdigest())


# 6cd3556deb0da54bca060b4c39479839

# 开发者密钥API实现方法类
def create():
    return 'create'


def disable():
    return 'disable'


def delete():
    return 'delete'

def status():
    return 'status'
