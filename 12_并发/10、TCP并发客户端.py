import socket
import sys

HOST = '127.0.0.1'
PORT = 8080

#Create a socket object
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)


try:
  s.connect((HOST,PORT))
except Exception as e:
  print('服务器无法连接')
  #退出程序
  sys.exit()

while True:
  msg = input('please input your message:')
  if(not msg):
    continue
  #发送数据
  s.send(msg.encode())

  #接收数据
  data = s.recv(1024).decode()
  print(data)
