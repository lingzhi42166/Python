""" 
  上一篇中，我们创建线程的方式 是使用Thread类实例化一个线程对象
  这篇 我们通过继承Thread类 重写run()方法自定义线程的行为
  
    start() 启动线程 默认自动调用run()方法
    run()方法 线程代码 是用来实现线程的功能与业务逻辑的  实例化类传入的target对象 就放在run中执行的
"""

import threading

def task_test(index):
  print(index)

class myThread(threading.Thread):
  def __init__(self,target,args):
    self.target = target
    self.args = args
    print(dir(self))
    super().__init__()# 需要执行基类的__init__ 初始化  把self 扔给基类__init__初始化  可以修改target为_target 即可看出效果
    print(dir(self))
  def run(self):
    print('自定义线程的功能')
    self.target(self.args[0])


if __name__ == '__main__':
  t = myThread(target=task_test,args=(0,))
  t.start()