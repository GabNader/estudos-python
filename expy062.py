p1 = int(input('Qual o primeira termo da PA?'))
r = int(input('Qual a razão da PA?'))
p10 = p1
loops = 0
termos = 10

while True:
    while loops < termos:
        print(f'{p10} -> ', end='')
        p10 += r
        loops += 1

    resposta = input('Gostaria de ver mais termos? s/n ')
    if resposta.lower().strip() == 'n':
        break
    extras = int(input('Quantos termos a mais gostaria de ver? '))
    termos += extras
print(f'Ao total foram mostrados {termos} termos.')


