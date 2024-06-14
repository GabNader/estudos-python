from random import randint
print('Tente adivinhar o número de 0 a 5 que estou pensando...')
n = randint(0, 5)
p = int(input('Digite aqui seu palpite:'))
if n == p:
    print(f'Você acertou! eu estava pensando no número {n} ')
else:
    print(f'Errou! eu estava pensando no número {n}')
