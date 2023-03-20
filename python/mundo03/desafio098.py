'''
Exercício Python 098: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:

a- de 1 até 10, de 1 em 1
b- de 10 até 0, de 2 em 2
c- uma contagem personalizada

solução do LUQUINHA:
'''
from time import sleep
#from sys import stdout

def contador(ini, fim, pas):
    if pas == 0:
        pas = 1
    abs_pas = abs(pas) # passando o número apra ABSOLUTO, caso esteja negativo

    print('-='*25)
    print(f'Contagem de {ini} até {fim} de {abs_pas} em {abs_pas}')
    if ini < fim:
        for c in range(ini, fim+1, abs_pas): 
            print(f'{c} ', end='', flush=True)
            sleep(0.15)
            #stdout.flush()
    else:
        for c in range(ini, fim-1, -abs_pas):
            print(f'{c} ', end='', flush=True)
            sleep(0.15)
            #stdout.flush()
    print('FIM')

    
contador(1, 10, 1)
contador(10, 0, 2)
print('-='*25)
print('Agora é sua vez de personalizar a contagem!')
i = int(input('Início: '))
f = int(input('Fim:    '))
p = int(input('Passo:  '))
contador(i, f, p)