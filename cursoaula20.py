# def title(msg):
#     print('-'*30)
#     print(msg)
#     print('-'*30)
#
#
# title('SISTEMA DE ALUNOS')
# title('VAMO INTER')
#
# def tabuada(num):
#     for n in range(1, 11):
#         print(f'{num} x {n} = {num * n}')
#
#
# pergunta = int(input('Digite um número para ver a tabuada:'))
# tabuada(pergunta)

def soma(* num):
    s = 0
    for n in num:
        s += n
    print(f'Somando os números {num} temos {s}')
soma(5, 73)

