num = []
for n in range(0,5):
    n = int(input(f'Digite um número para posição {n}: '))
    num.append(n)
print(f'os números digitados foram {num}')
print(f'O maior número foi {max(num)}, na posição {num.index(max(num))}')
print(f'O maior número foi {max(num)}, na posição {num.index(max(num))}')


#print(f'O menor número foi {min(num)}, na posição {num.index(min(num))}')
