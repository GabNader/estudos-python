import math

co = float(input('Qual o comprimento do cateto oposto?'))
ca = float(input('Qual o comprimento do cateto adjacente?'))
#hip = ((cato**2) + (cata**2)) ** 1/2
math.hypot(ca, co)

print(f'Se o cateto oposto mede {co} e o cateto adjacente {ca}, a hipotenusa mede {math.hypot(ca, co):.2f}')


