matriz = [[], [], []]
pares = []
for linha in range(0, 3):
    for coluna in range(0, 3):
        num = int(input(f'digite um número para a posição {linha}, {coluna}: '))
        matriz[linha].append(num)
        if num % 2 == 0:
            pares.append(num)
print('-='*30)
print(matriz[0])
print(matriz[1])
print(matriz[2])
print('-='*30)
print(f'A soma de todos os valores pares digitados é {sum(pares)}')
print(f'A soma dos valores da terceira coluna é {matriz[0][2] + matriz[1][2] + matriz[2][2]}')
print(f'O maior valor da segunda linha é {max(matriz[1])}')