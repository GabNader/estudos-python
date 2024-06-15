def fatorial(num, show=False):
    """
    -> Calcula o fatorial de um número.
    :param num: 0 número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta (padrão é não mostrar)
    :return: O valor do Fatorial do número 'num'
    """
    f = 1
    for c in range(num, 0, -1):
        if show:
            if c != 1:
                print(f'{c} x ', end='')
            else:
                print(f'{1} = ', end='')
        f *= c
    return f


print(fatorial(4, True))
