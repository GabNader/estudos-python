p = float(input('Qual o peso em kg?'))
a = float(input('Qual a altura em m?'))
imc = p / (a ** 2)
print(f'IMC = {imc:.2f}')
if imc < 18.5:
    print('Está abaixo do peso.')
elif imc < 25:
    print('Peso ideal.')
elif imc < 30:
    print('Sobrepeso.')
elif imc < 40:
    print('Obesidade')
else:
    print('Obesidade mórbida.')

