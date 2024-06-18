def leiadinheiro(n):
    print(n)
    x = str(input())
    if x.isnumeric():
        valor = float(x)
        return f'{valor:.2f}'
    else:
        print('ERRO! Digite um número válido.')

leiadinheiro('Digite um número: ')


def leiaint(num):
    while True:
        num = str(input(num))
        if num.isnumeric():
            valor = int(num)
            return valor
        else:
            print('ERRO! Digite um número inteiro válido.')