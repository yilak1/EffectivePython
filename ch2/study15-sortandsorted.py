from operator import itemgetter, attrgetter
# 内置函数sort（）
# 原型：sort（fun， key， reverse=False）
# fun表明函数是基于何种算法排序的，一般情况下是归并排序，所以基本不用重写
# key 指定一个函数，此函数在每次元素比较时被调用，
# reverse表明是否逆序，False是升序，True是逆序

sorted([5, 2, 3, 1, 4])
a = [5, 2, 3, 1, 4]
a.sort()
print(a)
sorted({1: 'D', 2: 'B', 3: 'B', 4: 'E', 5: 'A'})

# key functioin，
# lambda为匿名函数 student：student[0] student为函数入口， student[0]为函数体，并返回该值
sorted("this is a test string from andrew", key=str.lower)
student_tuples =[
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10)]

sorted(student_tuples, key=lambda student: student[2])


class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age

    def __repr__(self):
        return repr((self.name, self.grade, self.age))


student_objects = [
    Student('john', 'A', 15),
    Student('jane', 'B', 12),
    Student('dave', 'B', 10)
]
print(sorted(student_objects, key=lambda student: student.age))

# Operator Module Function
sorted(student_tuples, key=itemgetter(2))
sorted(student_objects, key=attrgetter('age'))
# 支持多参数排序，先按照第一个排序再按照第二个排序
sorted(student_tuples, key=itemgetter(1, 2))
sorted(student_objects, key=attrgetter('grade', 'age'))

# 升序和降序
# reverse = True 降序，reverse = False 升序（默认）

# 复杂分类和稳固排序
# 按照第一个排序，如果有重复，就继续按照第二个属性
data = [('red', 1), ('blue', 1), ('red', 2), ('blue', 2)]
sorted(data, key=itemgetter(0))

s = sorted(student_objects, key=attrgetter('age'))
sorted(s, key=attrgetter('grade'), reverse=True)


# 了解如何在闭包里使用外围作用域中的变量
# 这个函数能正常工作基于三个原因：
# 1 python支持闭包：闭包是一种定义在作用域中的函数，这种函数引用了那个作用域里面的变量。如helper访问group
# 2 python的函数是一级对象，我们可以直接引用函数、把函数赋给变量、把函数当成参数传给其他函数，并通过表达式及if语句对其
# 比较和判断。于是我们把helper这个函数传给key参数
# 3 python 使用特殊规则比较两个元组。它首先比较下标为0的对应元素，如果相等，再比较下标为1的对应元素。如果还是相等那就
# 继续比较下标为3 的对应元素
def sort_priority(valuse, group):
    def helper(x):
        if x in group:
            return 0, x
        return 1, x
    valuse.sort(key=helper)


number = [8, 3, 1, 2, 5, 4, 7, 6]
group = {2, 3, 5, 7}
sort_priority(number, group)
print(number)


# 排序结果正确，但是found值不对，
# 表达式引用变量时，python解释器将按照如下顺序遍历各个作用域，以解析该引用
# 1 当前作用域，2 任何外围作用域，3 包含当前代码的那个模块作用域（也叫全局作用域） 4 内置作用域（也就是len str等
# 函数作用域），向上查找
# 而在赋值的时候不是这样，如果当前域没有，则会把这次赋值当作对该变量的定义，这样做是为了
# 防止函数中的局部变量污染函数外面的模块，如果不这么做，赋值会影响到外围，很容易出bug
def sort_priority2(numbers, group):
    found = False           # scope：sort_priority2

    def helper(x):
        if x in group:
            found = True    # scope: 'helper'--bad
            return 0, x
        return 1, x
    numbers.sort(key=helper)
    return found


found = sort_priority2(number, group)
print('Found', found)
print(number)


# 获取闭包内的数据
# 使用nonlocal，可以在给变量赋值的时候应该在上层作用域中查找该变量，其唯一限制就是不能跨模块
# nonlocal 建议只在极其简单的函数中使用
def sort_priority3(number3, group):
    found = False

    def helper(x):
        nonlocal found
        if x in group:
            found = True
            return 0, x
        return 1, x
    number.sort(key=helper)
    return found


found = sort_priority3(number, group)
print('Found', found)
print(number)


# 下面这个类与你nonlocal作用相同，理解很容易（其中__call__的特殊方法，见23条）
class Sorter(object):
    def __init__(self, group):
        self.group = group
        self.found = False

    def __call__(self, x):
        if x in self.group:
            self.found = True
            return 0, x
        return 1, x


sorter = Sorter(group)
number.sort(key=sorter)
assert sorter.found is True
