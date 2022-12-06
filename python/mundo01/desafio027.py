'''
faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

ex: Ana Maria de Souza
primeiro = Ana
último : Souza


'''

nome = str(input('qual o nome completo? ')).strip()
lista = nome.split()
ultimo = lista[len(lista)-1]
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(lista[0]))
print('Seu último nome é {}'.format(ultimo))

