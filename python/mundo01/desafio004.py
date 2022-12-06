# faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele


dado = input('digite algo:')

print('o tipo primitivo deste valor é', type(dado))
print('Só tem espaços?', dado.isspace())
print('É um número?', dado.isnumeric())
print('É alfabético?', dado.isalpha())
print('É um alfanumérico?', dado.isalnum())
print('Está em maiuscúlas?', dado.isupper())
print('Está em minuscúlas?', dado.islower())
print('Está capitalizado?', dado.istitle())