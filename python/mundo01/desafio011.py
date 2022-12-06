# faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m²

largura = float(input('qual é a largura da parede em metros? '))
altura = float(input('qual é a altura da parede em metros? '))

area = largura*altura
tinta = area / 2

print('será preciso {:.2f} litros de tinta para pintar uma parede de {:.2f}m²'.format(tinta,area))