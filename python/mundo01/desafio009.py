# faça um programa que leia um número inteiro qualquer e mostre na tela sua tabuada

numero = int(input('digite um número para ver sua tabuada: '))

tab1 = numero*1
tab2 = numero*2
tab3 = numero*3
tab4 = numero*4
tab5 = numero*5
tab6 = numero*6
tab7 = numero*7
tab8 = numero*8
tab9 = numero*9

print('-'*12)
print('a tabuada de {} é:'.format(numero))
print('{} x {} = {}'.format(numero,1,numero*1))
print('{} x {} = {}'.format(numero,2,numero*2))
print('{} x {} = {}'.format(numero,3,numero*3))
print('{} x {} = {}'.format(numero,4,numero*4))
print('{} x {} = {}'.format(numero,5,numero*5))
print('{} x {} = {}'.format(numero,6,numero*6))
print('{} x {} = {}'.format(numero,7,numero*7))
print('{} x {} = {}'.format(numero,8,numero*8))
print('{} x {} = {}'.format(numero,9,numero*9))
print('-'*12)
