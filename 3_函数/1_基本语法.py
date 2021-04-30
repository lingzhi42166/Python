def fn(x,y=1):
  print(x+y)
fn(1)
print(fn.__defaults__)# 可以使用__defaults__ 查看函数所有默认值参数的值

""" 
  关键参数可以按参数名字传递值 实参顺序和形参可以不一致 

"""
def fn(x,y):
  print(x,y)
fn(y=1,x=2)
# print(fn(1,2))  默认返回None

""" 
  默认值参数只在第一次调用的时候解释
  如果多次调用有默认值参数的函数 并且不为默认值参数赋值
  那么该参数的值始终指向的是同一个内存地址  该特性叫 可记忆性
  再次调用该函数 并且不为默认值参数赋值 那么该参数还是上一次调用的结果
"""
def fn(list=[]):
  list.append(0)
  print(list)
fn()
fn()

""" 
  可变长度参数  类似于ES6的rest参数 但是功能更强大
   *parm  接受任意实参并放在一个元组中 赋值给形参parm
   **parms 只接受像关键参数一样显式赋值的实参并放在一个字典中 赋值给形参parms
"""
def demo(*param,**params):
  print(param,params) # (1, 2, 3, 4, 5, 6) {'x': 1, 'y': 2}
demo(1,2,3,4,5,6,x=1,y=2)

""" 
  序列解包
    传递多个参数的时候 可以使用*对实参(可迭代对象 内部通过循环迭代出每一个元素)进行解包
    ** 进行关键参数解包 也就是显式赋值 key=value
    也就是和 可变长度参数 反着来

    注意序列解包必须在关键参数解包之前用
    换言之 关键参数解包必须在序列解包后用

  字典对象作为实参时 默认键为参数
  如果需要键：值 则需要items() 返回字典所有键值对
  需要值  则需要 values()
"""
def demo(x,y,z):
  print('参数序列解包',x,y,z)

l = [1,2,3]            # 参数序列解包 1 2 3
d = {'x':1,'y':2,'z':3}
demo(* l)         # => 123                          参数序列解包 1 2 3
demo(* d)         # =>x,y,z                         参数序列解包 x y z
demo(* d.items()) # =>('x', 1) ('y', 2) ('z', 3)    参数序列解包 ('x', 1) ('y', 2) ('z', 3)
demo(* d.values())# =>1 2 3                         参数序列解包 1 2 3

def demo(*parm):
  print(parm)# (1, 2, 3)
l = [1,2,3]
demo(* l)

def demo(x,y):
  print(x,y)
d = {'x':1,'y':2}
demo(** d)  #  => x = 1, y = 2


"""
  局部变量和全局变量 概念都一样
  不同的是 python中局部作用域中想要定义全局变量或者使用全局变量 必须通过global关键字 声明

"""
print('==============')
def demo():
  global x
  x = 1

demo()
print(x)

y = 1
def demo():
  global y
  print('y={y}'.format(y=y))
demo()
