""" 
  大部分语言中枚举是一个数据类型 (专门有一个关键字定义)
  但是在python 枚举是一个类  
  一系列常量的集合

  特点:
    不可变
    唯一性

  单列模式  实例化是没有意义的
"""

from enum import Enum

class VIP(Enum):
  BLUE = 1   # 枚举的标识符 用大写  因为枚举成员不可变的特性 和常量一样 所以用大写  归为一类
  SKYBLUE = 2 #  SKYBLUE为标签  2为类型(数值)
  BLUE1 = 1

print(VIP.BLUE,type(VIP.BLUE))       # 获取枚举成员 类型=>枚举类型

print(VIP.BLUE1) # 如果值相等 则等同于先定义的枚举类型的别名  值相等不能是独立的一个枚举类型  不会被遍历出来

print(VIP.BLUE.value,type(VIP.BLUE.value)) #获取标签值   类型=>值的类型

print(VIP.BLUE.name,type(VIP.BLUE.name))  #获取标签名   类型=>字符串

print(VIP.__members__)# {'BLUE': <VIP.BLUE: 1>, 'SKYBLUE': <VIP.SKYBLUE: 2>, 'BLUE1': <VIP.BLUE: 1>}

print(VIP.__members__.items()) # dict_items([('BLUE', <VIP.BLUE: 1>), ('SKYBLUE', <VIP.SKYBLUE: 2>), ('BLUE1', <VIP.BLUE: 1>)])

# VIP.BLUE = 1  #Cannot reassign members.  不能再分配成员。   reassign:重新委派（任务、职位、责任等）；再分配，再指定

# 遍历枚举类  并不会遍历别名
for i in VIP:
  print(i)

# 枚举的比较运算  只能做等值和身份比较  不同枚举类的成员比较 都是false
print(VIP.BLUE == VIP.SKYBLUE)  # false
print(VIP.BLUE == VIP.BLUE)     # true
print(VIP.BLUE == 1)            # false
# print(VIP.BLUE > VIP.SKYBLUE) # not supported between instances of 'VIP' and 'VIP' 在python中不行 某些语言可以
print(VIP.BLUE is VIP.BLUE)     # True


""" 
  类型转换(本质不是类型转换) 只是通过数值 访问对应的枚举成员
    数据库中存储的是枚举类型的值  占用空间更小
"""
a = 1
print(VIP(a)) # VIP.BLUE 
print(VIP(1)) # VIP.BLUE 



obj = {
  'a' : 'a'
}
print(obj.items())# dict_items([('a', 'a')]) 成员名和成员值组成一个元组


from enum import IntEnum,unique  
# Enum类 不会限制枚举成员数值的类型(可以是字符串)  IntEnum 限制只能是整型
# unique装饰器  限制 成员值不允许重复

""" 
  item 逐条列出  项目
  members 成员
  unique 独一无二的 稀罕的
"""
