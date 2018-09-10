# 尽量用异常来表示特殊情况，而不要使用None
# 因为None和0以及空字符串之类的值，在条件表达式里都会评估为False
# 遇到特殊情况应该抛出异常，而不要返回None。
# 下面是正确例子
def divide(a, b):
    try:
        return a/b
    except ZeroDivisionError as e:
        raise ValueError('Invalid inputs') from e


x, y = 5, 2
try:
    result = divide(x, y)
except ValueError:
    print('Invalid inputs')
else:
    print('Result is %.lf' % result)


# 错误例子,只有分母为0 才返回错误输入，而本例子分子为0也会返回错误输入
def divide(a, b):
    try:
        result = a/b
    except ZeroDivisionError:
        return None


x, y = 0, 5
result = divide(x, y)
if not result:
    print('Invalid inputs')
