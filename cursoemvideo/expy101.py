def voto(ano):
    from datetime import date
    today = date.today()
    year = today.year
    idade = year - ano
    print(f'Com {idade} anos: ', end='')
    if idade < 16:
        return 'VOTO NEGADO.'
    elif 18 > idade >= 16 or idade >= 65:
        return 'VOTO FACULTATIVO'
    elif 65 > idade >= 18:
        return 'VOTO OBRIGATÓRIO'


print('-='*15)
pergunta = int(input('Ano de nascimento: '))
print(voto(pergunta))
