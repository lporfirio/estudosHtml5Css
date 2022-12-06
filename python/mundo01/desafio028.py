'''
Escreva um programa que faça o computador "pensar" em um número entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.

O programa deverá escrever na tela se o usuário venceu ou perdeu.
'''

'''import random
n = random.choice([0,1,2,3,4,5])
#print(n)

chute = int(input('O computador escolheu um número de 0 a 5, você consegue adivinhar qual? '))

if n == chute:
    print('Você acertou!')
else:
    print('Você errou!')'''

from random import randint
from time import sleep
computador = randint(0,5)

print('-=-' * 20)
print('O computador escolheu um número de 0 a 5, você consegue adivinhar qual?')

print('-=-' * 20)
chute = int(input('digite um número de 0 a 5: '))
print('...processando...')
sleep(2)
if computador == chute:
    print('Parabéns!!! você acertou!')
else:
    print('Ganhei! haha, eu pensei no número {} e não no {}!'.format(computador, chute))

