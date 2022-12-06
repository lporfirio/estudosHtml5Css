# faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, consseno e tangente desse ângulo.

import math
angulo = math.radians(float(input('qual é o ângulo? ')))
seno = math.sin(angulo)
cosseno = math.cos(angulo)
tangente = math.tan(angulo)

print('o seno é {:.2f}, o cosseno é {:.2f} e a tangente é {:.2f}'.format(seno, cosseno, tangente))
