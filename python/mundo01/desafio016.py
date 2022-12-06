# crie um programa que leia um número qualquer pelo teclado e mostre na tela a sua porção inteira.
# ex: 6.127 tem a parte inteira 6
import math
num = float(input('digite um número quebrado: '))
inteiro = math.floor(num)

'''print('o número {} tem a parte inteira {}'.format(num, inteiro))'''

print('o número {} tem a parte inteira {}'.format(num, math.trunc(num))) # TRUNC corta o que há depois do ponto

#-------------------
num2 = float(input('digite um número quebrado: '))
print('o valor digitado foi {} e a sua porção inteira é {}'.format(num2, int(num2)))


