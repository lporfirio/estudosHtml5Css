'''
Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

Solução do Luquinha:
'''
import datetime

pessoa = {}
pessoa['Nome'] = str(input('Nome: '))
nascimento = int(input('Ano de Nascimento: '))
anoAtual = datetime.datetime.now().year
pessoa['Idade'] = anoAtual - nascimento
pessoa['CTPS'] = int(input('Carteira de Trabalho (0 não tem): '))
if pessoa['CTPS'] != 0:
    pessoa['Contratação'] = int(input('Ano de contratação: '))
    pessoa['Salário'] = int(input('Salário? R$'))
    pessoa['Aposentadoria'] = (pessoa['Contratação'] + 35) - nascimento
for k, v in pessoa.items():
    print(f'- {k} tem o valor {v}')
