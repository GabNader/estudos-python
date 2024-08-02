div = []
n = int(input('Digite um número: '))
if n <= 1:
    print('O número não é primo')
for x in range(1, n+1):
    if n % x == 0:
        div.append(x)
if len(div) > 2:
    print('O número não é primo')
else:
    print('O número é primo.')





