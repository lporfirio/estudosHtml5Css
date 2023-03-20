'''
Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
'''

from random import randint 
from time import sleep

def sorteia():
    print('Sorteando 5 valores da lista: ', end='')
    for n in range(5):
        numero = randint(0, 10)
        numeros.append(numero)
        print(f'{numero} ', end='', flush=True)
        sleep(0.2)
    print('PRONTO')

def somaPar():
    soma = 0
    for n in numeros:
        if n % 2 == 0:
            soma += n
    print(f'Somando os valores pares de {numeros}, temos {soma}')
    
    
    
numeros = []
sorteia()
somaPar()





