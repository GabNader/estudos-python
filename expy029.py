v = float(input('Qual velocidade estava o carro?'))
if v > 80:
    print('O limite desta via é 80km/h!')
    print(f' A multa custa R${(v - 80) * 7:.2f}')
else:
    print('Muito bem. Lembre-se que o limite desta via é 80km/h!')
