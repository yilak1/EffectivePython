
# 切割序列
# assert是断言如果真程序继续运行，假则报断言错误
# 要点1：不要写多余代码：当start索引为0, 或者end时省略
# 要点2：切片操作不会比较start与end索引是否越界 a[20:] a[-20:]
# 要点3：对list赋值的时候，如果使用切片操作，就会把原列表中处在相关范围内的值替换成新值，即便他们长度不同也可以替换
a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print(a[0:4])
print(a[-4:])
print(a[3:-3])
assert a[:5] == a[0:5]
assert a[5:] == a[5:len(a)]

# 要点2代码展示
first_twenty_items = a[:20]
last_twenty_items = a[-20:]

# 对原列表切割，会产生新的列表，系统依然维护原列表各个对象的引用
b = a[:4]
b[1] = 99
print(a, '\n', b)

# 对赋值操作右侧使用切片，把切片起止都留空，产生原文件拷贝
b = a[:]
assert a == b and a is not b
# 对赋值操作左侧使用切片，而没有指定索引，那麽系统会把右侧的新值复制一份，并且这份拷贝来代替左侧列表的全部内容
# 而不会重新分配新的内容
b = a
print('before', a)
a[:] = [101, 102, 103]     # 要点3的应用
assert a is b
print('After', a)

# 单次切片操作内，不要同时指定start，end，stride
a = ['a', 'b', 'c', 'd', 'e', 'f']
odds = a[::2]
evens = a[1::2]
print(odds)
print(evens)
# 字符串翻转
x = b'mongoose'
y = x[::-1]
print(y)
# 对于需要同时用到start，end，stride时，采用步进式
# 一步切割范围，一步步进切割
b = a[::2]
c = b[1:-1]
