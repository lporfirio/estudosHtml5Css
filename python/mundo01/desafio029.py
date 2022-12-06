'''
Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.

A multa vai custar R$7,00 por cada Km acima do limite.

'''

from time import sleep
carro = int(input('qual a velocidade do carro? '))
multa = (carro-80) * 7
if carro > 80:
    print('Você foi multado!')
    sleep(1)
    print('...calculando valor da multa')
    sleep(2)
    print('sua multa ficou R${},00'.format(multa))    
else:
    print('Você está dentro do limite de velocidade.')
print('tenha um bom dia, dirija com segurança!')