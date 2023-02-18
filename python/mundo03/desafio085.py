'''
Crie um programa onde o usuário possa digitar SETE VALORES NUMÉRICOS e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final mostre os valores pares e ímpares em ordem crescente.

**uma lista com duas listas internas


temp = []
par = []
impar = []

for n in range(1,8):
    temp.append(int(input(f'Digite o {n}º número: ')))
    if temp[0] % 2 == 0:
        par.append(temp[0])
    else:
        impar.append(temp[0])
    temp.clear()

par.sort()
impar.sort()
print(f'Os valores pares digitados foram: {par}')
print(f'Os valores ímpares digitados foram: {impar}')

'''
numeros = [[],[]]
temp = []

for n in range(1,8):
    temp.append(int(input(f'Digite o {n}º número: ')))
    if temp[0] % 2 == 0:
        numeros[0].append(temp[0])
    else:
        numeros[1].append(temp[0])
    temp.clear()

print(numeros)

numeros[0].sort()
numeros[1].sort()
print(f'Os valores pares digitados foram: {numeros[0]}')
print(f'Os valores ímpares digitados foram: {numeros[1]}')
