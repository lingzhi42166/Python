""" 
  UDP:
    无连接、不可靠、基于数据报的传输层通信协议
      无连接:
        不需要事先建立连接，直接向对方发送数据
      不可靠:
        不提供应答和重传机制,无法保证数据能到达目的，也无法保证是按发出顺序到达地址

""" 

import socket
# 创建一个Socket对象  socket.AF_INET表示IPV4   socket.SOCK_DGRAM表示使用UDP
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# 绑定服务器主机地址'127.0.0.1' 端口5000  指定服务器和端口 并监听
s.bind(('127.0.0.1',5000))
 
while True:
  # socket.recvfrom(bufsize[, flags]) bufsize 参数代表套接字可接收数据的最大字节数  bufsize 参数的值最好设置为 2 的幂次方 计算机是二进制处理数据的
  # print(s.recvfrom(1024))
  data,addrs = s.recvfrom(1024) # 解构赋值
  print(data,'======',addrs)
  print(type(data))#<class 'bytes'>
  data = data.decode() # 把bytes类型转成str
  print(data) # hello
  # data 发送端 发送的数据
  # addrs 是发送方的 IP 地址与端口号，用二元组 (host(主机), port) 表示

  # 字符串前加 b 表示后面字符串是bytes 类型  
  # 网络编程中，服务器和客户端只认bytes 类型数据。如：send 函数的参数和 recv 函数的返回值都是 bytes 类型
