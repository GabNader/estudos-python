from random import choice
def jokenpo(user, pc):
    if user == pc:
        print(f'Nós dois jogamos {user}, então empatou')
    else:
        if (user == 'pedra' and pc == 'tesoura') or \
        (user == 'tesoura' and pc == 'papel') or \
        (user == 'papel' and pc == 'pedra'):
            print(f'{user} bate {pc}, você venceu.')
        else:
            print(f'{pc} bate {user}, eu venci.')


while True:
    pcchoices = ['pedra', 'papel', 'tesoura']
    pcchoice = choice(pcchoices)
    player_choice = str(input('pedra, papel ou tesoura?')).lower()

    while player_choice not in pcchoices:
        print('apenas pedra, papel, ou tesoura')
        player_choice = str(input('pedra, papel ou tesoura?')).lower()

    jokenpo(player_choice, pcchoice)

    segue = str(input('Gostaria de jogar de novo? [S/N]')).upper()
    while segue != 'S' and segue != 'N':
        print('apenas "S" ou "N", por favor. ')
        segue = str(input('Gostaria de jogar de novo? [S/N')).upper()
    if segue == 'N':
        print('Obrigado, volte sempre.')
        break








