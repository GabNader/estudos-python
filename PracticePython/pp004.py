n = (int(input('Digite um número que eu te digo os divisores dele:')))
div = []
for x in list(range(1, n + 1)):
    if n % x == 0:
        div.append(x)
print(div)

