listA = [11, 33, 55, 22, 10, 32]
listB = [31, 7, 32, 44, 19, 20, 5, 28, 61, 20]

# x = 2a + 3b - 10

listD = list(map(lambda a, b : 2*a+3*b-10, listA, listB))

print(listD)
