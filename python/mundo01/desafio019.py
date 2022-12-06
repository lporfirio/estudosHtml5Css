# um professor quer sorter um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido

import random
a1 = input('nome do primeiro aluno: ')
a2 = input('nome do segundo aluno: ')
a3 = input('nome do terceiro aluno: ')
a4 = input('nome do quarto aluno: ')

escolhido = random.choice([a1, a2, a3, a4])


print('o aluno escolhido foi {}'.format(escolhido))


