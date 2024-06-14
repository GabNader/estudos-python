estado = dict()
brasil = list()
for c in range(0,2):
    estado['UF'] = str(input('Qual o nome do Estado: ')).capitalize()
    estado['sigla'] = str(input('Qual a sigla do Estado: ')).upper()
    brasil.append(estado.copy())
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}')
