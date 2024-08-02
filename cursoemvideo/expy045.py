from random import random, choice
pcchoices = ['pedra', 'papel', 'tesoura']
pcchoice = choice(pcchoices)
userchoice = str(input('pedra, papel ou tesoura?')).strip().lower()
if userchoice == pcchoice:
    print(f' Nós dois escolhemos {userchoice}, então empatou.')
else:
    if userchoice == 'pedra' and pcchoice == 'tesoura':
        print('pedra bate tesoura, você venceu')
    if userchoice == 'pedra' and pcchoice == 'papel':
        print('papel bate pedra, eu venci')
    if userchoice == 'tesoura' and pcchoice == 'papel':
        print('tesoura corta papel, você venceu')
    if userchoice == 'tesoura' and pcchoice == 'pedra':
        print('pedra bate tesoura, eu venci')
    if userchoice == 'papel' and pcchoice == 'pedra':
        print('papel bate pedra, você venceu')
    if userchoice == 'papel' and pcchoice == 'tesoura':
        print('tesoura corta papel, eu venci')

