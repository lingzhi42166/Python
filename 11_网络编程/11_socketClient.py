import socket
import sys
import time
 
HOST, PORT = '127.0.0.1', 8080
data = " ".join(sys.argv[1:])
 
# Create a socket (SOCK_STREAM means a TCP socket)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 

# Connect to server and send data
sock.connect((HOST, PORT))
sock.sendall(bytes(data + "\n", "utf-8"))

# Receive data from the server and shut down
received = str(sock.recv(1024), "utf-8")
print(received)
time.sleep(10)
