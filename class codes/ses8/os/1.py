import os
import time
print(os.getpid())
print("nice value ->", os.nice(0))
time.sleep(10)
print("nice value increased to->", os.nice(15))
time.sleep(15)
