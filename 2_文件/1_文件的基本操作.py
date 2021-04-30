""" 
  文件是操作系统提供给用户操作硬盘的接口
  
  文件是长久保存信息并允许重复使用和反复修改的重要方式，同时也是数据交换的重要途经

  文件分为文本文件和二进制文件两大类

  操作文件的基本流程
    打开文件创建文件对象，通过文件对象对文件内容进行读写删改


  通过open() 以指定模式打开文件并创建文件对象

  文件路径可以是 相对路径和绝对路径
    相对路径是相对于 运行python命令的 目录 => 当前工作目录

  利用 os.getcwd() 函数可以取得当前工作路径的字符串，还可以利用 os.chdir() 改变它


  
"""
import os
print(os.getcwd())# C:\Users\Administrator\Desktop\python
# os.chdir(r'C:\Users\Administrator\Desktop')
# print(os.getcwd())

# f = open('2、文件/README.txt','r')
# # f = open('2、文件\README.txt','r')
# #f = open(r'2、文件\README.txt','r')
# print(f)
# print(f.read())
# f.close()

""" 
  window默认是通过gbk编码打开文件
  linux下是utf-8

  由应用程序向操作系统发起系统调用open(...)，操作系统打开该文件，对应一块硬盘空间，并返回一个文件对象赋值给一个变量f

"""
f = open(r'C:\Users\Administrator\Desktop\python\note.txt','r',encoding='utf-8')
# print(f)
# print(f.read())
for line in f:
  print(line)
  break
f.close()

""" 
  文件操作遵循 打开文件 读写文件 关闭文件
  但是文件操作使可能产生错误IOError 一旦出错 就不会执行close 无法正常关闭文件
  那么我们可以通过try ...finally 或者 with  with和try是一样的 代码更简洁
  with里的代码块执行完毕后 会自动还原进入该代码块时的现场 还原案发现场

  with自带异常处理 只要代码体抛出异常 则直接关闭文件

"""
# try:
#   f = open(r'C:\Users\Administrator\Desktop\python\note.txt','r',encoding='utf-8')
# finally:
#   if f:
#     f.close()

# with open(r'C:\Users\Administrator\Desktop\python\note.txt','r',encoding='utf-8') as fs:
#   print(fs.read())


""" 
  文件的打开模式
  r 读取模式 默认模式 如果文件不存在会报错      指针指向头
  w 写模式 文件如果存在 会清空原有内容         指针指向头
  x 写模式 创建新文件 如果文件已存在 会报错     指向指向头
  a 追加模式 指针指向文件末尾 不会覆盖原有内容   指针指向尾
  b 二进制模式
  t 文本模式
  + 读写模式(与其他模式配合使用)

重点注意:
  注意如果使用+  就要留意指针的位置
  文件的读写操作都会自动改变文件指针的位置

  比如 读模式 打开一个文件 读取10个字符 那么指针就会自动移到第11个字符的位置
  再次读取的时候 就是从11字符的位置开始

  可以通过seek(offset[,whence]) 更改文件指针位置 
    offset相对于whence偏移的字节数  
    whence表示从哪个位置开始
      0为文件头开始  1为当前位置开始 2为文件尾开始
  tell() 返回文件指针当前位置
"""
f = open('test.txt','r+',encoding='utf-8')
f.write('123456')# 这里写入123456 那么指针就指向了第7个字符的位置
print(f.read())# 从第7个字符的位置读取
f.close()

f = open('test.txt','r+',encoding='utf-8')
f.write('123456')# 这里写入123456 那么指针就指向了第7个字符的位置
f.seek(0) # 更改文件指针 为文件头
print(f.read())# 从文件头开始读取
print(f.tell())# 返回文件指针当前位置

""" 
  文件对象的常用属性
    name 返回文件的名字
    closed 返回文件是否关闭
    mode  返回文件的打开模式
"""
print(f.name)
print(f.closed)
print(f.mode)
f.close()

""" 
  文件对象常用方法
    就不一一列举了 看书P209
"""
f = open(r'C:\Users\Administrator\Desktop\python\note.txt','r',encoding='utf-8')
print(f.readline()) # 读取当前指针指向的一行内容 并返回
# print(f.readlines())# 返回一个列表  列表成员为每行文本的字符串类型
f.close()

# 注意文件编码  不指定是utf-8 保存就会乱码  
f = open('test1.txt','w+',encoding='utf-8')
# f.read(1)
# f.truncate(2) # 删除从当前指针到文件末尾的内容  如果指定了size参数 那么不管文件指向在哪里 都保留文件的前size个字节   这里指定的是 保留文件的前2个字节
# f.seek(0,0)
# print(f.read())

f.write('写入文本\n换行再写入')
f.writelines(['列表模式\n','写入'])  # 把字符串列表写入文本文件
f.seek(0,0)
print(f.readline())
f.seek(0,0)
print(len(f.readline()))  # 返回当前行的字节  换行符也算一个字节
f.seek(0,0)
""" 
  文件对是可迭代对象

"""
for line in f:
  print(line)   # print默认末尾就会换行 如果输出的内容有换行符 就会出现打印出来的效果 多换一行
  print(len(line))



import json
x = {'a':1}
print(type(x))
y = json.dumps(x)
print(y,type(y))
y = json.loads(y)
print(y,type(y))


""" 
单词:
  truncate: 截断


"""