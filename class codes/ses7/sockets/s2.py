# server

import socket
import threading
from _thread import *
import time
lock = threading.Lock()

def funcx(conn):
    while True:
        data = conn.recv(1024)
        if not data:
            print("will exit")

            lock.release()
            break

        data = data.upper()
        print("Server going to sleep")
        time.sleep(10)
        conn.send(data)

    conn.close()

def mainTask():
    host = "127.0.0.1"
    port = 64000
    objs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    objs.bind((host, port))
    objs.listen(4)


    while True:
        conn, addr = objs.accept()

        lock.acquire()
        print('connected to :', addr[0], "\t", addr[1])

        start_new_thread(funcx, (conn, ))

    objs.close()


mainTask()
