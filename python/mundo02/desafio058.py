'''
Melhore o jogo do desafio 028 onde o computador vai "pensar" um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até aceitar, mostrando no final quantos palpites foram necessários para vencer.
'''
'''
import random
computador = random.randint(0, 10)
print('Tente adivinhar o número de 0 a 10')
jogador = int(input('digite um número: '))
palpite = 1
while computador != jogador:
    palpite += 1
    if computador > jogador:
        print('Mais...tente mais uma vez...')
    elif computador < jogador:
        print('Menos...tente mais uma vez...')
    jogador = int(input('Digite um número:'))
print(f'você acertou!!! na tentativa número {palpite}')
'''

from random import randint
computador = randint(0,10)
print('O computador acabou de pensar em um número entre 0 e 10. \nTente adivinhar qual foi.')
acertou = False
palpiltes = 0
while not acertou:    ## só irá parar quando 'acertou' for igual a 'True'
    jogador = int(input('Qual é seu palpite? '))
    palpiltes += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... tente mais uma vez.')
        elif jogador > computador:
            print('Menos... tente mais uma vez.')
print(f'acertou com {palpiltes} tentativas. Parabéns!')
