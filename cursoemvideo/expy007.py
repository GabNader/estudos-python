print('Sou um programa que mostra a média entre duas notas de determinado aluno.')
n1 = float(input('Digite aqui a primeira nota:'))
n2 = float(input('Digite aqui a segunda nota:'))
m = (n1 + n2) / 2

#print(f'a média é {(n1 + n2) /2}')
print('a média é {:.1f}'.format(m))
