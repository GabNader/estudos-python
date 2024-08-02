from datetime import datetime
idade = int(input('Em que ano o atleta nasceu?'))
CurrentYear = datetime.now().year
if (CurrentYear - idade) <= 9:
    print('Categoria Mirim')
elif (CurrentYear - idade) <= 14:
    print('Categoria Infantil')
elif (CurrentYear - idade) <= 19:
    print('Categoria Junior')
elif (CurrentYear - idade) <= 25:
    print('Categoria Sênior')
else:
    print('Categoria Master')
