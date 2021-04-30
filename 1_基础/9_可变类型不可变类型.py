# 不可变类型   不可以在原地址上 修改值

x = 1
fl = 1.5
str = '123'
print(id(x),id(fl),id(str))
x = 2
fl = 2.5
str = '123456'
print(id(x),id(fl),id(str)) #地址发生变化

# 可变类型   可以在原地址上修改值   这是引用数据类型  只有变量重新赋值 才会修改地址指向 
# 列表里面保存的是值的地址
list = [1,2,3]
print(id(list))
list[0] = 1.1
print(id(list))

dist = {0:0,1:1}
print(id(dist))
dist[0] = 00
print(id(dist))