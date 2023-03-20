'''
Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 'a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt('Digite um n: ')

'''


def leiaInt(frase):
    n = ''
    while n.isnumeric() == False:
        n = input(frase)
        if n.isnumeric() == False:
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')
    return n
        


n = leiaInt('Digite um número: ')
print(f'você acabou de digitar o número {n}')


