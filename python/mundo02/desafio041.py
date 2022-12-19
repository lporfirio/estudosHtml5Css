'''
Escreva um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com sua idade:

-até 9 anos: MIRIM
-até 14 anos: INFANTIL
-até 19 anos: JUNIOR
-até 20 anos: SÊNIOR
-acima: MASTER

'''

import datetime
atual = datetime.date.today().year

aluno = int(input('Em que ano você nasceu? '))
idade = atual - aluno
print('sua idade é {} anos'.format(idade))

if idade <= 9:
    print('sua categoria é a MIRIM.')
elif idade <= 14:
    print('sua categoria é a INFANTIL.')
elif idade <= 19:
    print('sua categoria é a JUNIOR.')
elif idade <= 25:
    print('sua categoria é a SÊNIOR.')
else:
    print('sua categoria é a MASTER.')

