'''
crie um programa que vai gerar CINCO NÚMEROS ALEATÓRIOS e colocar em uma TUPLA.


depois disso, mostre a listagem de números gerados e também indique o MENOR e o MAIOR valor que estão na tupla.


solução do LUQUINHA

from random import randint

aleatorios = (randint(0, 999), randint(0, 999), randint(0, 999), randint(0, 999), randint(0, 999))

# mostrar a lista de números gerados:
print(f'Números gerados: {aleatorios}')

# verificar o maior e o maior número:
maior = 0
menor = 0
c = 0
for n in aleatorios:
    if c == 0:
        maior = n
        menor = n
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    c += 1

# mostrar o maior e o menor número:
print(f'O maior número gerado foi {maior} e o menor foi {menor}.')
'''

from random import randint
numeros = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
print('Os valores sorteados foram: ', end='')
for n in numeros:
    print(f'{n} ', end='')
print(f'\no maior valor sorteado foi {max(numeros)}')
print(f'o menor valor sorteado foi {min(numeros)}')



