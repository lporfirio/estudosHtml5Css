'''
desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo

'''
print('=-'*16)
print('analisador de triângulos..')
print('=-'*16)
a = int(input('tamanho da primeira reta: ')) 
b = int(input('tamanho da segunda reta: '))
c = int(input('tamanho da terceira reta: '))

if a < b + c and b < a + c and c < b + a:
    print('as retas podem formar um triângulo')
else:
    print('não dá para formar um triângulo')