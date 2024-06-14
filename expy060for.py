n = int(input('Digite um número: '))
loop = 0
for n in range(n, 0, -1):
    print(f'{n}',end='')
    print(' x ' if loop > 1 else ' = ')
    loop *= n
print(loop)