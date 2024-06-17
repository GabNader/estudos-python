def leiaint(num):
    while True:
        num = str(input(num))
        if num.isnumeric():
            valor = int(num)
            return valor
        else:
            print('ERRO! Digite um número inteiro válido.')


n = leiaint('Digite um número: ')
print(f'Você digitou o número {n}')
