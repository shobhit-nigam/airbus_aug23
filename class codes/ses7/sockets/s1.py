# server

import socket

host = "127.0.0.1"
port = 64000

objs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
objs.bind((host, port))
objs.listen()
conn, addr = objs.accept()

print(f"{addr} of connection ")

while True:
    data = conn.recv(1024)
    if not data:
        break
    conn.sendall(data)

objs.close()
