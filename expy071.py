n50 = n20 = n10 = n1 = 0
n = int(input('Qual o valor a ser sacado?'))
while n >= 50:
    n50 += 1
    n -= 50
if n50 > 0:
    print(f'Total de {n50} cédulas de R$50')
while n >= 20:
    n20 += 1
    n -= 20
if n20 > 0:
    print(f'Total de {n20} cédulas de R$20')
while n >= 10:
    n10 += 1
    n -= 10
if n10 > 0:
    print(f'Total de {n10} cédulas de R$10')
while n >= 1:
    n1 += 1
    n -= 1
if n1 > 0:
    print(f'Total de {n1} cédulas de R$1')
