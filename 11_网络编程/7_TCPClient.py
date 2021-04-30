import socket
import struct

HOST = '127.0.0.1'
PORT = 8080

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((HOST,PORT))

while True:
  # 先获取自定义头部  得到数据的大小
  data_size = s.recv(4)
  rec_size = struct.unpack('i',data_size)[0]
  has_size = 0

  while (has_size<rec_size):
    data = s.recv(1024)
    has_size+=len(data.decode())
    print(has_size)
    print(data.decode(),end='')
  print('\n接收完毕')
  break
s.close()