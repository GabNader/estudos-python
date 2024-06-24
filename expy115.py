from expy115options import listrinha #ver_cadastro, cadastrar
listrinha('MENU PRINCIPAL')
print('1 - Ver pessoas cadastradas')
print('2 - Cadastrar nova pessoa')
print('3 - Sair do Sistema')
while True:
    try:
        option = int(input('Sua opção: '))
        if option == 1:
            listrinha('Opção 1')
            #ver_cadastro()
        elif option == 2:
            listrinha('Opção 2')
            #cadastrar()
        elif option == 3:
            listrinha('Obrigado, volte sempre...')
            break
        else:
            print('Opção inválida')
    except ValueError:
        print('opção inválida')