""" 
  TCP面向连接、可靠的、基于字节流的传输层通信协议
  TCP 协议的运行分为连接创建（Connection Establishment）、数据传送（Data Transfer）和连接终止（Connection Termination）三个阶段，
  其中「连接创建」阶段是耳熟能详的 TCP 协议三次握手（TCP Three-way Handshake）

  建立双向通信管道  双方可以同时给对方发送数据

  为什么服务端 需要另一个套接字对象进行通信？
    因为服务端不只是服务一个客户端
    通过accept 返回的套接字对象 是标识了 该连接是哪一个客户端
"""
import socket

HOST = '127.0.0.1'
PORT = 50006

# # 创建socket对象
# s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# # 绑定服务器的IP地址和通信端口
# s.bind((HOST,PORT))
# # 监听客户端连接 把连接请求按照IFIO放入链接池池   socket.listen([backlog]) backlog允许挂起的最大连接数(半连接池大小) 如没有设置则会自动设置一个合理值
# s.listen()
# print('server start at port %s' %PORT)

# # 从链接池拿一个半连接 创建连接  accept() 一次拿一个
# conn,addr = s.accept()
# print(conn)#<socket.socket fd=468, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 50006), raddr=('127.0.0.1', 5094)>
# print(addr)#('127.0.0.1', 5094)  客户端的IP地址和端口号

# #接收数据
# data = conn.recv(1024)
# print(data.decode())

# conn.send('i got it'.encode())

# conn.close()
# s.close()


# 创建套接字对象
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#绑定服务器的ip+port
s.bind((HOST,PORT))

#监听链接 放入半链接池  并设置半链接池空间为5个链接
s.listen(5)

while True:
  #从链接池拿链接 创建与客户端通信的管道
  c,addr = s.accept()
  while True:
    #获取数据
    data = c.recv(1024).decode()
    #如果没有数据传输了 那么跳出本次连接循环 服务下一个客户端
    if not data: 
      break
    print(data)
    c.send(data.encode())
  #关闭连接 释放资源
  c.close()

#相当于关机 回收socket对象 可有可无
s.close()


