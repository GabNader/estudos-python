from datetime import date
today = date.today()
year = today.year
pessoa = {}
pessoa['nome'] = str(input('Nome: '))
nascimento = int(input('Ano de nascimento: '))
pessoa['idade'] = year - nascimento
pessoa['CTPS'] = int(input('CTPS (0 caso não tenha): '))
if pessoa['CTPS'] != 0:
    pessoa['contratação'] = int(input('Ano de contratação: '))
    pessoa['salário'] = float(input('Salário: R$'))

print(f'Nome: {pessoa['nome']}')
print(f'Idade: {pessoa['idade']}')
if pessoa['CTPS'] == 0:
    print('Vagabundo.')
else:
    print(f'CTPS n. {pessoa['CTPS']}')
    print(f'Ano de contratação: {pessoa['contratação']} ')
    print(f'Salário: R${pessoa['salário']}')
    print(f'Aposentadoria com {pessoa['idade'] + pessoa['contratação'] + 35 - year} anos.')
