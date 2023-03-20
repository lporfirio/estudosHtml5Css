'''
Exercício Python 106: Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores.


\033[style;text;back m



def pyhelp():
    while True:
        print('\033[0;33;42m~'*30)
        print('  SISTEMA DE AJUDA PyHELP')
        print('~'*30, end='')
        print('\033[m')
        
        comando = str(input('Função ou Biblioteca > ')).lower()
        
        print('\033[44m~'*46)
        print(f"  Acessando o manual do comando '{comando}' ")
        print('~'*46, end='')
        print('\033[m')
       
        print('\033[7m')
        print(help(comando))
        print('\033[m')
        
        if comando == 'fim':
            break

    print('\033[41m~'*13)
    print('  ATÉ LOGO')
    print('~'*13, end='')
    print('\033[m')
pyhelp()
'''

from time import sleep
c = ('\033[m',  # 0 - sem cor
     '\033[0;30;41m',  # 1 - vermelho
     '\033[0;30;42m',  # 2 - verde
     '\033[0;30;44m',  # 3 - azul
     '\033[7;30m]'     # 4 - branco
     )

def titulo(msg, cor=0):
    tam= len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')
    sleep(0.3)

def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 3)
    print(c[4], end='')
    help(com)
    print(c[0], end='')
    sleep(0.3)

# PROGRAMA PRINCIPAL
while True:
    titulo('SISTEMA DE AJUDA PYHELP', 2)
    comando = str(input('Função ou Biblioteca > ')).lower()
    if comando == 'fim':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO!', 1)
