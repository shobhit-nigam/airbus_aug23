# client

import socket

host = "127.0.0.1"
port = 64000

objs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
objs.connect((host, port))
objs.sendall(b"wednesday")
data = objs.recv(1024)

print(f"receivd data is {data}")


objs.close()
