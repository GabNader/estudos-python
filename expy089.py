dados = [[], [], []]
while True:
    nome = str(input('Nome do(a) aluno(a): ')).capitalize()
    dados[0].append(nome)
    n1 = float(input('Qual a primeira nota?'))
    n2 = float(input('Qual a segunda nota?'))
    dados[1].append(n1)
    dados[2].append(n2)
    segue = str(input('Quer continuar? [s/n]: ')).strip().lower()
    while segue != 's' and segue != 'n':
        print('Opção inválida.')
        segue = str(input('Quer continuar? [s/n]'))
    if segue == 'n':
        break
print('-='*30)
print(f'{'No.':<4}{'NOME':<10}{'MÉDIA':>8}')
print('------------------------------')
for n in range(len(dados[0])):
    print(f'{n:<4}{dados[0][n]:<10}{(dados[1][n] + dados[2][n]) / 2:>7.1f} ')
print('------------------------------')
while True:
    nota = int(input('Gostaria de ver as notas de qual aluno? (digite o número do aluno) (999 para finalizar): '))
    if nota == 999:
        print('Programa finalizado')
        break
    else:
        print(f'Notas de {dados[0][nota]}: n1 = {dados[1][nota]}, n2 = {dados[2][nota]} ')




