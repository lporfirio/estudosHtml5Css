'''
faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 a 500.
'''

'''
somaTotal = 0
for c in range(1, 500):
    if (c % 2) != 0:
        if (c % 3) == 0:
            somaTotal = somaTotal + c
print('o resultado é {}'.format(somaTotal))
'''

somaTotal = 0
valor = 0
for c in range(3, 500, 3):
    if (c % 2) != 0:
        valor += 1
        somaTotal += + c
print(f'a soma de todos os {valor} valores solicitados é {somaTotal}')


