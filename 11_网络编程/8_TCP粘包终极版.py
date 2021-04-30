""" 
  如果我们的头 不只是一串数字的话 而是一个字典 包含此次传输数据的多个信息
  那么就无法直接通过struct.pack转换

  那么怎么将字典 转换成固定的字节长度 告诉接收端 头数据的大小呢?  (大小 实际上就是多少个占用字节 可以通过len求出)
    首先分析struct.pack 是将一串数字转换成固定4个字节的二进制数
    那么我们怎么把字典转换成数字
      已知字符串类型是可以通过len求出字符串长度的
      并且json.dumps() 可以序列化字典 转成字符串格式
      所以我们可以先通过json.dumps 序列化字典
      然后通过len求出字典的长度(大小)
      再把这个值通过struct.pack 转成4个字节的二进制
      发送给接收端
      
    接收端首先接收前4个字节的数据
    然后通过json.loads() 将序列化的字典  反序列化 拿到字典 


  首先序列化json
  然后求出json的长度(大小)
  发送json大小给客户端
  客户端根据大小获取json数据 
  客户端反序列化json
  通过json拿到文件的大小
"""
import socket
import struct
import json

HOST = '127.0.0.1'
PORT = 8080

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((HOST,PORT))

s.listen(5)

while True:
  c,addr = s.accept()

  while True:
    try:
      data = c.recv(1024).decode()
      if(not data):
        c.close() 
        break
    except ConnectionResetError as e: # 捕捉接收端强迫关闭连接 导致的报错 避免服务器直接报错
      print(e)
      break

    file_url = r'C:\Users\Administrator\Desktop\python\11_网络编程\{name}'.format(name = data)
    try:
      with open(file_url,'r',encoding='utf-8') as f:
        header_fileIntro = {
          'size' : len(f.read()),
          'name' : f.name
        }
        strJson = json.dumps(header_fileIntro)
        header = struct.pack('i',len(strJson))
        c.send(header)
        c.send(strJson.encode()) #  encoding 把字符串编码 转换成byte
        f.seek(0)
        for line in f:
          c.send(line.encode())
    except EnvironmentError: 
      c.send('没有该文件')
  


s.close()
# data = 'readme'
# file_url = r'C:\Users\Administrator\Desktop\python\11_网络编程\{name}'.format(name = data)
# print(file_url)
# try:
#   with open(file_url,'r',encoding='utf-8') as f:
  
#     for line in f:
#       print(line.encode())
# except EnvironmentError: 
#   print('not')
