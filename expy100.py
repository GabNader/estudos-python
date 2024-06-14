from random import randint
from time import sleep
def sorteia(lista):
    print('Sorteando os 5 valores da lista:', end='')
    for x in range(1, 6):
        n = randint(1, 10)
        lista.append(n)
        print(f' {n}', end='')
        sleep(0.5)
    print(' PRONTO!')
def somaPar(lista):
    print(f'Somando os valores pares de {lista}, ', end='')
    pares = 0
    for n in lista:
        if n % 2 == 0:
            pares += n
    print(f'temos {pares}')


numeros = []
sorteia(numeros)
somaPar(numeros)
