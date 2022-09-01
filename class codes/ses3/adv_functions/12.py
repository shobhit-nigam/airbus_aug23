def genX():
    val = 11
    print("first call")
    yield val

    val = val + 2
    print("second call")
    yield val

    val = val + 3
    print("third call")
    yield val

x = genX()
print(next(x))
print(next(x))
print(next(x))

#error
print(next(x))

#StopIteration
