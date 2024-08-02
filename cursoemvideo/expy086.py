matriz = [[], [], []]
for linha in range(0, 3):
    for coluna in range(0, 3):
        num = int(input(f'digite um número para a posição {linha}, {coluna}: '))
        matriz[linha].append(num)
print('-='*30)
print(matriz[0])
print(matriz[1])
print(matriz[2])
print('-='*30)



