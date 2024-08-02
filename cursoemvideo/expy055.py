lista = []
for x in range(1, 6):
    peso = float(input(f'Qual o peso da {x}ª pessoa?'))
    lista.append(peso)
lista.sort()
print(f'O maior peso é {lista[4]}kg e o menor peso é {lista[0]}kg')

