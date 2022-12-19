'''
Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

-EQUILÁTERO: todos os lados iguais
-ISÓSCELES: dois lados iguais
-ESCALENO: todos os lados diferentes
'''

print('=-'*16)
print('analisador de triângulos..')
print('=-'*16)

a = int(input('tamanho da primeira reta: ')) 
b = int(input('tamanho da segunda reta: '))
c = int(input('tamanho da terceira reta: '))

if a < b + c and b < a + c and c < b + a:
    print('as retas podem formar um triângulo ', end='')
    if a != b and b != c and a != c:
        print('ESCALENO: todos os lados diferentes.')
    elif a == b == c:
        print('EQUILÁTERO: todos os lados iguais.')
    else:
        print('ISÓSCELES: dois lados iguais.')
else:
    print('não dá para formar um triângulo')