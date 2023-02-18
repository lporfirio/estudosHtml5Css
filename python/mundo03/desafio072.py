'''
crie um programa que tenha uma TUPLA totalmente preenchida com uma contagem por extenso, de ZERO até VINTE

seu programa deverá ler um número pelo teclado (ENTRE 0 E 20) e mostra-lo por extenso.


solução do LUQUINHA
'''

numeros = ('zero', 'um', 'dois', 'três', 'quatro',
           'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')

while True:
    n = int(input('Digite um número de 0 a 10: '))
    if 0 <= n <= 10:
        print(f'Você digitou o número {numeros[n]}')
    
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Você quer continuar [S/N] ')).strip().upper()
    if continuar == 'N':
        break
print('fim')
