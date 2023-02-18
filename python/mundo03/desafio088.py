'''
Faça um programa que ajude um jogador da mega sena a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 a 60 para cada jogo, cadastrando tudo em uma lista composta.

'''

from random import randint
import time

jogos = []

qtdjogos = int(input('Quantos palpites de jogo você quer? '))

for p in range(qtdjogos):
    palpites = []
    while len(palpites) < 6:
        numero = randint(1,60)
        if numero not in palpites:
            palpites.append(numero)
    palpites.sort()
    jogos.append(palpites)
time.sleep(0.5)
print('-='*3, f'gerando {qtdjogos} palpites', '-='*3) 
time.sleep(1.2)
for i, v in enumerate(jogos):
    time.sleep(0.8)
    print(f'Jogo {i+1}: {v}')
print('-='*5, 'BOA SORTE!', '-='*5)

