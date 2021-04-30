""" 
  前面的学习中，我们可以发送，服务端一次只能服务一个客户端 
  当有多个客户端请求连接服务端的时候 都会先放在半连接池 按顺序服务  (同步阻塞)

  再还没有学习并发编程之前 我们可以利用socketserver标准库来实现同时与多个客户端通信
  
"""

import socketserver

class MyServer(socketserver.BaseRequestHandler): 
  # 重写父类的handle()方法 请求处理函数
  def handle(self):                           
    #self.request => 封装了 s.accept() 中的conn 
    data = self.request.recv(1024) 
    print(data)                
    msg = '亲，学会了吗'
    self.request.send(bytes(msg,encoding='utf-8'))
    self.request.close()          

server = socketserver.ThreadingTCPServer(('127.0.0.1',8080),MyServer)
server.serve_forever() 