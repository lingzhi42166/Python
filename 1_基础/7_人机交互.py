""" 
python3中输入的值都是作为字符串存储 
注意 python2中的input是 输入的什么类型就是什么类型
"""
username = input("please input:")
print(username,type(username))

# eval 只接受字符串   计算并返回字符串s中表达式的值  返回是int数据类型
username = eval(username)
print(username,type(username))

# int只能转换整数  所以 就需要 eval了
# username = int(username)
# print(username,type(username))
