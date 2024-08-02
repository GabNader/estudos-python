dados = {'nome': 'Pedro', 'idade': 25
         }
dados['sexo'] = 'M'
del dados['idade']
print(dados)
filme = {'titulo': 'Star Wars', 'ano': 1977, 'diretor': 'George Lucas'
         }
print(filme.values())
print(filme.keys())
print(filme.items())

for k, v in filme.items():
    print(f'O {k} é {v}')
locadora = []
locadora.append(filme)
print(locadora[0]['ano'])
brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)