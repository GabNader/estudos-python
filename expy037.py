n = int(input('Digite um número:'))
con = int(input('Digite 3 para hexadecimal, 2 para octal, 1 para binário:'))
if con == 1:
    print(f'O número {n} em binário fica {bin(n) [2:]}')
elif con == 2:
    print(f'o número {n} em octal fica {oct(n)[2:]}')
elif con == 3:
    print(f' O número {n} em hexadecimal fica {hex(n)[2:]}')
else:
    print('É só 1, 2 ou 3, po. Perdeu.')

