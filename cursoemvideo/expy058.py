from random import randint
pc = randint(0, 20)
escolha = []
palpites = 0
while pc != escolha:
    escolha = int(input('Faça um palpite de 0 a 20: '))
    palpites += 1
    if pc != escolha:
        print('Tente novamente!')
        if pc > escolha:
            print('O que eu pensei é maior...')
        if pc < escolha:
            print('O que eu pensei é menor...')
else:
    print(f'\nAcertou! eu estava pensando no número {pc}!')
    print(f'Acertou com {palpites} palpites')