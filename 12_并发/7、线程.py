""" 
  概念:
    操作系统调度和分配处理器时间的基本单位，负责执行进程地址中的代码
    运行代码的执行单元
    一个进程被创建时，系统会自动为之建立一个线程，称之为主线程
    一个进程可以有多个线程，主线程根据需要自动创建其他子线程
    线程之间数据共享(共享进程的地址空间)
  原理:
    CPU每个核可以运行一个线程
    如果多个线程同时运行，且多于核的数量，就需要进行调度
    调度就是处理器为每个线程分配了一个很短的时间片，根据调度算法轮流获得该时间片

  threading模块提供了操作线程常用的方法和类
  其中Thread类是用来创建和管理线程的
    实例化得到线程对象
"""
from threading import Thread
import time
def task_test(index):
  print(index)
  time.sleep(6)
  print('线程结束')

if __name__ == '__main__':
  t = Thread(target=task_test,args=(0,)) # 创建线程
  t.start() # 启动线程  自动调用run方法
  print(t.is_alive())
  t.join(1) # 等待线程结束 如果指定了参数(等待时间) 则线程在指定参数的值内未结束时 会把控制权交回给主进程
  # t.join()
  print('结束')
  print(t.is_alive()) # 判断线程是否还存活 这里还为True 是因为我们设置了等待时间为1秒 超过一秒线程还未结束 CPU的控制权就交回给主线程了




