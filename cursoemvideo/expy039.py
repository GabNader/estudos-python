from datetime import datetime
n = int(input('Em que ano nasceu o jovem?'))
a = datetime.now().year
if a - n == 18:
    print('Está na hora de se alistar!')
elif a - n > 18:
    print('Já passou da hora de se alistar!')
    if a - n == 19:
        print('Inclusive, está 1 ano atrasado!')
    else:
        print(f'Inclusive, está {(a - n) - 18} anos atrasado!')
else:
    print('Um dia você ainda vai se alistar!')
    if a - n == 17:
        print('Inclusive, será ano que vem!')
    else:
        print(f'Inclusive, será daqui {(n - a) + 18} anos... ')