d = float(input('Qual a distância da viagem em km?'))
if d > 200:
    print(f'O valor da passagem é R${d * 0.45}')
else:
    print(f'O valor da passagem é R${d * 0.5}')
print('Boa viagem!')
