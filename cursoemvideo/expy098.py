from time import sleep
def contador (início, fim, passo):
    if fim > início or passo < 0:
        if passo == 0:
            for x in range(início, fim, 1):
                print(f'{x} ', end='')
                sleep(0.5)
        else:
            for x in range(início, fim, passo):
                print(f'{x} ', end='')
                sleep(0.5)
    elif início > fim:
        if passo == 0:
            for x in range(início, fim, -1):
                print(f'{x} ', end='')
                sleep(0.5)
        else:
            for x in range(início, fim, - passo):
                print(f'{x} ', end='')
                sleep(0.5)
    print('FIM!')


print('-='*15)
print('contagem de 1 até 10 de 1 em 1')
contador(1, 11, 1)
print('-='*15)
print('contagem de 10 até 0 de 2 em 2:')
contador(10, -2, -2)
print('-='*15)
print('Agora é sua vez de personalizar a contagem!')
p1 = int(input('Início: '))
pfim = int(input('Fim: '))
r = int(input('Passo: '))
print('-='*15)
print(f'Contagem de {p1} até {pfim} de {r} em {r}:')
contador(p1, pfim, r)
