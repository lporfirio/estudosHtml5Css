'''
crie um programa que crie uma MATRIZ de dimensão 3x3 e preencha com valores lidos pelo teclado.

No final, mostre a matriz na tela, com a formatação correta


lista = [[] for i in range(9)]
for n in range(0, 9):
    inteiro = int(input('digite um número: '))
    lista[n].append(inteiro)

print(f'[{lista[0][0]:^5}] [{lista[1][0]:^5}] [{lista[2][0]:^5}]')
print(f'[{lista[3][0]:^5}] [{lista[4][0]:^5}] [{lista[5][0]:^5}]')
print(f'[{lista[6][0]:^5}] [{lista[7][0]:^5}] [{lista[8][0]:^5}]')
'''

lista = []
for i in range(3):
    linha = []
    for num in range(3):
        linha.append(int(input(f'Digite um valor para [{i}, {num}]: ')))
    lista.append(linha)

for i in range(3):
    for num in range(3):
        print(f'[{lista[i][num]:^8}] ', end='')
    print()

