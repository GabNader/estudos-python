n1 = int(input('Digite o primeiro número:'))
n2 = int(input('Digite o segundo número:'))
n3 = int(input('Digite o terceiro número:'))
ns = [n1, n2, n3]
ns.sort()
if n1 == n2 and n1 == n3:
    print('Os três números são iguais')
else:
    print(f' O maior número é {ns[2]}')
    print(f'O menor número é {ns[0]}')

