from threading import Thread

ga = 120

def taskA():
    global ga
    for i in range(10000000):
        ga = ga+10

def taskB():
    global ga
    for i in range(10000000):
        ga = ga-10

ta = Thread(target=taskA)
tb = Thread(target=taskB)

ta.start()
tb.start()

ta.join()
tb.join()

print(f"val of ga = {ga}")
