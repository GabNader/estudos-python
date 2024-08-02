vn = float(input('Qual o valor do produto? R$'))
print('FORMAS DE PAGAMENTO')
print('[ 1 ] à vista dinheiro/pix (10% de desconto)')
print('[ 2 ] à vista cartão (5% de desconto)')
print('[ 3 ] 2x no cartão')
print('[ 4 ] 3x ou mais no cartão (juros de 20%)\n')
fp = int(input('Qual a forma de pagamento? (digite o número):'))
if fp == 1:
    print(f'O preço à vista no dinheiro pix fica R${vn * 0.9:.2f}')
elif fp == 2:
    print(f'O preço à vista no cartão fica R${vn * 0.95:.2f}')
elif fp == 3:
    print(f'O preço de cada parcela é de R${vn / 2:.2f}')
elif fp == 4:
    print(f'O preço em 3 ou mais parcelas fica R${vn * 1.2:.2f}')
    qp = int(input('Quer parcelar em quantas vezes?'))
    print(f'O preço de cada parcela será R${(vn * 1.2) / qp:.2f}')
else:
    print('Opção inválida. Tente novamente.')
