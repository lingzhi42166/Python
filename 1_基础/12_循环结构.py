# range控制循环次数  提供两个参数 第一个参数 代表从该参数值开始 到参数2-1停止
#条件不成立 或循环结束后 执行else  else主要用于 循环体内控制条件为不成立后执行else 比如给你三次登录机会 输入密码错误三次 则把循环条件设为false 被else捕捉执行
#break continue 不会执行else

# python3中range有一个优化  就是每循环一次 就在原本的内存空间中 更新值
# python2中是 range几个数 就开辟几个内存空间
for i in range(1,10):  #1~9 不包括10
  print(i)

for i in range(10):#0~9
  i += 1
else:
  print(i)

# while
i = 0
while i<100:
  i+=1
print(i)

i = 0
while i<100:
  i+=1
else:#条件不成立 或循环结束后 执行else
  print(i)

#break(结束所属层次的循环)  continue(提前结束本次循环 进行下一次循环 同样是同层次的) 跟js的一样  
#break continue 不会执行else
print('==========')
for i in range(10):  #==>  let i = 0 ; i<10  i++
  if(i==9):
    break
  print(i)#012345678
print('==========')
for i in range(10):
  if(i==8):
    continue
  print(i)#012345679


for i in ["1",'2','3']:
  print(i)

# 遍历 字典 返回key
obj = {"key":"value"}
for i in obj:
  print(i)
  print(obj[i])



for k,v in ([(0,0)]): 
  print(k,v) #   0 0

for k,v in [(0,0)]: 
  print(k,v) #   0 0