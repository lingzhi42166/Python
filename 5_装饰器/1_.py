""" 
  装饰器:
    装饰器就是一个函数 用来扩展另一个函数的功能
    比如计算另一个函数的代码执行时间
    给函数打日志
    类型检查
  开放封闭原则
    一个函数在项目中有多个地方使用
    如果一个函数针对于某个模块需要扩展功能的时候，直接修改函数源代码是会带来灾难性的毁灭的
    所以就可以通过装饰器 扩展这个函数的功能
    所以对于源代码是封闭的
    对于功能扩展是开放的
  @xxx   xxx会被执行 后面的函数是被修饰函数 作为参数传递给xxx
    def xxxx:
      pass
"""
def test(fn):
  print('hello')
  fn()

@test  # test执行  test2作为参数传递给test
def test2():
  print('world')

print(test2)

def test(fn):
  def wrapper():
    print('hello')
    fn()
  return wrapper

@test  # test执行  test2作为参数传递给test  变量test2指向 test的返回值
def test2():
  print('world')
def test3():
  print('test3')


print(test2)
test2()
test3()

""" 带参数的装饰器 """
from time import time,sleep

def logger(msg=None):#第一层
  print(1)
  def run_time(func): # 第二层
    def wrapper(*args, **kwargs): # 第三层
      start = time()
      func()                  # 函数在这里运行
      end = time()
      cost_time = end - start
      print("[{}] func three run time {}".format(msg, cost_time))
      return wrapper
    print(2)
    print(id(wrapper))
  print(id(run_time))
  return run_time

@logger('one') #如果装饰器传递了参数 那么返回的是第三层的函数 如果没有 则返回的是第二层的函数 换言之 如果是括号的方式调用了装饰器 默认会执行内部第一层函数 为的就是可以传递这个参数而已 
def fun_one():
  sleep(1)

print(id(fun_one))
# fun_one()
# @logger(msg="One")
# def fun_one():
#     sleep(1)
    
# @logger(msg="Two")
# def fun_two():
#     sleep(1)
    
# @logger(msg="Three")
# def fun_three():
#     sleep(1)
    
# fun_one()
# print(id(fun_one))
# fun_two()
# fun_three()

