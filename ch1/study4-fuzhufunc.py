from urllib.parse import parse_qs

# 辅助函数使用,

# 输出字典，空值字典保留
my_values = parse_qs('red=5&blue=0&green=', keep_blank_values=True)
print('Red:', my_values.get('red'))
print('Green', my_values.get("green"))
print('Opacity', my_values.get('opacity'))

# 对于待查询的参数没有出现在字符串中，或者空值时能输出0的方法
# get[k[,d]] if k in D, else d   返回的是列表我们需要访问第一个元素来判断即values[0]
# 使用or boolean表达式 a or b， if a = True ，else b
# 空字符串，空列表，0值，都会评估为False

red = my_values.get('red', [''])[0] or 0
green = my_values.get('green',[''])[0] or 0
opacity = my_values.get('opacity', [''])[0] or 0

# 确保这些参数为整数我们还需要int函数
red = int(my_values.get('red', [''])[0] or 0)

# 上种写法不容易读，我们做改进使用 if else 三元操作符
red = my_values.get('red', [''])
red = int(red[0]) if red[0] else 0

# 现在我们应该总结成辅助函数了，最终写法如下
def get_first_int(values, key, default=0):
    found = values.get(key, [''])
    if found[0]:
        found = int(found[0])
    else:
        found = default
    return found


green = get_first_int(my_values, 'green')
