from time import sleep
jogador = dict()
jogadores = []
while True:
    jogador = dict()
    jogador['nome'] = str(input('Qual o nome do jogador? ')).capitalize()
    partidas = int(input('Quantas partidas jogou?'))
    jogador['gols'] = []
    for n in range(1, partidas + 1):
        gols = int(input(f'Quantos gols na {n}ª partida?'))
        jogador['gols'].append(gols)
    jogador['total'] = sum(jogador['gols'])
    jogadores.append(jogador.copy())
    segue = str(input('Quer continuar? [s/n]')).lower().strip()
    while segue not in 'sn':
        print('Erro! apenas s ou n.')
        segue = str(input('Quer continuar? [s/n]'))
    if segue == 'n':
        break

print('-='*30)
print('-='*30)
print(f'{'cód.':<4}{'nome':<10}{'gols':>20}     {'total':>5}')
print('-' * 30)
for n, jogador in enumerate(jogadores):
    print(f'{n:<4} {jogador["nome"]:<10} {jogador["gols"]:>20} {jogador["total"]}:>5')

while True:
    selecionar_jogador = int(input('Mostrar dados de qual jogador? [999 para encerrar] '))
    if selecionar_jogador == 999:
        break
    if selecionar_jogador < 0 or selecionar_jogador >= len(jogadores):
        print('Erro! Não existe jogador com esse código.')
    else:
        jogador = jogadores[selecionar_jogador]
        print(f'Levantamento do jogador {jogador["nome"]}:')
        for i, gols in enumerate(jogador['gols']):
            print(f'  No jogo {i+1}, fez {gols} gols')
    print('-=' * 30)

print('Encerrando...')
