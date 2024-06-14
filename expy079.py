listanum = []
while True:
    n = int(input('Digite um número: '))
    if n not in listanum:
        listanum.append(n)
        print('Valor adicionado à lista.')
    else:
        print('Valor duplicado! não vou adicionar.')
    seguir = str(input('Quer continuar? [s/n]')).strip().lower()
    while seguir != 's' and seguir != 'n':
        seguir = str(input('Quer continuar? [s/n]')).strip().lower()
    if seguir == 'n':
        break
listanum.sort()
print(listanum)
