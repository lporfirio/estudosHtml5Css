'''
crie uma TUPLA preenchida com os 20 PRIMEIROS colocados da Tabela do CAMPEONATO BRASILEIRO DE FUTEBOL, na ordem de colocação. Depois mostre:

A) apenas os 5 PRIMEIROS colocados.
B) os ÚLTIMOS 4 colocados da tabela.
C) uma lista com os times em ORDEM ALFABÉTICA.
D) em que POSIÇÃO na tabela está o time da CHAPECOENSE


'''

serieA = ('palmeiras', 'internacional', 'fluminense', 'corinthians', 'flamengo', 'athletico-PR', 'atlético-MG', 'fortaleza', 'são paulo', 'américa-mg', 'botafogo', 'santos', 'goias', 'bragantino', 'coritiba', 'cuiabá', 'ceará', 'atlético-GO', 'avaí', 'juventude')

print('-='*20)
print('Times da série A do campeonato Brasileiro: ', serieA[0:5])
print('-='*20)
print('Primeiros 5 colocados: ', serieA[0:5])
print('-='*20)
print('Últimos 4 são:', serieA[-4:])
print('-='*20)
print('Times em ordem alfabética: ', sorted(serieA))
print('-='*20)
print(f'O Flamengo está na {serieA.index("flamengo")+1}ª posição')   # neste caso utilizar aspas duplas dentro do format
print('-='*20)