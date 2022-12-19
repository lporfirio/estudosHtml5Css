'''
faça um programa que leia três números e mostre qual é o maior e qual é o menor

'''

n1 = int(input('digite o primeiro valor: '))
n2 = int(input('digite o segundo valor: '))
n3 = int(input('digite o terceiro valor: '))

'''
if n1 > n2 and n1 > n3:
    print('o maior valor digitado foi {}'.format(n1))
if n2 > n1 and n2 > n3:
    print('o maior valor digitado foi {}'.format(n2))
if n3 > n1 and n3 > n2:
    print('o maior valor digitado foi {}'.format(n3))

if n1 < n2 and n1 < n3:
    print('o menor valor digitado foi {}'.format(n1))
if n2 < n1 and n2 < n3:
    print('o menor valor digitado foi {}'.format(n2))
if n3 < n1 and n3 < n2:
    print('o menor valor digitado foi {}'.format(n3))'''

#verificando maior
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
#verificando o menor
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
print('o menor número é o {}'.format(menor))
print('o maior número é o {}'.format(maior))
