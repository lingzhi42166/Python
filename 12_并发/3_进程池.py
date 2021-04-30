""" 
  如果要启动大量的进程，可以通过进程池的方式批量创建子进程
  multiprocessing提供了Pool对象 创建进程池
  由于Pool的默认大小是CPU的核数，如果你不幸拥有8核CPU，你要提交至少9个子进程才能看到上面的等待效果。
"""
from multiprocessing import Pool
import os
import time

def task_test(index):
  print('run task %s' %index)
  time.sleep(3)

if __name__ == '__main__':
  print('parent process %s' %os.getpid())
  p = Pool(6) # 创建一个可容纳6个进程的进程池
  for i in range(6):
    p.apply_async(task_test,args=(i,)) #异步申请一个进程
  p.close()
  p.join()
  print('done')
