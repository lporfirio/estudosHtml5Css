'''
Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
- o primeiro valor é maior
- o segundo valor é maior
- não existe valor maior os dois são iguais

'''

a = int(input('digite o  primeiro valor: '))
b = int(input('digite o  segundo valor: '))

if a > b:
    print('o primeiro valor é maior ')
elif b > a:
    print('o segundo valor é maior')
else:
    print('não existe valor maior, os dois são iguais')
