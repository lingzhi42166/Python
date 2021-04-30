
from multiprocessing import Process,Lock,Queue
import time

""" 
  创建多进程不建议使用全局变量
    在Windows中，进程不像Linux / Unix中那样 fork 。
    相反，它们是 spawned ，这意味着将为每个新的 multiprocessing.Process 启动一个新的Python解释器。这意味着所有全局变量都将重新初始化
  并且进程间 数据不共享 相互独立
  所以即使是子进程 也要通过别的方式操作主进程或者别的进程的数据
"""
# surplus = 10
# print(1)  # 不知道为什么也会执行10次  http://c.biancheng.net/view/2633.html 跟这里说的相反


# 查票方法
def checkMethod(l,i,q):
  l.acquire()
  print('{i}来查票了'.format(i=i))
  surplus = q.get()
  if(surplus>=1):
    shop(i,q,surplus)
  time.sleep(1)
  l.release()

def shop(i,q,surplus):
  # global surplus
  # surplus -= 1  #python中 函数内部涉及变量赋值 默认都是局部作用域的  所以想要在函数内定义全局变量或者修改全局变量 必须通过global声明 但是这里因为是进程间通信 不共享数据 所以不能操作全局变量 实现效果
  surplus -= 1
  q.put(surplus)
  print('{i}购买成功,还剩{num}张'.format(i=i,num=surplus))



if __name__ == '__main__':
  lock = Lock()
  q = Queue()
  q.put(10)
  for i in range(1,11):
    p = Process(target=checkMethod,args=(lock,i,q))
    p.start()
  