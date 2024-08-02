parents = []
expressao = input('digite a expressão: ')
valida = True
for n in expressao:
    if n == '(':
        parents.append(n)
    elif n == ')':
        if len(parents) == 0:
            valida = False
            break
        parents.pop()
if valida and len(parents) == 0:
    print('a expressão está correta')
else:
    print('a expressão está errada')




