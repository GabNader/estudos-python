print('Sou um programa que te diz se o primeiro número inteiro é divisível pelo segundo!')
n1 = int(input('Digite o primeiro número:'))
n2 = int(input('Digite o segundo número'))
if n1 % n2 == 0:
    print(f'{n1} é divisível por {n2}.')
else: print(f'{n1} não é divisível por {n2}')


