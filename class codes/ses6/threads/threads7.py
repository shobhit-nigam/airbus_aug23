from threading import Thread, Lock

objl = Lock()
ga = 120

def taskA():
    global ga
    print(f"task A requesting lock with name = {Thread.getName(ta)}")
    objl.acquire()
    print("task A acquired lock")
    for i in range(50000000):
        ga = ga+10
    print("task A released lock")
    objl.release()

def taskB():
    print(f"task B requesting lock with name = {Thread.getName(tb)}")
    objl.acquire()
    print("task B acquired lock")
    global ga
    for i in range(50000000):
        ga = ga-10
    print("task A released lock")
    objl.release()

ta = Thread(target=taskA, name="aaaa")
tb = Thread(target=taskB)

ta.start()
tb.start()

ta.join()
tb.join()

print(f"val of ga = {ga}")
