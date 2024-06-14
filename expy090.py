pessoa = dict()
pessoa['nome'] = str(input('Nome: ')).capitalize()
pessoa['média'] = float(input(f'Média de {pessoa["nome"]}: '))
if pessoa['média'] >= 7:
    pessoa['situação'] = 'Aprovado'
elif 7 > pessoa['média'] >= 5:
    pessoa['situação'] = 'Em recuperação'
else:
    pessoa['situação'] = 'Reprovado'
print(f'Nome: {pessoa["nome"]}')
print(f'Média: {pessoa["média"]}')
print(f'Situação: {pessoa["situação"]}')
