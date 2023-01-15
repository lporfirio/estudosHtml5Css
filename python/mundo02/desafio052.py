'''faça um programa que leia um número inteiro e diga se ele é ou não um número primo


o número primo só pode ser dividido 2 vezes, por 1 e por ele mesmo.



'''


numero = int(input('Digite um número: '))
print('')
totalDeDivisoes = 0
for c in range(1, numero+1):
 if numero % c == 0:
    totalDeDivisoes += 1
    print(f'\033[32m{c}\033[m', end=' ')
 else:
    print(f'\033[31m{c}\033[m', end=' ')
print('')
print(f'\n{numero} foi dividido um total de {totalDeDivisoes} vezes, ', end='')
if totalDeDivisoes == 2:
    print('logo ele \033[32mé um número primo\033[m.')
else:
    print('logo ele \033[31mnão é um número primo\033[m.')

