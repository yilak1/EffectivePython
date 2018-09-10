import os
# 接受str或者bytes，总是返回str
def to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str
    return value


def to_bytes(bytes_or_str):
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode('utf-8')
    else:
        value = bytes_or_str
    return value


# python3 open 默认使用utf-8打开文件，写入二进制要用'wb'
# 下面报错 TypeError: write() argument must be str, not bytes
# with open('/random.bin', "w") as f:
#     f.write(os.urandom(10))
with open('/home/lds/code/machine-learning/EffecttivePython/ch1/random.bin', "wb") as f:
    f.write(os.urandom(10))
# 打开‘rb’也是同样问题,不要使用r模式


