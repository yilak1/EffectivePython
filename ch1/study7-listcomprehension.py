# 使用list comprehension 取代 map filter
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = [x**2 for x in a]
print(squares)

squares = map(lambda x: x**2, a)
# 计算那些可以被2整除的数平方
even_squarse = [x**2 for x in a if x % 2 == 0]
print(even_squarse)

# 不要使用含有两个以上表达式的列表推导
# 把矩阵简化成一维列表
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [x for row in matrix for x in row]
print(flat)

# 先执行最外层括号再执行里层括号,多加括号就多加一层维度
squared = [[x**2 for x in row] for row in matrix]

# 每一级循环的for表达式后面都可以指定条件
filtered = [[x for x in row if x % 3 == 0] for row in matrix if sum(row) >= 10]
print(filtered)

# 在列表推导式中，最好不要使用两个以上的表达式，可以使用两个条件两个循环，或一个条件搭配一个循环，
# 比这个复杂就要使用if 和for语句

# 用生成器表达式（generator expression）来改写数据量较大的列表推导
# 列表推导缺点：数据量较小时没问题，数据量较大，内存消耗大，会导致程序崩溃
# 生成器表达式会生成迭代器，而不会深入处理文件的内容

# 下面代码会输出迭代器对象
it = (x for x in a)
print(it)
# next（） 一个一个输出
print(next(it))
# 生成器可以相互组合，下面代码会把刚才那个生成器表达式所返回的迭代器用作另一个生成器表达式的输入值
# 每次执行外部迭代器都会推动内部迭代器
# 生成器表达式返回的迭代器是有状态的，用过一轮之后，就不要反复使用了
roots = ((x, x**5) for x in it)
print(next(roots))


