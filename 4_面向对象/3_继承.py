""" 
  通过给类指定参数的方式 继承父类  默认继承object
  如果子类内部想要使用父类的方法和属性就需要显式的调用
    通过父类.xx
    或者super(类名,self).xx
    python3中可以直接super().xx
  如果子类没有重写__init__构造函数 默认自动调用父类的构造函数
  如果重写了 那么也可以通过显式调用的方式访问到父类的构造函数
  
  通过super调用父类的方法 其self不是父类的self 而是基类的self

  成员查找机制:
    先从实例自身查找，如果没有再从类查找 类没有再从父类查找
    Python支持多继承 搜索机制 从左往右

"""

class Father:  # 基类 父类 超类
  father = 'father'
  def __init__(self):
    # super().__init__()
    x = 1  # 执行完 回收帧 内存空间被清理  所以x 只是函数执行时产生 执行完毕随着作用域销毁而销毁
    self.y = 2 # 定义在实例对象上的
    print('如果子类(派生类)没有重写__init__构造函数，那么会自动调用父类(基类、超类)的构造函数')
  def fatherMethod(self):
    print('调用父类方法')

class Son(Father):
  # print(Father.father)
  # Father().fatherMethod()
  def sonMethod(self):
    super(Son,self).fatherMethod()
    print(super(Son,self).father)


son = Son()
son.sonMethod() # 调用父类方法

