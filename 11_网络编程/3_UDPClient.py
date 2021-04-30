import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
addr = ('127.0.0.1', 5000)


data = 'hello'
# 像addr指定的服务器端口 发送数据
# encode() 将字符串转换为 bytes 对象后
s.sendto(data.encode(), addr)


s.close()