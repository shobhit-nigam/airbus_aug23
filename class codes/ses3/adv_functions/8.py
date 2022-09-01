listB = [31, 7, 32, 44, 19, 20, 5, 28, 61, 80]

print(list(filter(lambda a : a%5 == 0 and a%4 == 0, listB)))
