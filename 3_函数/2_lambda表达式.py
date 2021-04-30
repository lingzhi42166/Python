""" 
  lambda 声明匿名函数
"""
f = lambda x,y,z : x+y+z  # =>   f = function(){}
print(f(1,2,3))

# map(fn,list) 对原元素进行加工 返回一个map可迭代对象 
result = list(map(lambda x: x+1 , [1,2,3]))  # map(function(x){return x+1},[1,2,3])
print(result)

""" 
  注意作用域问题

"""

""" 
  出现以下问题是因为 i 是全局变量
  当执行函数的时候 根据指令找到i的地址 i已经是9了
  可以通过闭包 或者 默认值参数 解决
"""
r = []
for i in range(10):
  r.append(lambda : i)
print(r[0]()) # 9
print(r[1]()) # 9

# 默认参数
r = []
for i in range(10):
  r.append(lambda x= i : x)
print(r[0]()) # 0
print(r[1]()) # 1

# 闭包
r = []
for i in range(10):
  def fn(x):
    return lambda : x  # 在定义的时候 其作用域链上就有fn的作用域  调用的时候 先从最近的作用域开始找变量

  r.append(fn(i))

print(r[0]()) # 0
print(r[1]()) # 1
