quant = 0
n = 0
ordem = []
while True:
    num = int(input('Digite um número'))
    n += num
    quant += 1
    ordem.append(num)
    cont = input('Quer continuar? digite n para finalizar').strip().lower()
    if cont == 'n':
        break
print(f'a média dos {quant} valores foi {n / quant}')
ordem.sort()
print(f'O maior número digitado foi {ordem[-1]} e o menor foi {ordem[0]}')



