
def leiaInt(frase):
    while True:
        try:
            n = int(input(frase))
            return n
        except:
            print('\033[31mTente de novo. (Somente números inteiros)\033[m')

def linha(tam = 42):
    return '-' * tam        
    
def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c+=1
    print(linha())
    opc = leiaInt('\033[32mSua opção:\033[m ')
    return opc

