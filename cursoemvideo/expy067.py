while True:
    n = int(input('Digite um número (número negativo para encerrar): '))
    if n < 0:
        break
    for x in range (1, 11):
        print(f'{n} x {x} = {n*x}')
print('PROGRAMA TABUADA ENCERRADO.  VOLTE SEMPRE')
