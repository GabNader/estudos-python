lista = []
cincun = 0
while True:
    n = int(input('Digite um número:'))
    lista.append(n)
    if n == 5:
        cincun += 1
    pergunta = str(input('Gostaria de continuar? [s/n] ')).strip().lower()
    while pergunta != 's' and pergunta != 'n':
        pergunta = str(input('Gostaria de continuar? [s/n] ')).strip().lower()
    if pergunta == 'n':
        break
print(f'foram digitados {len(lista)} números.')
print(f'os números em ordem decrescente: {sorted(lista, reverse=True)}')
if cincun == 1:
    print('o número 5 foi digitado uma vez')
if cincun > 1:
    print(f'o número 5 foi digitado {cincun} vezes')
if cincun == 0:
    print('o número 5 não foi digitado nenhuma vez')
