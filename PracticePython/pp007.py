a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
pares = []
for n in a:
    if n % 2 == 0:
        pares.append(n)
print(f'Os números pares da lista são {pares}')
