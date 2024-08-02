total = []
pares = []
for n in range(1, 7):
    n = int(input(f'Digite o {n}º número:'))
    total.append(n)
    if n % 2 == 0:
        pares.append(n)
print(f'Dos {len(total)} números, {len(pares)} são pares. A soma deles dá {sum(pares)} ')



