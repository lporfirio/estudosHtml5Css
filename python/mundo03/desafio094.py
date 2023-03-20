'''
Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: 
A) Quantas pessoas foram cadastradas 
B) A média de idade 
C) Uma lista com as mulheres 
D) Uma lista de pessoas com idade acima da média

Solução do LUQUINHA:
lista = []
while True:
    pessoa = {}
    pessoa['nome'] = str(input('Nome: '))
    pessoa['idade'] = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MmFf':
        sexo = str(input('Sexo [M/F]: ')).upper()
    pessoa['sexo'] = sexo

    lista.append(pessoa)

    continuar = ' '
    while continuar not in 'SsNn':
        continuar = str(input('Quer continuar? [S/N]: ')).upper()
    if continuar == 'N':
        break
#print(lista)
print('-='*30)
#A
print(f'  A) Ao todo temos {len(lista)} pessoas cadastradas.')
#B
somaIdade = 0
for p in lista:
    somaIdade += p['idade']
mediaIdade = somaIdade / len(lista)
print(f'  B) A média de idade é de {mediaIdade:.2f} anos')
#C
mulheres = []
for p in lista:
    if p['sexo'] == 'F':
        mulheres.append(p['nome'])
print(f'  C) As mulheres cadastradas foram: ', end='')
for m in mulheres:
    print(f'{m} ', end='')
print()      
#D
acimaMedia = []
for p in lista:
    if p['idade'] > mediaIdade:
        acimaMedia.append(p)
print(f'  D) Lista das pessoas que estão acimda da média: ')
for p in acimaMedia:
    print(f'     nome = {p["nome"]:8}; sexo = {p["sexo"]:4}; idade = {p["idade"]}')

print('<< ENCERRADO >>')
'''
galera = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())

    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-=' * 30)
print(galera)
print(f'Ao todo tempos {len(galera)} pessoas cadastradas.')
media = soma / len(galera)
print(f'A média de idade é de {media:.2f} anos')
print('As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] == 'F':
        print(f'{p["nome"]} ', end='')
print()
print('Lista das pessoas que estão acima da média: ')
for p in galera:
    if p['idade'] >= media:
        print('   ', end='')
        for k, v in p.items():
            print(f'{k} == {v}; ', end='')
        print()
print('<< ENCERRADO  >>')