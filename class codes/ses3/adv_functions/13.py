def genX(val):
    while(val>0):
        yield val
        val = val - 1

for x in genX(5):
    print("x =", x)
