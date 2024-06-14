def área(l, c):
    print(f'para um terreno de largura {l}m e comprimento {c}m, temos a área de {l*c}m²')

print('   Controle de Terrenos')
print('-'*30)
l = float(input('Qual a largura? (m) '))
c = float(input('Qual o comprimento? (m)'))
área(l, c)