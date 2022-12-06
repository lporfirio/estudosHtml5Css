# o professor que sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada

import random
a1 = input('nome do primeiro aluno: ')
a2 = input('nome do segundo aluno: ')
a3 = input('nome do terceiro aluno: ')
a4 = input('nome do quarto aluno: ')

alunos = [a1, a2, a3, a4]
random.shuffle(alunos)

print('a ordem de apresentação será {}, {}, {} e {}'.format(alunos[0], alunos[1], alunos[2], alunos[3]))