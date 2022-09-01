listA = [11, 33, 55, 22, 10, 32]
listB = [31, 7, 32, 44, 19, 20, 5, 28, 61, 80]

def filter_a(a):
    return a%5 == 0 and a%4 == 0

print(list(filter(filter_a, listB)))
