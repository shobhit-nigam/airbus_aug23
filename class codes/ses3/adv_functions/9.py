listA = [11, 33, 55, 22, 10, 32, 11, 66, 44, 9]
listB = [31, 7, 32, 44, 19, 20, 5, 28, 61, 20]

listC = list(map( lambda a, b : a if a>b else b, listA, listB))
print(listC)
