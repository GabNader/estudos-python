from time import sleep
def maior(* num):
    q = len(num)
    print('-='*30)
    print('Analisando os números passados...')

    if q == 0:
        print('Foram informados 0 valores')
        print('O maior valor informado foi 0')
    else:
        for valor in num:
            print(f'{valor} ', end='')
            sleep(0.5)
        print(f'Foram informados {len(num)} valores ao todo. ')
        print(f'O maior valor informado foi {max(num)}.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()



