frase = str(input('Digite uma frase e te trago as estatísticas sobre a letra "a":')).strip().upper()
frase = frase.replace('Á', 'A')
frase = frase.replace('À', 'A')
frase = frase.replace('Ã', 'A')
print(f'A letra A aparece {frase.count('A')} vezes na frase')
print(f'A primeira letra A aparece na posição {frase.find('A') + 1}')
print(f'A última letra A aparece na posição {frase.rfind('A') + 1}')
