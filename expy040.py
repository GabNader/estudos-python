n1 = float(input('Qual a primeira nota?'))
n2 = float(input('Qual a segunda nota?'))
m = (n1 + n2) / 2
if m >= 7:
    print(f'Média = {m:.2f}. Aprovado.')
elif m < 5:
    print(f'Média {m:.2f}. Reprovado.')
else:
    print(f'Média {m:.2f}. Recuperação.')
