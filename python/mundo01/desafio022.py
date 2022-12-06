# crie um programa que leia o nome de uma pessoa e mostre:
'''
> o nome com todas as letras maiúsculas
> o nome com todas as letras minúscultas
> quantas letras ao todo( sem considerar espaços )
> quantas letras tem o primeiro nome



'''

nome = str(input('qual seu nome? '))
print('em maiusculo fica: {}'.format(nome.upper()))
print('em minusculo fica: {}'.format(nome.lower()))
#print(len(nome))
dividir = nome.split()
juntar = ''.join(dividir)
print('tem {} letras ao todo'.format(len(juntar)))
print('o primeiro nome tem {} letras'.format(len(dividir[0])))