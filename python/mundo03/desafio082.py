'''
crie um programa que vai ler vários números e colocar em uma lista.

depois, crie duas listas extras que vão conter apenas os valores pares e os valores impares digitados, respectivamente.

ao final motre as três listas geradas.

'''
lista = []
while True:
    lista.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar? [S/N}] '))
    if resp in 'nN':
        break
listaPar = []
listaImpar = []
for valor in lista:
    print(valor)
    if valor % 2 == 0:
        listaPar.append(valor)
    else:
        listaImpar.append(valor)
print(f'Todos os valores: {lista}')
print(f'Valores pares: {listaPar}.')
print(f'Valores ímpares: {listaImpar}')