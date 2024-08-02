def leiadinheiro(n):
    válido = False
    while not válido:
        entrada = str(input(n)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'Erro! {entrada} é um preço inválido.')
        else:
            válido = True
            return float(entrada)
