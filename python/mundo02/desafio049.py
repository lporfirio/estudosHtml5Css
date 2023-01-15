'''
refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
'''
'''
numero = int(input('Digite um número para saber sua tabuada: '))
for c in range (1, 11):
    resultado = c * numero
    print(f'{numero} x {c} = {resultado}')


'''
numero = int(input('Digite um número para saber sua tabuada: '))
for c in range(1, 11):
    print('{} x {:2} = {}'.format(numero, c, numero*c))
