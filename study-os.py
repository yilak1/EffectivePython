import os.path
# os模块常用用法

# os.walk
# os.walk(top[, topdown=True[, onerror=None[, followlinks=False]]])
#  在目录树中游走输出在目录中的文件名，向上或者向下。
# top --是所要遍历的目录地址，返回三元组（root， dirs， files）
#     root：这个文件夹本身的地址，
#     dirs：是个list，表示该文件夹所有目录的名字（不包括子目录）
#     files：一个list，表示该文件夹中所有的文件（不包括子目录）

# 例子
# for root, dirs, files in os.walk(".", topdown=False):
#     for name in files:
#         print(os.path.join(root, name))
#     for name in dirs:
#         print(os.path.join(root, name))



# os.path

# 1.os.path.abspath(path) 返回path规范化的绝对路径
print(os.path.abspath("test.csv"))
print(os.path.abspath('../test.csv'))

# 2. os.path.split(path) 将path分割成目录和文件名二元组返回
print(os.path.split('/home/lds/code/machine-learning/test.csv'))

# 3. os.path.dirname(path) 其实就是os.path.split()的第一个元素
print(os.path.dirname('/home/lds/code/machine-learning/test.csv'))

# 4. os.path.basename(path),
# 返回path最后的文件名。如果path以／或\结尾，那么就会返回空值。即os.path.split(path)的第二个元素。
print(os.path.basename('/home/lds/code/machine-learning/test.csv'))

# 5. os.path.commonprefix(list) 返回list中，所有path共有的最长的路径。
print(os.path.commonpath(['/home/td', '/home/td/ff', '/home/td/fff']))

# 6. os.path.exists(path) 如果path存在，返回True；如果path不存在，返回False
print(os.path.exists('/home/lds/code/machine-learning/test.csv'))

# 7. os.path.isabs(path) 如果path是绝对路径，返回True。
# 8. os.path.isfile(path) 如果path是一个存在的文件，返回True。否则返回False。
# 9. os.path.isdir(path) 如果path是一个存在的目录，则返回True。否则返回False。
print(os.path.isdir('/home'))

# 10.os.path.join(path1[, path2[, ...]]) 将多个路径组合后返回，第一个绝对路径之前的参数将被忽略。
print(os.path.join('/home', 'test.csv'))

# 11 os.path.normcase(path) 在Linux和Mac平台上，该函数会原样返回path，
print(os.path.normcase('/home/lds/code/machine-learning/test.csv'))

# 12 os.path.splitdrive(path) 返回（drivername，fpath）元组
print(os.path.splitdrive('/home/lds/code/machine-learning/test.csv'))

# 13 os.path.splitext(path) 分离文件名与扩展名；默认返回(fname,fextension(.后面的扩展名))元组，可做分片操作
print(os.path.splitext('/home/lds/code/machine-learning/test.csv'))
# 14 os.path.getsize(path) 返回path的文件的大小（字节）。
print(os.path.getsize('/home/lds/code/py'))
# 15 os.path.getatime(path) 返回path所指向的文件或者目录的最后存取时间。
print(os.path.getatime('/home/lds/code/py'))
# 16 os.path.getmtime(path) 返回path所指向的文件或者目录的最后修改时间
print(os.path.getmtime('/home/lds/code/py'))