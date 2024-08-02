km = float(input('Quantos km o carro rodou?'))
d = int(input('Por quantos dias?'))
print('São R$60 por dia e R$0.15 por km rodado, portanto:')
#pkm = km * 0.15
#pd = d * 60
#price = pkm + pd

print(f' Rodando {km}km por {d} dias, o custo fica R${(km * 0.15) + (d * 60):.2f}')

