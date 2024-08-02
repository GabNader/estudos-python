from random import randint
v = 0
while True:
    numpc = randint(0, 10)
    uchoice = str(input('Par ou ímpar?'))
    numuser = int(input('Qual seu número??'))
    print(f'O meu número era {numpc}.')
    if uchoice == 'ímpar':
        if (numpc + numuser) % 2:
            print(f'{numpc} + {numuser} dá {numpc + numuser}, que é ímpar, então você ganhou.')
            v += 1
        else:
            print(f'{numpc} + {numuser} dá {numpc + numuser}, que é par, então eu ganhei!')
            break
    # Caso o usuário escolha par:
    else:
        if (numpc + numuser) % 2:
            print(f'{numpc} + {numuser} dá {numpc + numuser}, que é ímpar, então eu ganhei!')
            break
        else:
            print(f'{numpc} + {numuser} dá {numpc + numuser}, que é par, então você venceu.')
            v += 1
print(f'Jogo encerrado. você venceu um total de {v} vezes. ')