n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro: '))
n3 = int(input('Mais um: '))
n4 = int(input('o último: '))
tnumeros = (n1, n2, n3, n4)
print(f'O número 9 apareceu {tnumeros.count(9)} vezes')
if 3 in tnumeros:
    print(f'O primeiro número 3 aparece na posição {tnumeros.index(3)}')
else:
    print('O número 3 não aparece.')
print('Os valores pares digitados foram')
for n in tnumeros:
    if n % 2 == 0:
        print(n, end=' ')
