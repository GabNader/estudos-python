n = 1
par = []
ímpar = []
while n != 0:
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        par.append(n)
    else:
        ímpar.append(n)
print(f'Você digitou {len(par)} números pares e {len(ímpar)} números ímpares')

