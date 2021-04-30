""" 
  multiprocessing提供了 Queue对象进行进程间的数据交换
  队列使用的是IFIO先进先出的数据结构
  该案例实现了一个生产者消费者模型
  q.get() 获取队列数据
  q.put() 向队列推送数据
  q.empty() 队列是否为空 空 返回True
  
  IPC机制:  
    进程间通信
      socket 套接字
      Queue  队列
    
"""

from multiprocessing import Queue,Process

# 消费者
def task_read(q):
  onOff = True
  while onOff:
    print('我读取队列中的数据:%s' %q.get())
    onOff = False if q.empty() else True
# 生产者
def task_write(q):
  for i in range(10):
    q.put(i)

if __name__ == '__main__':
  q = Queue()
  p1 = Process(target = task_read, args = (q,))
  p2 = Process(target = task_write, args = (q,))
  p1.start()
  p2.start()
  p1.join()
  p2.join()
  print('done')