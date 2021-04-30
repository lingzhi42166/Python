""" 
  执行模块源代码
  创建一个命名空间存放源文件执行过程中产生的名字  =>模块的属性

  模块搜索路径:
    先从当前目录 如果没有则从sys模块的path变量(列表)指定的目录查找
    可以通过append() 向其添加扩展搜索路径
"""
import sys # 引入模块  创建一个sys命名空间  sys模块里面的属性方法都是该空间下的成员
import testPage

print(testPage.x)
testPage.test()

""" 
第一次导入模块已经将其加载到内存空间了，之后的重复导入会直接引用内存中已存在的模块，不会重复执行文件
"""
from testPage import test  # 引入模块指定的对象  挂载在当前命名空间  会与当前命名空间的名字有命名冲突
from testPage import test as mytest # 在当前作用域中挂载对象 并以 as 指定的值 命名
test()  
mytest()
# 以上两个都是同一个对象

# print(sys.modules) 查看内存中已经加载的模块

print(sys.path) # 获取搜索模块的路径 
from testPage import *   # 引入模块所有的成员 都引入在当前全局命名空间  

