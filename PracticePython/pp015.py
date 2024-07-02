from time import sleep
def reverso():
    frase = str(input('Frase: ')) ##pergunta a frase para o usuário e separa as palavras da frase
    inverter = frase.split()[-1::-1] ##analisa detrás pra frente
    mostra = ' '.join(inverter) ##pega a frase invertida e adiciona numa string, pra sumir com os colchetes e vírgulas
    print('invertendo frase', end='') ##um loop apenas pra mostrar com um delayzinho por pura estética
    for n in range(0,3):
        if n == 2:
            print('.')
        else:
            print('.', end='')
        sleep(0.5)
    print(mostra)


reverso()