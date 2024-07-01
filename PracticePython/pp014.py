def tirar_repetidos(lista):
    new = []
    for n in lista:
        if n not in new:
            new.append(n)
    print(new)


lista1 = [1, 3, 5, 23, 3, 14, 21, 5, 1]
tirar_repetidos(lista1)
