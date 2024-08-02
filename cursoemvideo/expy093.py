from time import sleep
jogador = dict()
jogador['nome'] = str(input('Qual o nome do jogador? ')).capitalize()
partidas = int(input('Quantas partidas jogou?'))
jogador['gols'] = []
for n in range(1, partidas + 1):
    gols = int(input(f'Quantos gols na {n}ª partida?'))
    jogador['gols'].append(gols)
jogador['total'] = sum(jogador['gols'])
print('-='*30)
print(jogador)
print('-='*30)
print(f'O campo nome tem o valor {jogador['nome']}')
print(f'O campo gols tem o valor {jogador['gols']}')
print(f'O campo total tem o valor {jogador['total']}')
print('-='*30)
print(f'O jogador {jogador['nome']} jogou {partidas} partidas.')
for n in range(1, partidas + 1):
    if jogador['gols'][n-1] == 1:
        print(f'=> Na partida {n}, fez {jogador['gols'][n-1]} gol')
        sleep(1)
    else:
        print(f'=> Na partida {n}, fez {jogador['gols'][n-1]} gols')
        sleep(1)
print(f'Foi um total de {jogador['total']} gols.')