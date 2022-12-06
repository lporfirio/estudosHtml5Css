#crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = str(input('qual é seu nome completo? ')).strip()
nome2 = nome.upper()

print('Seu nome tem Silva? {} '.format('SILVA' in nome2))
