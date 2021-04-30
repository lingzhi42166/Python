""" 
  重载:
    指同一个作用域可以存在多个同名函数 通过参数的列表和定义不同区分
    当调用一个重载函数或重载运算符，编译器会自动将传形参和实参的数据类型 参数个数 进行对比 决定最合适的那个函数
    选择最合适的重载函数或重载运算符的过程，称为重载决策
    但是python是动态语言 不需要声明变量类型 所以Python支持重载 但大部分不需要重载

  运算符重载，就是对已有的运算符重新进行定义，赋予其另一种功能
"""

class Demo(object):
  def __new__(cls):
    pass
  def __init__(self,arr):
    self.arr = arr
    print(self.arr)
  def __add__(self,order):  # 重载运算符 两个实例对象进行运算时 自调用对应的运算符
    print(self.arr,order.arr)
# demo1 = Demo([1,2,3])
# demo2 = Demo([4,5,6])
# demo3 = Demo([4,5,6])
# demo1 + demo2
# print(Demo.__init__)


""" 如果执行类 重载new函数 不创建实例对象 那么返回的就是一个None对象  """
demo1 = Demo()
# print(demo1) # None
# print(dir(demo1))
# print(type(demo1)) # NoneType对象
# print(type(None)) # None的数据类型就是NoneType  
# print(demo1.__init__)
# print(dir(None))

""" 
  None特殊对象就是NodeType类型
  内部有系统定义的一些共同特殊成员
  ['__bool__', '__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']

"""




