""" 
  遍历指定目录
  返回目录下的 目录的绝对路径 和 当前目录的子目录列表 和 当前目录下的文件列表
  一直遍历到没有目录为止  
  
"""
import os
import os.path
print(os.getcwd())
# print(os.walk(os.getcwd()))
list1 = os.walk(os.getcwd()) # os.walk() 遍历指定目录  返回目录树对象  可迭代对象

for i in list1:
  print(i)  # 返回一个元组 元组有三个成员 分别是 目录的绝对路径,[子目录列表],[目录下的文件列表]

""" 
  返回指定path下的目录和文件
  os.listdir(path)  返回一个列表 列表成员是该path下的目录和文件
"""
# 默认的工作目录为运行python命名的目录  可通过chdir修改
os.chdir('2_文件')
# . 为当前工作目录
file_list = os.listdir('.') 
print(file_list) #['1_文件的基本操作.py', '2_二进制文件操作.py', '3_标准库操作文件文件夹.py', 'README.txt']
for i in file_list:
  pos = i.rindex('.') #rindex 返回子字符串 str 在字符串中最后出现的位置
  # print(pos)
  print(i[pos+1:])  # 字符串 切片  利用该方法可以返回 文件的 扩展名
  if(i[pos+1:] == 'py'):
    print('这是py文件，可以通过rename(oldfilename(旧的文件名 如果不是当前目录下的 需要文件的路径),newname(新的文件名)) 更改文件名')
  else:
    print('这不是py文件')

print(os.path.dirname('a/b/c'))
