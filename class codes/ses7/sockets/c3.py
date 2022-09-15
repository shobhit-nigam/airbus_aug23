# client
import os
import socket

host = "10.0.0.22"   # get the ip address & mention here
port = 64000

objs = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    data = input("type your message:\n")


    objs.sendto(data.encode(), (host, port))
    if data == "quit":
        break

objs.close()
os._exit(0)
