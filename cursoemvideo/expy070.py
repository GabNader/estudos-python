ptotal = 0
mais_de_mil = 0
nome_mais_barato = ''
menor = float('inf')
while True:
    nome = str(input('Qual o nome do produto: ')).strip()
    price = float(input('Qual o preço do produto: '))
    if price > 1000:
        mais_de_mil += 1
    if price < menor:
        menor = price
        nome_mais_barato = nome

    ptotal += price
    cont = str(input('Deseja continuar? [S/N]')).strip().upper()
    if cont == 'N':
        break
print(f'O total a pagar é de R${ptotal:.2f}')
print(f'{mais_de_mil} produtos custaram mais de R$1000.00')
print(f'O produto mais barato foi {nome_mais_barato} custando {menor:.2f}')
