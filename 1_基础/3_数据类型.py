""" 
常见的就不列出来了

数据类型
  不同是数据需要定义不同的类型 根据不同的类型做出不同的处理

字符串: '123'  "123" '''123'''   还可以使用三引号作为界定符(三引号可以换行)   不可变序列 不可以通过下标修改元素值

列表: [1,2,3,x,[1,2]] 如js的 数组   可通过下标访问修改列表成员  列表存的是地址 

字典: {1:'food',2:'test'}  键值对  如js的 对象

元组: (2,-5,6)  不可变序列  也就是不可以通过下标修改元素值

文件: open('data.txt','rb')  open内置函数  使用指定模式打开指定文件 

集合: set('abc') ==> {'a','b','c'} 所有元素放在大括号中  元素不允许重复


函数是用 def 定义    如js中 function xx(){}
类 用 class定义      如js中 class xx{}


"""

print({'a','b','c'})
print(set('abc'))

x = [1,2,3]
print(x[1])

print('''
123
''')

# 用r''表示''内部的字符串默认不转义
print(r'\\\t\\')

# 元组 不可变序列
x = (2,-5.6)
# print(x[1]=1) 不可变序列


# python 中 取字典的属性 只能通过[]   . 是js中的 它会隐式转换成['']的  所以要记住
obj = {
  "x" : 1,
  "y" : 1
}
print(obj["x"])


# 字符串可以相乘
print("*"*10)
 


# 字符串常用方法
str = 'hello world'

# 切片 

print(str[:]) #不写起始位置和截至位置 默认就是从0 到末尾  等同于浅拷贝 这是python的一种优化 
print(str[0:len(str)])

print(str[0:5])   #下标 0~4

# 步长
print(str[0:5:2])   #下标 0 2 4

#反向步长
print(str[5:0:-2])  #下标  5 3 1
print(str[::-1]) #倒着取 

# 判断是否为字符串成员 
print('h' in str)

#移出字符串两侧空白字符   注意 字符串是不可变序列 所以移出空白符 不会修改原字符串 而是产生一个新的字符串
msg = '   hello world   '
print(msg.strip())
msg = '***hello world***'
print(msg.strip('*'))
msg = '***hello world***'
#只移出左边
print(msg.lstrip('*'))
msg = '***hello world***'
#只移出右边
print(msg.rstrip('*'))

#切分  split(分隔符，切分次数)   根据分隔符进行截取 返回一个新的列表
str = 'hello world'
print(str.split())  #默认以空格为分隔符
str = 'hello,world,!'
print(str.split(',')) 
print(str.split(',',1))   #只切分一次['hello', 'world,!']

print(str.rsplit(',',1)) #rsplit 从右往左切分 只切分一次['hello,world', '!']
 

#join 列表转字符串
list1 = ['1','2','3']
print(','.join(list1))


# 大小写转换   
str = 'Hello World'
str = str.lower()     #全部转换为小写
print(str)            
print(str.islower())  # 判断是否全为小写
str = str.upper()     #全部转换为大写
print(str)           
print(str.isupper())  #判断是否全为大写



#replace(匹配字符,替换字符值,替换几个)  替换字符串

str = 'you can you up no can no bb'
print(str.replace('you','YOU'))  #YOU can YOU up no can no bb
print(str.replace('you','YOU',1)) #YOU can you up no can no bb


#isdigit  判断字符串是否由纯数字组成
str = '123'
print(str.isdigit())
str = '123s'
print(str.isdigit())


# 查找子字符串起始索引
str = 'hello world'
print(str.find('h'))
print(str.index('h'))

print(str.find('!')) # -1   找不到返回-1
#print(str.index('!')) #ValueError: substring not found   找不到会报错


#填充字符 center liust rjust zfill
str = 'hello'
print(str.center(66,'*')) # 字符串居中并占66个字符  不够的   *    填充
print(str.ljust(66,'*'))  # 字符串左边对齐并占66个字符 不够的 * 填充
print(str.rjust(66,'*'))  # 字符串右边对齐并占66个字符 不够的 * 填充
print(str.zfill(66))      # 字符串右边对齐并占66个字符 不够的 0 填充


#expandtabs   设置制表符的空格数
str = 'hello\tworld'
print(str.expandtabs(10))

# captalize  swapcase title
str = 'hello world'
print(str.capitalize()) #字符串首字母大写
print(str.swapcase())   #字符串全部转换为大写
print(str.title())      #字符串每个单词首字母大写


""" 
  str.istitle()       判断字符串所有单词首字母是否为大写
  str.isalnum()       判断字符串是否为字母或数字组成的
  str.isalpha()       判断字符串是否全为字母组成
  str.isspace()       判断字符串是否全由空格组成
  str.isidentifier()  判断变量名是否合法的
  str.isnumeric()     判断是否为数字  包括中文数字 罗马数字    isdigit 不能判断中文数字和罗马数字 只能判断阿拉伯数字
  str.isdecimal()     判断是否为unicode数字
 
"""

""" 
  列表
    不能通过通过索引追加值  list[3] = 1 会报错 不存在3索引  跟JS不一样
    只能通过append()末尾追加值  insert(索引位,值) 插入值   extend() 迭代对象追加到列表(继承指定列表的所有成员)  内部就是for遍历值 追加到列表

    删除
      del list[x]
      list.pop(index) 删除指定索引成员 默认删除末尾  并返回被删除的成员值
      list.remove(value) 删除指定值的成员   没有返回值  Node

    检索
      count   检索指定值在列表中有几个
      index   返回 匹配到的第一个成员的索引值
    排序
      reverse() 列表倒序
      sort()    按照规则排序(大小)字符串就根据ASCII码表  默认升序   参数为reverse=True 就是降序

    列表之间也可以比大小 原理与字符串一样 但是双方对应的位置(成员)的元素必须是同种数据类型

"""
#增
list1 = [1,2,3]
#list1[3] = 1 #list assignment index out of range
list1.append(4)
print(list1)

list1.insert(0,0)
print(list1)

list2 = [5,6]
list1.extend(list2)
print(list1)

#删
print(list1.pop(0))
print(list1)

print(list1.remove(4))
print(list1)

#需要掌握的

#count 检索指定值在列表中出现的次数
list1 = ['a','a','a','b','a']
print(list1.count('a'))


#元组
t = (10,)
print(t)# (10,)
print(t[0]) # 10

t = (10)
print(t)#10
t = (10,11)
print(t)# (10, 11)

tuple1 = (1,)
tuple1+=(2,)
print(tuple1)#(1,2)

tuple1 = (1)
tuple1+=(2)
print(tuple1)# 3

#类型转换
print(tuple('hello'))




#字典
"""
  pop()     删除指定key 并返回对应的value 默认是末尾
  popitem() 随即删除一键值对 一般删除最后一个key 返回删除的键值对

  keys()   通过元组的形式 返回字典全部的key     ([])
  values() 通过元组的形式 返回字典全部的value值 ([])   默认遍历的是字典的key 如果想要遍历value 就可以利用这个方法
  items()  通过元组的形式 返回字典所有键值对    ([(),(),()])
  
  clear()       清除字典所有键值对

  update(obj)                       添加指定字典的所有键值对
  get(key，[,returnValue])          获取指定的key对应的value值  key不存在不会报错返回None 可以指定默认返回值  默认获取key不存在就会报错   js天生就是这个特性 不存在则返回Undefined   容错性好 
  setdefault(key,[,value])          返回字典中指定key对应的值 如果key不存在 则添加上指定的key 并把第二个参数作为value 如果没有指定value  则为None
"""
obj = {
  "a" : "aValue",
  "b" : "bValue",
  "c" : "cValue",
  "d" : "dValue"
}

print(obj.keys())
print(obj.values())
print(obj.items())# dict_items([('a', 'aValue'), ('b', 'bValue'), ('c', 'cValue'), ('d', 'dValue')])

print(obj.popitem())#返回并删除字典中的最后一对键和值。
print(obj.pop("c")) #删除指定key 并返回对应的value
print(obj.pop("b"))
print(obj)



#可以通过dict()创建字典

#给定key=value
print(dict(age='20')) # {'age': '20'}
#zip(keys,values)
keys = ['a','b','c']
values = [1,2,3,4]
print(dict(zip(keys,values)))# {'a': 1, 'b': 2, 'c': 3}

#fromkeys([key1,key2])创建指定值为建 value为空的字典
print(dict.fromkeys(['key1','key2'])) # {'key1': None, 'key2': None}


#update({})  把另一个字典的键值对 一次性全部添加到字典对象 如果两个字典有相同的键 则以另一个字典中的值为准进行更新
obj = {'a':'a'}
obj1 = {'b':'b'}

obj.update(obj1)

print(obj)

#del 删除整个字典或指定元素

del obj['b']
print(obj)

# del obj 删除整个字典
# print(obj)

#clear  清空字典对象中所有的元素  只是删除成员
obj.clear()
print(obj)

#get  
obj = {'a':'aValue'}
print(obj.get('a'))
# print(obj['b']) KeyError: 'b'
print(obj.get('b'))

#setdefault  获取指定key的value  如果key不存在 就会创建一个新的key 并把第二个参数作为value 如果没有提供第二个参数 就默认value 为 None
print(obj.setdefault('a'))
print(obj.setdefault('b'))
print(obj['b'])

""" 
  集合
    无序可变序列
    每个元素都是唯一的
    成员只能是 数字 字符串 元组 等不可变类型(修改直接换地址)，而不能包含列表 字典 集合等可变数据类型

    可以通过set()将列表 元组等可迭代对象(内部原理都是通过for循环)转换为集合
    如果原数据中有重复的元素，则转换为集合的时候只保留一个

    一般用于关系运算
      比如取交集 合集等

    集合去重的局限性
        因为是无序的 所以无法保证去重对象的顺序
        元素必须是不可变类型
"""

a = {6,6}
# a = {[1,2,3],6} TypeError: unhashable type: 'list'  只能是不可变类型
print(6)

# print(set([1,2,3,[4,5,6]])) 不可以嵌套列表
print(set([1,2,3])) # {1, 2, 3}


#取交集   两者共同的好友
a = {6,16}
b = {6}
print(a & b)  # {6}
print(a.intersection(b),'====') # {6}

#取合集
print(a|b) # {16, 6}
print(a.union(b))

#取独有成员   a 相对于 b 所独有的成员
print(a - b)# 16
print(b - a)# set()
print(a.difference(b))

#对称差集  求双方独有的成员  去除共有好友
print(a ^ b)  # {16}
print(a.symmetric_difference(b))

#父子集   包含关系   a 完整的包含 b 所有成员 a就是b的父亲
print(a > b)  # true  a 包含了 b 的所有成员  a 是 b 的 父亲
print(b < a)  # true  b 是 a 的儿子
print(a.issuperset(b)) # a是不是b的爹
print(b.issubset(a))   # b是不是a的儿子  子集

b = {6,16}
print(a == b) #True  a b 互为父子关系

""" 
  内置方法
    pop()       随机删除并返回该元素
    discard(vl) 删除指定元素 元素不存在不会报错
    remove(vl)  删除指定元素 元素不存在会报错
    clear()     清除所有成员

    add()       添加新元素
    update(集合) 把新集合添加到旧集合

    difference(集合) 求差集 并返回一个新的集合 
    differenct_updata(集合) 求差集 并将结果赋值给调用该方法的集合  => s = s.difference({})


    


    s.isdisjoint({}) 判断两个集合是否完全独立 没有共同部分 返回true

 """