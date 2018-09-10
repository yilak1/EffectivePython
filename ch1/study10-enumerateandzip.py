from random import *
# 看不懂
random_bits = 0
for i in range(64):
    if randint(0, 1):
        random_bits |= 1 << i
        print(random_bits)
# 字符串迭代
flavor_list = ['vanilla', 'chocolate', 'pecan', 'strawberry']
for flavor in flavor_list:
    print('%s is delicious' % flavor)
# 想知道索引，用range比较复杂
for i in range(len(flavor_list)):
    flavor = flavor_list[i]
    print('%d: %s' % (i+1, flavor))

# 同样的任务，使用enumerate解决
# emumerate 可以把各种迭代器包装成生成器，以便稍后产生输出值。生成器每次产生一对输出值
# 前一个表示索引，后一个表示值
for i, flavor in enumerate(flavor_list):
    print('%d: %s'%(i, flavor))

# enumerate 还可指定函数计数时所用的值,即初始值不是0而变成其他的
for i, flavor in enumerate(flavor_list, 2):
    print('%d:%s' % (i, flavor))

# 用zip函数打包同时遍历两个迭代器,
# zip 可以把两个或两个以上的迭代器封装成生成器，以便求值，这种zip生成器，会从每个迭代器中获取该迭代器的下一
# 个值。然后把这些值汇聚成tuple
# 如果提供的迭代器长度不等，那麽zip会提前终止,
# itertools 内置模块中zip_longest函数可以平行地遍历多个迭代器，而不在乎他们长度是否相等
name = ['Cecilia', 'Lise', 'Marie']
letters = [len(n) for n in name]
longest_name = None
max_letters = 0

for name, count in zip(name, letters):
    if count > max_letters:
        longest_name = name
        max_letters = count
