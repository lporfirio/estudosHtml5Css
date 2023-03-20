from lib.interface import *
from lib.arquivo import *
from time import sleep

arq = 'python\mundo03\desafio115_2\cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)


while True:
    resposta = menu(['Listar Pessoas','Cadastrar Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        #opção de listar conteúdo de um arquivo
        lerArquivo(arq)   
    elif resposta == 2:
        cabecalho('Cadastrando Nova Pessoa')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(1)

