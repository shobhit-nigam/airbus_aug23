# server

import socket
import time

def mainTask():
    host = "127.0.0.1"
    port = 64000
    objs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    objs.connect((host, port))

    info = "let the force be with you"

    while True:
        objs.send(info.encode('utf-8'))

#        objs.settimeout(5)
        data = objs.recv(1024)


        print("received from the server --> ", data)

        x = input("continue ? (y/n) : ")
        if x.lower() in ["yes", "y"]:
            continue
        else:
            break

    objs.close()


mainTask()
