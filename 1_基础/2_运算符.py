x = 3
""" ** 是幂乘运算符  这里表示的是 x的2次方  == 9  """
print(x**2)

# 只保留整数部分   不会进行四舍五入
print(x // 2)

# 取余
print(10%3)


"""
注意浮点数的运算 会因为精度问题 出现奇葩的结果  这是通病 所以永远不要拿浮点数做比较  比如这里0.1+0.2=0.30000000000000004
这是基于IEEE754数值的浮点计算的通病   ECMAScript也是这样
"""
print(0.1+0.2)

""" 
内置支持复数运算 
形如 x = a + bi   这种称之为复数
a是实部 b是虚部  i是虚数单位
将复数的实部与虚部的平方和的正的平方根的值称为该复数的模，记作∣a∣
"""
x = 3 + 4j
y = 5 + 6j
print(x+y)
print(x-y)
print(x*y)
print(x/y)


""" abs函数可求出复数的模 """
print(abs(x))

""" imag属性 => 虚部  """
print(x.imag)

""" real属性 => 实部 """
print(x.real)

""" 
conjugate()函数 => 共轭复数
对于复数 x = a + bi  称 x = a-bi为 x 的 共轭复数。 即两个实部相等，虚部互为相反数的复数 互为共轭复数
 """
print(x.conjugate())


""" 
python标准库  fractions中的Fraction对象支持分数运算  
从 fractions 库中  引入  Fracion对象  类似于 javascript中的  import xx from xxx  从xxx模块引入其模块导出的xx对象
Fracion(分子，分母)  通过Fraction函数创建分数
"""
from fractions import Fraction
x = Fraction(3,5)
y = Fraction(3,7)
print(x)
print(y)
""" numerator属性 => 分子 """
print(x.numerator)

""" denominator属性 => 分母 """
print(x.denominator)

print(x+y)
print(x*y)
print(x*2)


""" 注意 浮点数相减  会有偏差 """
print(0.3-0.2)


""" 
  逻辑运算符   运算符两侧会 隐式转换 为 布尔类型
    and  逻辑与
    or   逻辑或
    not  逻辑非

"""

if(1 and "true"):
  print("true")

if(1 > 6 or "true"):
  print("true")

if(not 0):
  print("not false")

""" 
  成员测试运算符  
    判断指定值是否为其成员
    x in y
    x not in y   x不是y的成员

    js的in是判断指定属性是否在指定对象的原型链上
"""
print("========")
print(1 in [1,2,3])
print(4 in [1,2,3])
print("1" in {"1" : 1})
print("2" not in {"1" : 1})





