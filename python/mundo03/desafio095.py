'''
Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.



solução do LUQUINHA:
'''
jogadores = []
while True:
    jogador = {}
    jogador['nome'] = str(input('Nome do jogador: '))
    numeroDePartidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    gols = []
    for g in range(numeroDePartidas):
        gols.append(int(input(f'   Quantos gols na partida {g+1}? ')))

    jogador['gols'] = gols

    jogador['total'] = sum(gols)
    jogadores.append(jogador)

    while True:
        continuar = str(input('Quer continuar? [S/N] ')).upper()[0]
        if continuar in 'SN':
            break
    if continuar == 'N':
        break    

print(jogadores)
print('-='*30)
print('cod nome            gols          total')
print('-'*45)
#for i, j in enumerate(jogadores):
#    print(f'{i:3} {j["nome"]:15} {str(j["gols"]):15} {j["total"]}')
for k, v in enumerate(jogadores):
    print(f'{k}   ', end='')
    for dados in v.values():
        print(f'{str(dados):16}', end='')
    print()

print('-'*45)

while True:
    j = int(input('Mostrar dados de qual jogador? (usar o "cod" para escolher, 999 para parar) '))
    if j == 999:
        break    
    if j < 0 or j > (len(jogadores)-1):
        print(f'Não existe o jogador com cod {j}')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {jogadores[j]["nome"]}')
        for i, v in enumerate(jogadores[j]['gols']):
            print(f'     No jogo {i+1}, fez {v} gols.')
    print('-'*45)
print('<< VOLTE SEMPRE >>')