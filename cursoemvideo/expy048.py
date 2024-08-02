corretos = []
errados = []
for n in range(3, 500, 3):
    if n % 2 == 0:
        errados.append(n)
    else:
        corretos.append(n)
print(f' A soma de todos os {len(corretos)} valores é {(sum(corretos))}')


