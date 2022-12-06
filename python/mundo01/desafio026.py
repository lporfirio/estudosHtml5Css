"""
faça um programa que leia uma frase pelo teclado e mostre:

> quantas vezes aparece a letra A:
> em que posição ela aparece a primeira vez:
> em que posição ela aparece a última vez:

"""

frase = str(input('Digite uma frase: ')).strip()
frase2 = frase.lower()
print('a letra "a" aparece {} vezes na frase'.format(frase2.count('a')))
print('a letra "a" aparece pela primeira vez na posição {}'.format(frase2.find('a')+1))
print('a letra "a" aparece pela última vez na posição {}'.format(frase2.rfind('a')+1))