f = str(input('Digite uma frase: ')).strip().lower().split()
limpa = ''.join(f)
if limpa == limpa[::-1]:
    print('É palíndromo')
else:
    print('Não é palíndromo')
