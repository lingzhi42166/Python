""" 
  列表推导式
    [表达式 for 变量 in 可迭代对象]
  循环执行表达式 执行结果作为列表的元素

  逻辑上就是一个循环 只是形式更加简洁
"""

x = [x+1 for x in range(10)]
print(x)

# 等同于下面的代码
x = []
for i in range(10):
  x.append(i+1)
print(x)



