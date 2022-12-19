'''
Crie um programa que lçeia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:

- média abaixo de 5.0: REPROVADO
- média entre 5.0 e 6.9: RECUPERAÇÃO
- média 7.0 ou superior: APROVADO

'''

nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1+nota2)/2

if media >= 7.0:
    print('Média: {:.1f} -=- APROVADO'.format(media))
elif media >= 5.0:
    print('Média: {:.1f} -=- RECUPERAÇÃO'.format(media))
else:
    print('Média: {:.1f} -=- REPROVADO'.format(media))