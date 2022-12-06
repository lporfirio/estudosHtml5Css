#faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

import math

co = float(input('qual o cateto oposto do triângulo?: '))
ca = float(input('qual o cateto adjacente do triângulo?: '))

print('a hipotenusa é {:.2f}'.format(math.hypot(co,ca)))