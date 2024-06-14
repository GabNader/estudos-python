from random import randint
from time import sleep
from operator import itemgetter
resultados = dict()
print('Valores Sorteados:')
for n in range(1,5):
    dado = randint(1, 6)
    print(f'o jogador{n} tirou {dado}')
    resultados[f'jogador{n}'] = dado
    sleep(0.7)
ranking = []
print('Ranking dos jogadores:')
ranking = sorted((resultados.items()), key=itemgetter(1), reverse=True)
print('-='*30)
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}')
    sleep(0.7)




