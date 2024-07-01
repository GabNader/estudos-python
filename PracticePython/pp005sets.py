def sem_repetidos(lista1, lista2):
    lista3 = lista1 + lista2
    lista_sem_repetidos = set(lista3)
    print(lista_sem_repetidos)


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
sem_repetidos(a, b)
