'''
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
- se ele ainda vai se alistar ao serviço militar.
- se é a hora de se alistar
- se já passou do tempo do alistamento

Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
'''
import datetime

print('Você é do sexo Masculino ou Feminino?')
sexo = str.upper(input('Digite M para masculino ou F para Feminino: '))
nascimento = int(input('que ano você nasceu? '))
anoAtual = datetime.date.today().year
idade = anoAtual - nascimento

if sexo == 'F':
    print('Por ser do sexo Feminino o Alistamento não é obrigatório.')
elif sexo == 'M':
    print('Quem nasceu em {} tem {} anos em {}'.format(nascimento, idade, anoAtual))

    if idade < 18:
        print('Ainda faltam {} anos para o alistamento.'.format(18-idade))
        print('Seu alistamento será em {}.'.format(nascimento+18))
    elif idade > 18:
        print('Se passou {} ano(s) do alistamento.'.format(idade-18))
        print('Você deveria ter se alistado em {}'.format(nascimento+18))
    else:
        print('É hora de se alistar!')
else: 
    print('Sexo inválido. Tente novamente.')

