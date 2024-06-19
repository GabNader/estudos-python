from utilidadesCeV import moeda
from utilidadesCeV import dado

print("Chamando leiadinheiro")  # Debug
preco = dado.leiadinheiro('Digite um número: ')
print(f"Valor lido: {preco}")  # Debug
print("Chamando resumo")  # Debug
moeda.resumo(preco, 10, 20)

