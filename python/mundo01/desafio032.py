'''
Crie um programa que leia um ano qualquer e mostre se ele é BISSEXTO
'''

# Qualquer ano que seja uniformemente divisível por 4 é um ano bissexto: por exemplo, 1988, 1992 e 1996 são anos bissextos

import datetime
ano = int(input('Digite um ano para saber se ele é bissexto ou não (coloque 0 para saber do ano atul): '))

if ano == 0:
    ano = datetime.date.today().year #para pegar o ano atual
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0 :
    print('{} é um ano bissexto!'.format(ano))
else:
    print('{} não é um ano bissexto!'.format(ano))