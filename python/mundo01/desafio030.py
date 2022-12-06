'''
Crie um programa que leia um número inteiro e mostre se ele é PAR ou ÍMPAR.
'''

n = int(input('digite um número: '))
if n % 2 == 0:
    print('{} é par'.format(n))
else:
    print('{} é ímpar'.format(n))
