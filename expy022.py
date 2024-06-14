n = str(input('Qual seu nome completo?')).capitalize()
ns = n.replace(' ', '')
print(f'Seu nome completo tem {len(ns)} letras')
separado = n.split()
print(f'Seu primeiro nome é {separado[0]} e tem {len(separado[0])} letras')



