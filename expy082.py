lista = []
pares = []
impares = []
while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    escolha = str(input('deseja continuar?'))
    while escolha != 's' and escolha != 'n':
        print('apenas s ou n!')
        escolha = str(input('deseja continuar?'))
    if escolha == 'n':
        break
print(f'a lista de números digitados: {lista}')
for valor in lista:
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)
print(f'A lista de números que são pares: {pares}')
print(f'A lista de números que são ímpares: {impares}')
