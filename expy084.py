pessoas = []
dados = []
pena = []
pesado = []

while True:
    dados.append(str(input('Qual o nome?')).capitalize())
    dados.append(int(input('Qual o peso?')))
    pessoas.append(dados[:])
    dados.clear()
    segue = str(input('Gostaria de continuar? [s/n]').strip().lower())
    if segue != 's' and segue != 'n':
        print('Opção inválida.')
        segue = str(input('Gostaria de continuar? [s/n'))
    if segue == 'n':
        break
print(f'foram cadastradas {len(pessoas)} pessoas')
for p in pessoas:
    if p[1] >= 100:
        pesado.append(p[0])
    if p[1] <= 70:
        pena.append(p[0])
print(f'Os pesos-pesados são {pesado}')
print(f'Os peso-pena são {pena}')



