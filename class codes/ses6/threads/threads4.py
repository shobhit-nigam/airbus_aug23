from threading import Thread
import time

def taskA(arg):
    for i in range(arg, 0, -1):
        print(f"task A will end in {i} seconds")
        time.sleep(1)

def taskB(arg):
    for i in range(arg, 0, -1):
        print(f"task B will end in {i} seconds")
        time.sleep(1)

ta = Thread(target=taskA, args = (2, ))
tb = Thread(target=taskB, args = (5, ))

ta.start()
tb.start()

for i in range(6, 0, -1):
    print(f"main task will end in {i} seconds")
    time.sleep(1)

tb.join()
print("main has to wait for tb to finish")
