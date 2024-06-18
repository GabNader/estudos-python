from moeda_expy107_112 import metade, dobro, aumento, desconto

p = float(input('Digite o preço: R$'))
print(f'A metade de {p} é {metade(p)}')
print(f'O dobro de {p} é {dobro(p)}')
print(f'Aumentando 10%, temos {aumento(p, 10)}')
print(f'Com 13% de desconto, temos {desconto(p, 13)} ')
