sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Qual o sexo? [M/F]')).strip().upper()
    if sexo != 'M' and sexo != 'F':
        print('Opção inválida, digite novamente')
if sexo == 'M':
    print('Obrigado, senhor!')
elif sexo == 'F':
    print('Obrigado, senhora')




