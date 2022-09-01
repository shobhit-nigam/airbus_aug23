listA = [11, 33, 55, 22, 10, 32]
listB = [31, 7, 32, 44, 19, 20, 5, 28, 61, 20]

# x = 2a + 3b - 10
def cal(a, b):
    return 2*a + 3*b - 10

listC = []

if len(listA) < len(listB):
    for i in range(len(listA)):
        listC.append(cal(listA[i], listB[i]))
else:
    for i in range(len(listB)):
        listC.append(cal(listA[i], listB[i]))

print(listC)

listD = list(map(cal, listA, listB))

print(listD)
