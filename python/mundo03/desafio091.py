'''
Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.


solução do LUQUINHA:

from random import randint
from time import sleep

resultados = {}

for c in range(4):
    sleep(0.6)
    valor = randint(1,6)
    resultados[f'jogador{c+1}'] = valor
    print(f'Jogador{c+1} tirou {valor} no dado.')

print('-='*20)
sleep(0.6)
#print(resultados)
resultadosNaOrdem = dict(sorted(resultados.items(), key=lambda item: item[1], reverse=True))
'''
# lambda é a forma de trabalhar com uma função anônima, o reverse é utiliado para organizar ao contrário

'''
print('== RANKING DOS JOGADORES ==')
c = 1
for k, v in resultadosNaOrdem.items():
    sleep(0.6)
    print(f'{c}º lugar: {k} com {v}.')
    c += 1

'''
from random import randint
from time import sleep
from operator import itemgetter

jogo = {'jogador1' : randint(1, 6), 'jogador2': randint(
    1, 6), 'jogador3': randint(1, 6), 'jogador4': randint(1, 6)}
print('Valores sorteados: ')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(0.5)


ranking = []
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-='*30)
print(' == Ranking dos Jogadores ==')
for i, v in enumerate(ranking):
    print(f'  {i+1}º lugar: {v[0]} com {v[1]}')

