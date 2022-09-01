ga = 100
print("outside ga =", ga)

def funcX():
    global ga
    ga = 133
    print("in funcX ga =", ga)

funcX()

print("outside ga =", ga)
