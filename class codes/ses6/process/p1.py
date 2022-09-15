from multiprocessing import Process
import time
import os

def taskA(arg):
    for i in range(arg, 0, -1):
        print(f"task A will end in {i} seconds with pid = {os.getpid()}")
        time.sleep(1)

def taskB(arg):
    for i in range(arg, 0, -1):
        print(f"task B will end in {i} seconds with pid = {os.getpid()}")
        time.sleep(1)

pa = Process(target=taskA, args = (20, ))
pb = Process(target=taskB, args = (25, ))

pa.start()
pb.start()

for i in range(10, 0, -1):
    print(f"main task will end in {i} seconds with pid = {os.getpid()}")
    time.sleep(1)
