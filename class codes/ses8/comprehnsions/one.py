# comprehensions

lista = list(range(1000000))

def with_for():
    temp = []
    for i in lista:
        if i%3:
            temp.append(i)
    return temp

def with_comprehension():
    return [i for i in lista if i%3]

def with_lambda():
    return list(filter(lambda i : i%3, lista))

# python -m timeit -s "from one import with_comprehension" "with_comprehension()"
