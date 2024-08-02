galera = []
soma = 0
mulheres = []
while True:
    pessoa = {}
    pessoa['nome'] = str(input('Nome: ')).capitalize()
    while True:
        pessoa['sexo'] = str(input('Sexo [m/f]:')).lower()
        if pessoa['sexo'] in 'm' or pessoa['sexo'] in 'f':
            break
        print('Apenas m ou f.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    if pessoa['sexo'] == 'f':
        mulheres.append(pessoa.copy())
    galera.append(pessoa.copy())
    segue = str(input('Gostaria de continuar? [s/n]')).lower()
    while segue != 's' and segue != 'n':
        print('Opção inválida.')
        segue = str(input('Gostaria de continuar? [s/n]'))
    if segue == 'n':
        break
print(f'Foram cadastradas {len(galera)} pessoas')
print(f'A média de idade é de {soma / len(galera):.2f}')
print(f'As mulheres do grupo são {mulheres}')
print(f'As pessoas com idade acima da média são')







