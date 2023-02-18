'''
Aprimore o desafio anterior, mostrando no final:

A) A soma de todos os valores pares digitados
B) A soma dos valores da terceira coluna
C) O maior valor da segunda linha


solução do LUQUINHA

lista = []
somaPar = soma3 = maior2 = 0

for i in range(3):
    linha = []
    for num in range(3):
        valor = int(input(f'Digite um valor para [{i}, {num}]: '))
        linha.append(valor)
        if valor % 2 == 0:
            somaPar = somaPar + valor
        if num == 2:
            soma3 = soma3 + valor
        if i == 1:
            if num == 0:
                maior2 = valor
            else:
                if valor > maior2:
                    maior2 = valor
        valor = 0
    lista.append(linha)

for i in range(3):
    for num in range(3):
        print(f'[{lista[i][num]:^8}] ', end='')
    print()

print(f'A soma dos valores pares digitados é: {somaPar}')
print(f'A soma dos valores da terceira coluna é: {soma3}')
print(f'O maior valor na linha 2 é: {maior2}')
'''

matriz = [[0,0,0],[0,0,0],[0,0,0]]
spar = mai = scol = 0
for linha in range(0,3):
    for valor in range(0,3):
        matriz[linha][valor] = int(input(f'Digite um valor para [{linha}, {valor}]: '))

for linha in range(0,3):
    for valor in range(0,3):
        print(f'[{matriz[linha][valor]:^5}]', end='')
        if matriz[linha][valor] % 2 == 0:
            spar += matriz[linha][valor]
    print()

print(f'A soma dos valores pares digitados é: {spar}')
for linha in range(0,3):
    scol += matriz[linha][2]
print(f'A soma dos valores da terceira coluna é: {scol}')
for valor in range(0, 3):
    if valor == 0:
        mai = matriz[1][valor]
    elif matriz[1][valor] > mai:
        mai = matriz[1][valor]
print(f'O maior valor na linha 2 é: {mai}')
