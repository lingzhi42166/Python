""" 
  私有成员
    __开头的
    凡是__开头的 都是私有成员 内部使用
    (
      什么方式定义的就什么方式使用 如通过self.__xx定义 就通过self.__使用
      如果是类的命名空间中定义的 那么在类的命令空间中 可以直接访问  因为类不是函数 解释器会直接进来解释工作
      在类的实例方法等局部命名空间 就通过类.__xx 访问
    ) 
    外部只能通过实例对象._类名__xx
  
  _xxx   =>  保护成员 不能通过from module import引入
  _xxx__ =>  系统定义的特殊成员   会在满足某种条件时自动触发
  
  私有成员实现原理:
    任何形式为 __spam 的标识符（至少带有两个前缀下划线，至多一个后缀下划线）的文本将被替换为 _classname__spam
    因此 仅限从一个对象内部访问的“私有”实例变量在 Python 中并不存在 只是代码都遵循这样一个概念
"""
globalA = 'a'
class Father:
  __x = 1  # 私有成员 只能类自身访问 子类都不行 外部只能通过实例对象._类名__x
  print('自身访问',__x)
  print(globalA)

class Son():
  # __x = '__x'
  print(11111)
  def __init__(self):
    # print(super(Son,self).__x) # 此时super指向的就是Son的基类 'super' object has no attribute '_Son__x'
    # print(self._Father__x)
    # # print(__x)
    # self.__myx = '__myx'
    # self.myx = 'myx'
    pass
  pass
  

son = Son()
print(son.myx)
# print(son.__myx)'Son' object has no attribute '__myx'
print(son._Son__myx)


father = Father()
# print(father.__x) 'Father' object has no attribute '__x'
print(father._Father__x)


class Father:
  print(1)  #一行一行的执行 执行到这里就打印了  注意啊 类不是一个函数 所以不需要执行 解释器就会跑到里面来解释工作

def test():
  print('test')