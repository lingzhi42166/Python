""" 
  object.__new__(类)
    创建一个类的实例对象

  类不是一个块级作用域
  当代码解释到class 的时候 是会进入代码块工作的
  当调用类的时候 就会自动执行该类的__new__ 和__init__函数
  __new__ 是创建该类的实例对象 并返回该实例对象
  然后再调用__init__并把__new__的返回值作为参数 
"""
class Person:
  x = 1

person = object.__new__(Person) # 执行类  实际上就是通过object.__new__ 创建实例对象的  init只是对new返回的实例进行初始化操作 如:添加属性
print(person.__init__())
print(person.x)  # 1

person1 = Person()
print(person1.x) # 1

class Demo(object):#程序解释(并没有调用类)到这里的时候是会进入代码块的
  print('Demo')# 打印 Demo
  total = 0    # 开辟内存空间
  def __new__(cls): # 定义函数   调用类以后 自动执行该函数  返回该类的实例对象 接着调用__init__函数 把实例对象作为参数传递给__init__
    print(cls,'cls') # cls 指向 类
    print(cls.total)
    obj = object.__new__(cls)
    print(id(obj))
    return obj
  def __init__(self):# 定义函数  调用类以后 自动执行该函数  接受该类的实例对象
    print(id(self))
    self.x = 1
  def __add__(self):# 定义函数
    print('add')

demo1 = Demo()  # 调用类==>实例化操作   实例化操作首先调用__new__方法创建实例对象 然后再自动调用__init__()并把实例对象作为参数传入
demo2 = Demo()
# print(Demo.self)



