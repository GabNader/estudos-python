h = 0
maiores = 0
msub20 = 0
while True:
    idade = int(input('Qual sua idade? '))
    if idade > 18:
       maiores += 1
    gen = str(input('Qual o gênero? (responda apenas M ou F): ')).strip().upper()
    if gen == 'M':
        h += 1
    if gen == 'F' and idade < 20:
        msub20 += 1
    cont = str(input('Gostaria de continuar? (responda apenas S ou N): ')).strip().upper()
    if cont == 'N':
        break
print(f'\nDas pessoas cadastradas, {maiores} eram maiores de 18 anos;')
print(f'{h} eram homens;')
print(f'{msub20} das mulheres possuem menos de 20 anos.')