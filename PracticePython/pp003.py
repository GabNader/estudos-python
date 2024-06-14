from random import sample
a = sample(range(1, 100), 10)
print(f'Os números são {a}')
b = []
for x in a:
    if x % 2 == 0:
        b.append(x)
print('Dentre os dez números aleatórios, os pares são:')
print(b)
