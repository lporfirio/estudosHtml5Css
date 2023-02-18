'''
faça um programa que leia o nome e o peso de várias pessoas, guardando tudo em uma lista. No final, mostre:

A) Quantas pessoas foram cadastradas
B) Uma listagem com as pessoas mais pesadas
C) Uma listagem com as pessoas mais leves


pessoas = []
dado = []
maisLeve = maisPesado = 0
pessoaL = pessoaP = ' '
while True:
    dado.append(str(input('Digite o nome: ')))
    dado.append(int(input('Digite o peso: ')))
    pessoas.append(dado[:])
    dado.clear()

    continuar = ' '
    while continuar not in 'SsNn':
        continuar = str(input('Deseja continuar? [S/N] ')).upper()
    if continuar == 'N':
        break

for p in pessoas:
    if p == pessoas[0]:
        maisLeve = p[1]
        maisPesado = p[1]
        pessoaL = p[0]
        pessoaP = p[0]
        #print(p)
        #print(p[0], p[1])
    if p[1] < maisLeve:
        maisLeve = p[1]
        pessoaL = p[0]
    if p[1] > maisPesado:
        maisPesado = p[1]
        pessoaP = p[0]


print(pessoas)
print(f'{len(pessoas)} pessoas foram cadastradas')
print(f'a pessoa mais pesada: {pessoaP}\na pessoa mais leve: {pessoaL}')

'''

''' tentando outro jeito'''

pessoas = []
temp = []
maisL = maisP = 0
while True:
    temp.append(str(input('Digite o nome: ')))
    temp.append(float(input('Digite o peso: ')))
    if len(pessoas) == 0:
        maisL = maisP = temp[1]
    else:
        if temp[1] > maisP:
            maisP = temp[1]
        if temp[1] < maisL:
            maisL = temp[1]
    pessoas.append(temp[:])
    temp.clear()

    continuar = ' '
    while continuar not in 'SsNn':
        continuar = str(input('Deseja continuar? [S/N] ')).upper()
    if continuar == 'N':
        break

print(f'Os dados foram {pessoas}')
print(f'Ao todo, você cadastrou {len(pessoas)} pessoas.')
print(f'Pessoas mais pesadas: ', end='')
for p in pessoas:
    if p[1] == maisP:
        print(f'{p[0]} ', end='')
print(f'\nPessoas mais leves: ', end='')
for p in pessoas:
    if p[1] == maisL:
        print(f'{p[0]} ', end='')