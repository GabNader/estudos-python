print('Sou um programa que lê a largura e a altura de uma parede e calcula a área e a quantidade de tinta necessária '
      'para pintá-la')
largura = float(input('qual a largura em metros?'))
altura = float(input('qual a altura em metros?'))
area = largura * altura
tinta = area / 2

print('para uma largura de {}m e uma altura de {}m, tem-se uma área de {}m². Além disso, seriam necessários {:.2f}l de '
      'tinta para pintar tal parede'.format(largura, altura, area, tinta))
print('(Supondo que cada litro de tinta consegue pintar uma área de 2m²')
