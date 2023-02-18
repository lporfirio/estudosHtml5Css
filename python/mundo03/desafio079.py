'''
crie um progrma onde o usuário possa digitar vários VALORES NUMÉRICOS e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado.
no final, serão exibidos todos os VALORES ÚNICOS digitados, em ordem crescente



solução do Luquinha:
'''

lista = []
while True:
    valor = int(input('Digite um número: '))
    if valor not in lista:
        lista.append(valor)
        print('Valor adicionado com sucesso.')
    else:
         print('Valor duplicado, não vou adicionar')

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).upper()
    if continuar == 'N':
            break
lista.sort()
print(lista)