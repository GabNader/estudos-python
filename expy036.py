casa = float(input('Qual o valor do imóvel?'))
s = float(input('Qual seu salário?'))
t = int(input('Em quantos anos você pretende pagar?'))
pm = (casa / t) / 12
print(f'Nesse caso, o valor da prestação mensal ficaria em R${pm:.2f}.')
if pm > (s * 0.30):
    print('O que excede nossa cota de 30% do salário.')
    print(f'Com esses termos, infelizmente, o empréstimo será negado.')
else:
    print(f'Parabéns, seu empréstimo foi aprovado!')
    print(f'R${pm:.2f} mensais ao longo de {t} anos.')
