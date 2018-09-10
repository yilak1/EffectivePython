import json
# 不要在for和while循环后面写else块
# 合理利用try/except/else/finally结构中的每个代码块

# 第一行发生IO异常，程序不会执行try和finally，如果执行try，则不管出不出现异常，都执行finally
handle = open('random_data.txt')   # May raise IOError
try:
    data = handle.read()         # May raise UnicodeDecodeError
finally:
    handle.close()              # Always runs after try:


# 从字符床中加载JSON字典数据，使用else代码块，try没有发生异常，那麽就执行else块
# 如果数据不是json格式，用json.load解码会报出ValueError异常，这个异常由except捕获处理。
# 如果能够解码，那麽else块的查询语句就会执行，他会根据键来查出相关的值。
# 若else里查询异常，则会向上传播，给屏幕报错。
def load_json_key(data, key):
    try:
        result_dict = json.loads(data)         # May raise ValueError
    except ValueError as e:
        raise KeyError from e
    else:
        return result_dict[key]                # May raise KeyError


# 从文件中读取某项事务的描述信息，处理该事务，然后就地更新该文件。
# 即使在写入result时，finally也能够执行
UNDEFINED = object()


def divide_json(path):
    handle = open(path, "r+")       # May raise IOError
    try:
        data = handle.read()        # May raise UnicodeDecoderError
        op = json.load(data)        # May raise ValueError
        value =(
            op['numerator']/
            op['denominator'])      # May raise ZeroDivisionError
    except ZeroDivisionError as e:
        return UNDEFINED
    else:
        op['result'] = value
        result = json.dump(op)
        handle.seek(0)
        handle.write(result)        # May raise IOError
        return value
    finally:
        handle.close()              # Always runs
