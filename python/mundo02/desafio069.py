'''
crie um programa que leia a IDADE e o SEXO de VÁRIAS PESSOAS. a cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final mostra:

a- quantas pessoas tem mais de 18 anos
b- quantos homens foram cadastrados
c- quantas mulheres tem menos de 20 anos


SOLUÇÃO DO LUQUINHA
'''
c = maisDe18 = homem = mulheresJovens = 0
while True:
    sexo = continuar = ' '
    idade = int(input('Qual a idade da pessoa? '))
    while sexo not in 'MF':
        sexo = str(input('Qual o sexo da pessoa? [M/F] ')).upper()[0]
    c += 1
    if idade >= 18:
        maisDe18 += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        mulheresJovens += 1
    while continuar not in 'SN':
        continuar = str(input('Você quer continuar? [S/N] ')).upper()[0]
    if continuar == 'N':
        break
print(f'temos {c} pessoas cadastradas.')
print(f'temos {maisDe18} pessoas com mais de 18 anos.')
print(f'temos {homem} homens cadastrados.')
print(f'temos {mulheresJovens} mulheres com menos de 20 anos cadastradas.')
