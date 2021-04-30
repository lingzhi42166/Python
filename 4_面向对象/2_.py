""" 
  注意python并没有对私有成员提供严格的访问保护机制
    可以通过实例对象._类名__私有成员名  访问  虽然这是破坏类的封装性的 但是无法阻止有人这个做

  

  注意self不是关键字  可以换成任意名称  但遵循约定的一种美德

  通过内置函数获取对象的属性
    getattr(obj, name[, default]) : 访问对象的属性。
    hasattr(obj,name) : 检查是否存在一个属性。
    setattr(obj,name,value) : 设置一个属性。如果属性不存在，会创建一个新属性。
    delattr(obj, name) : 删除属性。

  绑定方法和非绑定方法
    绑定方法:
      在类中正常定义的函数 都是绑定在实例对象上的
      通过@classmethod装饰器装饰后的函数  是绑定类上的  但是实例对象和类都可以调用 只不过自动传入的第一个参数始终是类   容易混淆
    非绑定方法:
      通过@staticmethod装饰器装饰后的函数 是非绑定的  不会自动传入第一个参数  类和实例对象都可以调用
"""

class A:
  x = 1 # 类变量  
  def __init__(self,param):  # __init__ 是构造函数(创建类的实例)  执行类 就会自动执行构造函数 返回实例对象(self代表实例对象)
    print(self) # <__main__.A object at 0x000001EFFB8C5B80>
    print(param)# 2
    print(self.__class__) # 实例对象的__class__方法 可以访问类  <class '__main__.A'>
  
  def test(self):  # 实例方法
    self.testA = 'A'  # self指向调用函数的实例对象 所以执行test的时候 会往该实例对象添加testA属性
    print('==')
    print(A.x)
    print('==')

  def __test1(self): # 实例对象的私有方法 一般用于内部操作 如果外部需要调用 则需要 实例对象._类__私有成员名
    print('__test1')

  def test2(self):
    self.__test1()
    A.classMethod()

  def __del__(self):  # 析构函数 __del__ ，__del__在对象销毁的时候被调用，当对象不再被使用时，__del__方法运行：
    class_name = self.__class__.__name__
    print(class_name,'销毁')
    
  @classmethod  # 修饰器 声明类方法  可以通过实例和类访问
  def classMethod(cls):  # 第一个参数表示类本身 cls非关键字
    print('classMethod')

  @staticmethod # 修饰器 声明静态方法 可以通过实例和类访问
  def staticMethod():
    print('staticMethod')


a = A(2)  # => 执行init方法 返回实例对象  参数被init接受  实例对象可以访问 类的所有方法和属性 相当于有一个原型链 顺藤摸瓜
print(a.__class__.x) # 1
print(a)  # <__main__.A object at 0x000001EFFB8C5B80>

A.classMethod()
a.classMethod()

A.staticMethod()
a.staticMethod()

a.test()
print(a.testA)


a._A__test1()

a.test2()

# 属性查找顺序 优先从自身的__dict__ 未找到 就从类的__dict__查找
print(a.__dict__)
print(A.__dict__)

del a

