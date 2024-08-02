def listrinha(msg):
    print('-'*40)
    print(msg.center(40))
    print('-'*40)


def formatar_nome(nome):
    return ' '.join(part.capitalize() for part in nome.split())


def ver_cadastro():
    try:
        with open('pessoas.txt', 'r') as arquivo:
            pessoas = arquivo.readlines()
            if pessoas:
                for pessoa in pessoas:
                    nome, idade = pessoa.strip().split(', ')
                    print(f'{nome:<30} {idade:>5} anos')
            else:
                print('Nenhuma pessoa cadastrada.')
    except FileNotFoundError:
        print('Nenhuma pessoa cadastrada')


def cadastrar():
    while True:
        nome = input('Digite o nome da pessoa: ').strip().capitalize()
        if nome:
            break
        else:
            print('Nome não pode ser deixado em banco. Por favor, insira um nome válido.')

    while True:
        idade = input('Digite a idade da pessoa: ').strip()
        if idade.isdigit():
            idade = int(idade)
            if idade < 0:
                print('A idade não pode ser negativa. Por favor, insira uma idade válida.')
            else:
                break
        else:
            print('Entrada inválida. Por favor, insira apenas números para a idade.')

    nome_formatado = formatar_nome(nome)
    with open('pessoas.txt', 'a') as file:
        file.write(f'{nome_formatado}, {idade}\n')
    print(f'{nome_formatado} ({idade} anos) cadastrado(a) com sucesso.')
