div = []
n = int(input('Digite um número: '))
if n < 0:
    print(f'{n} não é primo.')
else:
    for num in range(1, n+1):
        if n % num == 0 and num != 1 and num != n:
            div.append(num)
    if len(div) > 0:
        print(f'{n} não é primo, pois é divisível por {div}')
    else:
        print(f'{n} é um número primo')
