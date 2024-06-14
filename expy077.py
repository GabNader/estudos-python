tupla = ('banana', 'abacate', 'kiwi', 'amora', 'morango', 'melancia')

for palavra in tupla:
    print(f'Na palavra {palavra}, temos')
    for letra in palavra:
        if letra in 'aeiou':
            print(letra, end='')
    print()



