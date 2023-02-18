'''
faça um progrma aque jogue PAR OU IMPAR com o computador. o jogo será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.


solução do LUQUINHA
import random
import time

vitorias = 0
while True:
    computador = random.randint(0, 5)
    #print(computador)
    print('-='*20)
    print('VAMOS JOGAR PAR OU ÍMPAR!!!')
    print('-='*20)

    parOuImpar = str(input('Par ou ímpar? [P/I] ')).upper()
    jogador = int(input('Digite um número: '))
    time.sleep(1)
    soma = computador + jogador
    if soma % 2 == 0:
        resultado = 'P'
        print(f'você jogou {jogador} e o computador {computador}. Total de {soma}, deu PAR')
    else:
        resultado = 'I'
        print(f'você jogou {jogador} e o computador {computador}. Total de {soma}, deu ÍMPAR')
    #print(resultado, parOuImpar)
    print('-='*20)
    if resultado != parOuImpar:
        print('você PERDEU!')
        break
    else:
        print('você VENCEU.')
    vitorias += 1
print(f'GAME OVER! Você venceu {vitorias} vezes')

'''

from random import randint
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print(f'voce jogou {jogador} e o computador {computador}. total de {total}')
    print('DEU PAR' if total % 2 == 0 else 'DEU IMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('VOCÊ VENCEU!')
            v += 1
        else:
            print('VOCÊ PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('VOCÊ VENCEU!')
            v += 1
        else:
            print('VOCÊ PERDEU!')
            break
    print('Vamos jogar novamente...')    
print(f'GAME OVER!!! Você venceu {v} vezes.')

