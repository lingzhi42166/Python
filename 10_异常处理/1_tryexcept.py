""" 
  异常和错误的概念是不一样的
    错误一般分为逻辑错误和语法错误,都是程序员的问题，这类错误是在开发的时候就可以通过报错信息 及时处理的
    不然代码是无法正常运行的

    异常:
      运行过程中，由于某些条件引发。主要是各种客观因素决定的 比如用户的操作问题等
      异常会一层层的往外抛 直到最后还是没被捕捉 就显式报错 代码无法正常运行

      捕捉异常 执行对应处理的代码 避免程序无法正常运行

      try:
        ...
      except 异常种类 as 命名:  明确捕捉指定异常类 有针对性的编写相应的代码    p254 异常类结构

      try:
        ...
      except:
        如果try代码体出错 则被我捕捉
      else:
        如果没有出错 则执行我

      try:
        ...
      except:
        如果try代码体出错 则被我捕捉
      finally:
        无论代码是否引发异常(异常是否被捕捉) 最终都会执行我
"""
print('======')
try:
  int('a') 
except Exception as e: # 明确捕捉Exception异常类 错误信息存到变量e
  print(e,'\n')

try:
  int('a') 
except:
  print('错误\n')  


try:
  print("我没错")
except:
  print('错了就来我这，别影响程序运行')
else:
  print('你没错，真棒')



""" 
  单词:
    identifier 标识符
    Exception  例外 除外 除外
    finally    最后 终于
    finish     完成
    syntax     语法
"""