def ficha(nome, gols):
    if nome == '':
        nome = '<desconhecido>'
    if gols == '':
        gols = '0'
    print(f'O jogador {nome} marcou {gols} gols.')


print('-'*20)
jogador = str(input('Nome do jogador: '))
golos = input('Quantos gols: ')
ficha(jogador, golos)