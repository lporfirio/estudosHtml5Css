'''
Faça um progrma que leia um número qualquer e mostre seu fatorial.

ex:
5! = 5x4x3x2x1 = 120
'''
'''
MÓDO LUQUINHA
numero = int(input('digete um número para saber seu fatorial: '))
n = numero
resultado = numero
while n != 1:
    resultado = resultado * (n-1)
    n -= 1
print(f'\033[32mO fatorial de {numero} é {resultado}\033[m')

'''
'''
resultado = resultado * (n-1)
n -= 1
print(resultado)
resultado = resultado * (n-1)
n -= 1
print(resultado)
resultado = resultado * (n-1)
n -= 1
print(resultado, n)'''

'''
MODO FÁCIL - PYTHON

from math import factorial
n = int(input('Digite um número para saber seu fatorial: '))
f = factorial(n)
print(f'o fatorial de {n} é {f}.')
'''

n = int(input('Digite um número para saber seu fatorial: '))
c = n
f = 1
print(f'calculando {n}! = ', end='')
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f'{f}.')




