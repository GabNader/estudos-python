# Pergunta o valor do salário atual
s = float(input('Digite seu salário:'))
print('Você ganhou aumento')
# Se o salário é menor ou igual a 1200, o aumento é de 15%
if s <= 1200:
    print(f'Seu novo salário é {s * 1.15:.2f}')
# Caso contrário, o aumento é de 10%
else:
    print(f'Seu novo salário é {s * 1.10:.2f}')



