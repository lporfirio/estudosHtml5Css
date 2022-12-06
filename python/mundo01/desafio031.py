'''
Desenvolva um programa que pergunte a distância de uma viagem em Km. 
Calcule o preço da passagam de ônibus, cobrando RS0,50 por Km para viagens até 200km e R$0,45 para viagens mais longas.
'''

distancia = float(input('Qual a distancia da viagem em km? '))
'''passagem1 = distancia * 0.5
passagem2 = distancia * 0.45
if distancia <= 200:
    print('o preço da passagem é: R${:.2f}'.format(passagem1))
else:
    print('o preço da passagem é: R${:.2f}'.format(passagem2)) '''

if distancia <= 200:
    passagem = distancia * 0.50
else:
    passagem = distancia * 0.45
print('o preço da sua passagem será de R${:.2f}'.format(passagem))