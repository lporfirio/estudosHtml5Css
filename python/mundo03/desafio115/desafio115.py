'''
Crie um pequeno SISTEMA MODULARIZADO que permita cadastrar pessoas pelo seu nome e idade em um arquivo de texto simples.

O sistema só vai ter 2 opções: CADASTRAR uma nova pessoa e LISTAR todas as pessoas cadastradas

'''

# print('-'*35)
# print('MENU PRINCIPAL'.center(35))
# print('-'*35)
# print('\033[33m1\033[m - \033[36mVer pessoas cadastradas\033[m')
# print('\033[33m2\033[m - \033[36mCadastrar nova pessoa\033[m')
# print('\033[33m3\033[m - \033[36mSair do programa\033[m')
# print('-'*35)

# with open('dados.txt', 'r') as arquivo:
#     conteudo = arquivo.readlines()
# print(conteudo)
# print(len(conteudo))

'''
'''
import functions

def sistema():
    while True:
        print('-'*40)
        print('MENU PRINCIPAL'.center(35))
        print('-'*40)
        print('\033[33m1\033[m - \033[36mVer pessoas cadastradas\033[m')
        print('\033[33m2\033[m - \033[36mCadastrar nova pessoa\033[m')
        print('\033[33m3\033[m - \033[36mSair do programa\033[m')
        print('-'*40)
        try:
            opcao = int(input('\033[33mSua opção:\033[m '))
            if opcao == 1:
                print('-'*40)
                print('PESSOAS CADASTRADAS'.center(40))
                print('-'*40)
                functions.visualizar()
            elif opcao == 2:
                print('-'*40)
                print('NOVO CADASTRO'.center(40))
                print('-'*40)
                functions.cadastrar()
            elif opcao == 3:
                print('-'*40)
                print('Saindo do sistema... Até logo!'.center(40))
                print('-'*40)
                break
            else:
                print('\033[31mDigite uma das 3 opções válidas\033[m]')
        except:
            print(f'\033[31mDigite um número inteiro válido\033[m')


sistema()

