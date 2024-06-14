listagem = ('pão', 1, 'leite', 3.50, 'frango', 19.90, 'farinha', 5.50, 'arroz', 9.99)
for i in listagem:
    if type(i) is str:
        print(f'{i:.<32}', end='')
    else:
        print(f'R$ {i:.2f}')
print('--' * 20)