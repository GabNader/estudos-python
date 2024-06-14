import math

print('sou um programa que lê seu número e te mostro o dobro, o triplo e a raíz quadrada dele ')
n = int(input('digite aqui o número:'))
#s=n+n
s = n * 2
l = n * 3
#t = (math.sqrt(n))
#l = n + n + n
t = n ** (1 / 2)
#print('o dobro é {}, o triplo é {}, e a raíz quadrada é {}'.format(s, l, t))
print(f'o dobro de {n} é {n*2}. \no triplo é {n*3}. \ne a raíz quadrada é {n**(1/2)}.')

