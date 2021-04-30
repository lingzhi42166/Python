""" 
在python中一切皆对象  除了内置对象  还有大量的标准库对象和扩展库对象  标准库是python默认安装的 通过import 引入 
扩展库则需要自己安装后 再引入

1、python是强类型编程语言
但不同的是python不需要事先声明变量及其数据类型   直接赋值即可创建各种类型的对象
因为解释器会根据赋值或运算来自动推断数据类型

2、python是动态语言  所以变量的类型随时可以改变

变量是用来保存状态的  

常量:
  python中是没有常量的概念的  
  但是有一个约定   命名全为大写的 就是常量 告诉自己人 这是常量 别改
"""

x = 3
print (x)
x = 'hello world'
print (x)
""" python中数组是 列表对象 list   type是检测数据类型  对应js中的typeof """
x = [1,2,3]
print (type(x))  
""" 
isinstance(data,datatype) 内置函数   检测指定的数据(data)是否为指定的对象(datatype)的实例   对应js中的 instanceof 
这里表示的是   x变量  是不是list(列表)对象类型   返回 true false
"""
print(isinstance(x,list))


# 链式赋值
x = y = z = 10
print(x,y,z)
print(id(x),id(y),id(z))

# python中提供了一种语法 交叉赋值  类似于js中的 解构赋值 [x,y] = [y,x]
x,y = y,x
print(x,y)
# 下面的代码 等同于上面的操作  x 和 y 换值
x = 10
y = 20
print(x,y)

temp = x
x = y
y = temp
print(x,y)

# 解压赋值  也是相当于 js中的解构赋值 
x,y,z = [1,2,3]
print(x,y,z)

arr = [1,2,3]
x,y,z = arr
print(x,y,z)

# *变量名 获取没有对应关系的值  注意和 js中的 rest参数不一样 res参数是把剩余的全部获取到
# *  只会获取没有对应关系的  看下面的案例

# x,y,z = [1,2,3,4,5,6]  报错

# 获取没有对应关系的值作为列表存到变量 _
x,y,z,*_ = [1,2,3,4,5,6]
print(x,y,z,_) #1 2 3 [4, 5, 6]
# 下面案例就证明了 * 只获取没有对应关系的值
*_,x,y,z = [1,2,3,4,5,6]
print(_,x,y,z) # [1, 2, 3] 4 5 6

x,*_,y,z = [1,2,3,4,5,6]
print(x,_,y,z) # 1 [2, 3, 4] 5 6

# 解压字典  只获取 key
x,y = {'x':1,'y':2}
print(x,y)


x,y = (6,6)
print(x,y)





