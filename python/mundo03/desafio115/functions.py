def visualizar():
    with open('python/mundo03/desafio115/dados.txt', 'r', encoding='utf-8') as arquivo:
        conteudo = arquivo.read()
    print(conteudo)



def cadastrar():
    with open('python/mundo03/desafio115/dados.txt', 'a', encoding='utf-8') as arquivo:
        nome = str(input('Digite o nome: '))
        while True:
            try:
                idade = int(input('Digite a idade: '))
            except:
                print('\033[31mInsira um número válido\033[m')
                continue
            else:
                break
        linha = f'{nome:<24} {idade:<2} anos'
        print(f'Novo registro de {nome} adicionado.')
        arquivo.write(linha + '\n')


