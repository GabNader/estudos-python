from time import sleep
from random import randint
print('-'*30)
print('JOGA NA MEGA SENA')
print('-'*30)
quantos = int(input('Quantos jogos quer fazer?'))
for jogo_atual in range(quantos):
    jogo = []
    while len(jogo) < 6:
        num = randint(1, 60)
        if num not in jogo:
            jogo.append(num)
    jogo.sort()
    sleep(1)
    print('-='*16)
    print(f'Jogo {jogo_atual+1}: {jogo}')
