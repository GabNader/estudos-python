maior = []
menor = []
for n in range (1, 8):
    age = int(input(f'em que ano a {n}ª pessoa nasceu?'))
    if age < 2006:
        maior.append(age)
    elif age > 2006:
        menor.append(age)
print(f'Existem {len(maior)} pessoas maiores de idade e {len(menor)} pessoas menores de idade')


