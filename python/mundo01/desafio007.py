# desenvolva um programa que leia duas notas de um aluno, calcule e mostre sua média

nota1 = float(input('digite a primeira nota: '))
nota2 = float(input('digite a segunda nota: '))

media = (nota1 + nota2) / 2

print('a média é {:.2f}'.format(media))