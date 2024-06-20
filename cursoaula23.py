try:
    a = int(input('numerador'))
    b = int(input('denominador'))
    r = a / b
except (ValueError, TypeError):
    print('deu erro. Os dados informados não funcionam para o programa em questão.')
except ZeroDivisionError:
    print('Não dá pra dividir por zero pae')
except KeyboardInterrupt:
    print('o usuário preferiu não informar os dados.')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')
else:
    print(f' o resultado é {r}')
finally:
    print('volte sempre.')
