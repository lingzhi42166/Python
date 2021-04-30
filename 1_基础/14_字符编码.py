# coding:utf-8
""" 
  python2 默认是ASCII读文件的
  python3 默认是UTF-8读文件的  写文件默认是 cp936 等同于GBK

  所以UTF-8的py文件 用python2的解释器读 就会乱码

  所以需要指定字符编码
  除了编辑器可以指定  还可以通过
  # coding:utf-8
  # coding:ASCII
  # 来设置
"""
print('1')
print([1]*11)
print(list(zip([6,6],[1]*11))) 
print(range(10))
for i in range(10):
  print(i)
print(type(str(1)))