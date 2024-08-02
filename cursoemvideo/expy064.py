n = 0
soma = 0
quant = 0
while n != 999:
    n = int(input('Digite um número: '))
    soma += n
    quant += 1
print(f'foram mostrados {quant - 1} números')
print(f'A soma deles é {soma - 999}')