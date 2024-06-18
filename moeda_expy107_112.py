def moeda(n):
    return f'R${n:.2f}'.replace('.', ',')


def metade (n):
    res = n / 2
    return res


def dobro(n):
    res = n * 2
    return res


def aumento(n, d):
    res = n + ((n*d)/100)
    return res


def desconto(n, d):
    res = n - ((n*d)/100)
    return res


def resumo(n, aumen, descon):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'{"Preço analisado:".ljust(20)}{moeda(n).rjust(10)}')
    print(f'{"Dobro do preço:".ljust(20)}{moeda(dobro(n)).rjust(10)}')
    print(f'{"Metade do preço:".ljust(20)}{moeda(metade(n)).rjust(10)}')
    print(f'{f"{aumen}% de aumento:".ljust(20)}{moeda(aumento(n, aumen)).rjust(10)}')
    print(f'{f"{descon}% de desconto:".ljust(20)}{moeda(desconto(n, descon)).rjust(10)}')
    print('-' * 30)
