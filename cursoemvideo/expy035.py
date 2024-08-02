a = float(input('Qual a medida do primeiro lado?'))
b = float(input('Qual a medida do segundo lado?'))
c = float(input('Qual a medida do terceiro lado?'))
t = [a, b, c]
t.sort()
if t[2] < (t[1] + t[0]):
    print('É possível formar um triângulo')
else:    print('Não é possível formar um triângulo')

