km = float(input('Quantos km o carro percorreu? (escreva apenas o número)'))
d = int(input('Por quantos dias? (escreva apenas o número)'))
print('Custa R$60.00 por dia e R$0,15 por km rodado.')
print(f'Tendo corrido {km}km por {d} dias, o custo total é de R${(km * 0.15) + (d * 60):.2f}')
