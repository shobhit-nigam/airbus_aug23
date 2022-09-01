import colour
import time
import importlib

print("red =", colour.red)

print("*"*10)

time.sleep(30)

importlib.reload(colour)
print("red =", colour.red)
