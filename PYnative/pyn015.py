def exponent(base, exp):
    result = base ** exp
    print(f'base = {base} \nexponent = {exp}')
    print(f'{base} raises to the power of {exp}: {result} ', end='')
    print(f'i.e. ', end='')
    for n in range(exp):
        print(f'{base}', end='')
        if n < exp - 1:
            print(' * ', end='')
        else:
            print(f' = {result}')



exponent(2, 5)