n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro: '))
options = 0
while options != 5:
    print('Escolha [1] para soma\nEscolha [2] para multiplicar \nEscolha [3] para ver qual é maior')
    print('Escolha [4] para digitar novos números\nEscolha [5] para sair do programa')
    options = int(input('opção escolhida (apenas o número): '))
    if options == 1:
        print(f'\n{n1} + {n2} = {n1 + n2}\n')
    elif options == 2:
        print(f'\n{n1} x {n2} = {n1 * n2}\n')
    elif options == 3:
        if n1 > n2:
            print(f'\n{n1} é maior que {n2}\n')
        elif n1 == n2:
            print(f'\n{n1} é igual a {n2}\n')
        else:
            print(f'\n{n2} é maior que {n1}\n')
    elif options == 4:
        n1 = int(input('\nDigite o novo primeiro número: '))
        n2 = int(input('\nDigite o novo segundo número: '))
    elif options == 5:
        print('Então tá joia!')
    elif options > 5:
        print('\nOpção inválida.\n')