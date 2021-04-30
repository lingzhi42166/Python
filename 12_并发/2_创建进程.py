from multiprocessing import Process
import os
import time
def f(*param):
  print(param)
  print('父进程id:{id}'.format(id=os.getppid()))
  print('子进程id:{id}'.format(id=os.getpid()))
  time.sleep(60)


if __name__ == '__main__':
  print('当前进程id:{id}'.format(id=os.getpid()))#python解释器执行的  进程
  print('当前进程的父进程id:{id}'.format(id=os.getppid()))#启动python解释器命令的终端 的进程
  p = Process(target=f,args=('one','two'))  # 实际上 再创建一个新的进程 作为python.exe的载体 把target指定的函数 载入python.exe 执行解释
  p.start() # 启动p进程 
  
  p.join()  # 挂载 直到 p 进程结束
  print('子进程运行完毕')
  print('父进程运行完毕')
  
  time.sleep(6)