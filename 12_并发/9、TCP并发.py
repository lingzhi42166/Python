""" 
  没有经过处理的TCP通信，一次只能处理一个请求
  当多个请求进来的时候 都放在了半连接池中
  这是因为一个进程默认只有一个线程(工人)在工作
  So when a request comes in We can create a new thread to server it
"""

from threading import Thread
import socket
import struct
import json

HOST = '127.0.0.1'
PORT = 8080

# creat a socket object
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# Bind the server ip address and port
s.bind((HOST,PORT))

# Number of connections allow  
s.listen(6)



# extract a connetion request from the connertions pool   accept() once create a channel
# c is the tunnel from this connetion creates     Through c.recv(bit) receive the data
# addr is client ip addres and port 

# c,addr = s.accept()
#s.close()



if __name__ == '__main__':
  def method(c):
    while True: #We're constantly getting data from here
      try:
        data = c.recv(1024).decode()
        if(not data):
          c.close() # close the connetion to free up resources
          break # if don't have data must be break it and then server the next one
        c.send(data.encode())
      except ConnectionResetError as e: # 捕捉接收端强迫关闭连接 导致的报错 避免服务器直接报错
        print(e)
        break


  while True:
    c,addr = s.accept() # if not connertion  it will remain suspended  会一直挂起直到从半连接池获得连接请求
    t = Thread(target=method,args=(c,))# 当我获得该通道后 创建一个线程负责该请求的通信
    t.start()
    print(t.is_alive())






