from random import randint
c = 0
numeros = ()
while c < 5:
    num = randint(0,10)
    numeros +=(num,)
    c += 1
print(f'Os números sorteados foram {numeros}')
print(f'O menor valor é {min(numeros)}')
print(f'O maior valor é {max(numeros)}')