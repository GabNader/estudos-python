p1 = int(input('Qual o primeira termo da PA?'))
r = int(input('Qual a razão da PA?'))
p10 = p1
loops = 0
while loops < 10:
    print(f'{p10}', end='')
    p10 += r
    loops += 1
    print(', 'if loops < 10 else '.', end='')


