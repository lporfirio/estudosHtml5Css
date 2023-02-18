'''
crie um programa que vai ler vários números e colocar em uma lista.
depois disso, mostre:

A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente
c) Se o valor 5 foi digitado e está ou não na lista



SOLUÇÃO DO LUQUINHA

lista = []
c = 0
while True:
    numero = int(input('Digite um número: '))
    lista.append(numero)
    c += 1
    continuar = ' '
    while continuar not in 'sSnN':
        continuar = str(input('Quer continuar? [S/N] ')).upper()
    if continuar == 'N':
        break
print(f'foram digitados {c} números')
lista.sort(reverse=True)
print(f'A lista ordenada em forma decrescente é: {lista}')

if 5 in lista:
    print('O valor 5 está na lista')
else:
    print('o valor 5 não está na lista')

'''

lista = []
while True:
    lista.append(int(input('Digite um número: ')))
    continuar = str(input('Quer continuar? [S/N] '))
    if continuar in 'Nn':
        break
print('-='* 30)
print(f'Você digitou {len(lista)} números.')
lista.sort(reverse=True)
print(f'A lista ordenada em forma decrescente é: {lista}')
if 5 in lista:
    print('O valor 5 está na lista.')
else:
    print('O valor 5 não está na lista.')