'''
crie um programa que leia o ano de nascimento de 7 pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.


'''
import datetime
anoAtual = datetime.datetime.now().year
maiores = 0
menores = 0
for c in range(1,8):
    nascimento = int(input(f'Ano de nascimento da {c}ª pessoa: '))
    idade = anoAtual - nascimento
    #print(idade)
    if idade >= 21:
        maiores += 1
    else:
        menores += 1
print('')
print(f'{menores} pessoas ainda não atingiram a maioridade. \n{maiores} pessoas atingiram a maioridade.')