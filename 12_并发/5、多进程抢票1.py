""" 
  多进程模拟并发抢票:
    并发编程一定程度上，提高了机器利用率 吞吐量 但是也随之带来了一些麻烦
    多进程编程时候，如果不做处理，就会出现以下问题:
      当仅剩一张票的时候，如果三台电脑同时查询 那么都是收到还有一张票的信息，处于可下单状态
      但是如果其中一台电脑抢先下单了，那么其他电脑再下单就会造成三个人买的是一张票
    解决方案:
      使用Lock互斥锁(同步锁)
"""


from multiprocessing import Process,Lock
import time


def u_lock(l,i):
  print('{i}来买票了'.format(i=i))
  time.sleep(1)

def has_lock(l,i):
  l.acquire() #上锁 并立即返回 当前线程拥有该锁   进入函数时判断 锁的状态 如果处于lock状态 则阻塞当前线程 等待释放   通俗 一个茅坑 一个人 
  print('{i}来买票了'.format(i=i))
  time.sleep(1)
  l.release() #开锁 锁不属于任何线程 



if __name__ == '__main__':
  lock = Lock()
  for i in range(10):
    Process(target=u_lock,args=(lock,i)).start()
    Process(target=has_lock,args=(lock,i)).start()
