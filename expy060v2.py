n = int(input('Digite um número: '))
n2 = 1
loop = n
while loop > 0:
    print(f'{loop}', end='')
    print(f' x ' if loop > 1 else ' = ', end='')
    n2 *= loop
    loop -= 1
print(f' {n}! = {n2}')
