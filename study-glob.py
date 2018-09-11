import glob

# glob 模块 用它可以查找符合特定规则的文件路径名，跟windows路径搜索差不多
# 查找文件只用到三个匹配符：'*',  '?' , '[]'. ？匹配单个字符，[]匹配指定范围内字符， 如[0-9]匹配数字

# 获取指定目录下的所有图片
print(glob.glob('/home/lds/图片/*.png'))

# 获取上级目录中所有.py文件
print(glob.glob(r'../*.py'))

# glob.iglob
# 获取一个可编历对象，使用它可以逐个获取匹配的文件路径名。
# 与glob.glob()的区别是：glob.glob同时获取所有的匹配路径，而 glob.iglob一次只获取一个匹配路径。
# 这有点类似于.NET中操作数据库用到的DataSet与DataReader。下面是一个简单的例子：

# 父目录中的.py文件,f是个生成器generator
f = glob.iglob(r'../*.py')
print(f)
for py in f:
    print(py)