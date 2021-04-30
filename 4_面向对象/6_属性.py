""" 
  即使是通过 __ 定义了私有成员 但还是提供的方法可以在外部访问修改
  python3中新增了特性 提供了更全面的保护  

"""
class Test:
  def __init__(self):
    self.__value = 1
  @property
  def value(self):
    return self.__value

test = Test()
print(test.value)

# property() 
class Test:
  def __init__(self):
    self.__value = 1
  def __get(self):
    return self.__value
  def __set(self,vl):
    if(vl>3):
      print('值不允许大于3')
      return
    self.__value = vl
  def __del(self):
    del self.__value
  
  value = property(__get,__set,__del) # 通过property 设置value为可读可写可删除属性
  # value = property(__get,__set) # 通过property 设置value为可读可写属性
  # value = property(__get) # 通过property 设置value为可读属性

test = Test()
print(test.value)
test.value = 4
del test.value
# print(test.value)'Test' object has no attribute '_Test__value'


class Test:
  def __init__(self):
    self.__value = 1
  def __get(self):
    return self.__value
  def __set(self,vl):
    if(vl>3):
      print('值不允许大于3')
      return
    self.__value = vl

  value = property(__get,__set)

  def __del__(self):  # 析构函数 __del__ ，__del__在对象销毁的时候被调用，当对象不再被使用时，__del__方法运行：
    class_name = self.__class__.__name__
    print(class_name,'销毁')

test = Test()
print(test.value)
# del test.value    can't delete attribute


