'''
crie um progrma aque leia o NOME e o PREÇO de VÁRIOS PRODUTOS. O programa deverá perguntar se o USUÁRIO vai continuar. No final, mostre:

A- qual o TOTAL GASTO na compra
B- quantos produtos custam MAIS de R$1000.
C- qual é o NOME do produto mais BARATO

solução do LUQUINHA
total = maisDeMil = c = 0
while True:
    nome = str(input('Qual o nome do produto? ')).strip()
    preco = float(input('Qual o preço do produto? '))
    total += preco
    c += 1
    if preco > 1000:
        maisDeMil += 1
    if c == 1:
        maisBarato = preco
        nomeMaisBarato = nome
    else:
        if preco < maisBarato:
            maisBarato = preco
            nomeMaisBarato = nome
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(
            input('Você quer continuar a adicionar produdos? [S/N]')).strip().upper()
    if continuar == 'N':
        break
print(f'Total gasto na compra: R${total:.2f}')
print(f'{maisDeMil} produtos custam mais de R$1000.')
print(f'o produto mais barato é {nomeMaisBarato}')
'''
total = totmil = menor = cont = 0
barato = ''
while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('preço: R$'))
    cont += 1
    total += preco
    if preco > 1000:
        totmil += 1

    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {totmil} produto custando mais de R$1000.')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')