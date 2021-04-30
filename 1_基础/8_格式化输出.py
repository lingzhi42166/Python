# 字符串格式化输出  %
# 根据位置取值
msg = 'hello %s' %"world"
print(msg)

# 根据key取值
msg = 'hello %(value)s' %{'value':'world'}
print(msg)


# 注意%d只能接受int 

msg = '数字%d' %1
print(msg)


# str.format 速度次于变量赋值 比%快  但是兼容性好

#按索引 
str = 'hello {0}{1}{2}{3}{4}'.format('w','o','r','l','d')
print(str)

# 根据key
str = 'name: {name} , age: {age}'.format(name='Ling',age=20)
print(str)


# 直接变量   python3.5推出的   速度最快
x = 1
str = '数字{x}'
print(x)

# f''     碰到{} 会执行{}里面的代码
print(f'{{{x}}}')
print(f'number:{x}')
print(f'1+2+3')
print(f'{1+2+3}')

# python3新增语法  字符不够 指定值来凑  类似于 C
msg = 123
# msg占10个字符  >是代表输入字符的位置 这个代表右边  <代表向左对齐   ^代表居中  如果输入的值不够10个则用= 来替代
str = f'{msg:=>10}'
print(str)
str = f'{msg:=<10}'
print(str)
str = f'{msg:=^10}'
print(str)

# :.3f  四舍五入保留三位小数
print(f'{123.3567:.3f}')

#设置默认的结束符号  默认是换行   空 为 取消换行
print('hello',end='')
print('world',end='*')