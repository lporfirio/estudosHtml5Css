'''
Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

'''
from time import sleep

def maior(*num):
    print('-='*30)
    print('Analisando os valores passados.')
    m = 0
    for ind, valor in enumerate(num):
        if ind == 0:
            m = valor
        else:
            if valor > m:
                m = valor
        print(f'{valor} ', end='', flush=True)
        sleep(0.2)
    print(f'Foram imformados {len(num)} valores.')
    print(f'O maior valor informado foi {m}.')

maior(2, 0, 1, 5, 15)
maior(20,0, 13, 15)
maior(12, 2, 25, 14)
maior(0)