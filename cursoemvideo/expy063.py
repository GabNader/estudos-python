n = int(input('Digite a quantidade de termos:'))
cont = 0
fibo1 = 0
fibo2 = 1
while n > cont:
    print(fibo1)
    fibo3 = fibo1 + fibo2
    fibo1 = fibo2
    fibo2 = fibo3
    cont += 1