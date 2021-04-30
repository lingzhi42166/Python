from multiprocessing import process
import os
import time

def f(name):
  print('module name:',__name__)
  print(os.getppid())  # 获取父进程id   父进程是 终端  通过终端启动进程 作为 python.exe的载体  运行python.exe  
  print(os.getpid())  # 获取当前进程id  当前进程 是 python.exe  因为python的代码是通过python.exe解释的 在python.exe中运行的

if __name__ == '__main__':
  f('test')
  print(os.getpid())
  time.sleep(30)
