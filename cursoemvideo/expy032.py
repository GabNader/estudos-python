a = int(input('Diga-me o ano e te falo se é bissexto (digite 0 para analisar o ano atual:'))
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print(f'O ano {a} é bissexto')
else:
    print(f'O ano {a} não é bissexto')
