import socket
import struct
import json

HOST = '127.0.0.1'
PORT = 8080

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect((HOST,PORT))

s.send('readme'.encode())

# 首先获取信息头的大小
header_size = struct.unpack('i',s.recv(4))[0]
#获取信息头
file_intro = json.loads(s.recv(header_size).decode())
#从信息头 拿到文件的大小
total_size = file_intro['size']

has_size = 0
print(has_size,total_size)

print(has_size<total_size)

while (has_size < total_size) :
  data = s.recv(1024).decode()
  has_size += len(data)
  print(data,end='')

s.close()



