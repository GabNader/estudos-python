def leiaint(num):
    while True:
        try:
            num = int(input(num))
        except (ValueError, TypeError):
            print('por favor, digite um número inteiro válido.')
        except KeyboardInterrupt:
            print('o usuário preferiu não informar dados.')
            return 0
        else:
            return num


def leiafloat(num):
    while True:
        try:
            num = float(input(num))
        except (ValueError, TypeError):
            print('por favor, digite um número real válido.')
        except KeyboardInterrupt:
            print('o usuário preferiu não informar dados')
            return 0
        else:
            return num



nint = leiaint('Digite um número inteiro: ')
nfloat = leiafloat('Digite um número real: ')
print(f'Você digitou o número inteiro {nint} e o número real {nfloat}')
#
# leiafloat('Digite um número real')
# print(f'O valor inteiro digitado foi {n} e o real foi {n2}')
