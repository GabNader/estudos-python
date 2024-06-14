from math import factorial
n = int(input('Digite um número: '))
loop = n
while loop > 0:
    print(f'{loop}', end='')
    print(' x ' if loop > 1 else ' = ', end='')
    loop -= 1
print(factorial(n))
