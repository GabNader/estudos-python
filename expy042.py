a = float(input('Qual a medida do primeiro lado?'))
b = float(input('Qual a medida do segundo lado?'))
c = float(input('Qual a medida do terceiro lado?'))
t = [a, b, c]
t.sort()
if t[2] < (t[1] + t[0]):
    print('É possível formar um triângulo')
    if t[2] == t[1] == t[0]:
        print('Inclusive, é um triângulo equilátero!')
    elif t[1] == t[0]:
        print('Inclusive, é um triângulo isósceles!')
    else:
        print('Inclusive, é um triângulo escaleno!')
else:
    print('Não é possível formar um triângulo')