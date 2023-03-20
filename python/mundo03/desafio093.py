'''
Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.


solução do Luquinha:
'''

jogador = {}
jogador['nome'] = str(input('Nome do jogador: '))
numeroDePartidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
gols = []
for g in range(numeroDePartidas):
    gols.append(int(input(f'   Quantos gols na partida {g+1}? ')))

jogador['gols'] = gols

jogador['total'] = sum(gols)
# totalDeGols = 0
# for i, v in enumerate(gols):
#     totalDeGols += v
# jogador['total'] = totalDeGols

print('-='*30)
print(jogador)
print('-='*30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f' => Na partida {i+1}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')

