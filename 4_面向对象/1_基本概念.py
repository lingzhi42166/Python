class Test():
  num = 1  # 类数据成员 可以通过类和实例对象调用 是共享的  如果通过类访问 那么值的修改是作用在类上的 
  def __init__(self):
    self.num1 = 2 # 对象的数据成员  只能实例对象调用

test = Test()
test.num+=1
print(test.num) # 是在实例对象上修改
test.num1+=1
print(test.num1)

test1 = Test()
print(test1.num)
print(test1.num1)

Test.num+=1
print(Test.num) # 是在类上修改
# print(Test.num1) type object 'Test' has no attribute 'num1'
print(test.num)
print(test1.num)
