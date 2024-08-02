nome = []
somaidade = 0
gender = []
for n in range(1, 5):
    #nome = str(input(f'Qual o nome da {n}ª pessoa?')).strip
    idade = int(input(f'Qual a idade da {n}ª pessoa?'))
    somaidade = somaidade + idade
    #gender = str(input(f'Qual o gênero da {n}ª pessoa? (escreva M/F')).strip.lower

print(f'A média de idade é {somaidade/4:.1f}')
