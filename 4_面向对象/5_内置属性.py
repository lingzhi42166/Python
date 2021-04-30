
class Father:
  pass
class Test(Father):
  x = 1
  __y = 2
  def __init__(self):
    self.a = 'self.a'
    a = 'a'
  def test1(self):
    pass
  pass


test = Test()

print(test.__dict__) # （包含一个字典，由类的实例对象的数据属性组成）
print(Test.__dict__) # （包含一个字典，由类的数据属性组成）


print(Test.__module__) # 类定义所在的模块（类的全名是'__main__.className'，如果类位于一个导入模块mymod中，那么className.__module__ 等于 mymod）

print(Test.__base__) # <class '__main__.Father'> 元组形式返回类的所有父类 




