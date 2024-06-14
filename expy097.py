def escreva(txt):
    largura = len(txt) + 2
    print('~~'* largura)
    print(f'  {txt}')
    print('~~'* largura)


msg = str(input('Mensagem: '))
escreva(msg)