'''
Reescreva a função leiaint() que fizemos no desafio 104, incuindo agora a possibilidade da digitação de um número do tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

'''

def leiaInt(frase):
    while True:
        try:
            n = int(input(frase))
            return n
        except:
            print('\033[31mTente de novo. (Somente números inteiros)\033[m')

def leiaFloat(frase):
    while True:
        try:
            n = float(input(frase))
        except (ValueError, TypeError):
            print ('\033[31mTente de novo. (Somente números reais.)\033[m')
            continue
        else:
            return n



n1 = leiaInt('Digite um número inteiro: ')
n2 = leiaFloat('Digite um número real: ')
print(f'você acabou de digitar o inteiro {n1} e o real {n2}')