from moeda_expy107_112 import moeda, metade, dobro, aumento, desconto

p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda(p)} é {moeda(metade(p))}')
print(f'O dobro de {moeda(p)} é {moeda(dobro(p))}')
print(f'Aumentando 10%, temos {moeda(aumento(p, 10))}')
print(f'Com 13% de desconto, temos {moeda(desconto(p, 13))} ')
