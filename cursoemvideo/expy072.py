while True:
    n = int(input('Qual número você quer ver por extenso? (entre 0 e 20)'))
    if n > 20:
        print('Opção inválida.')
    if n < 0:
        print('Opção inválida.')
    if 21 > n > 0:
        break

extenso = ('zero', 'um', 'dois', 'três', 'quatro',
           'cinco', 'seis', 'sete', 'oito', 'nove',
           'dez', 'onze', 'doze', 'treze', 'quatorze',
           'quinze', 'dezesseis', 'dezessete', 'dezoito',
           'dezenove', 'vinte')
print(f'{extenso[n]}')
