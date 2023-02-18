'''
Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

'''
alunos = []
while True:
    # aluno = []
    # notas = []
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    # aluno.append(nome)
    # notas.append(nota1)
    # notas.append(nota2)
    # aluno.append(notas)
    # aluno.append(media)
    # alunos.append(aluno)
    alunos.append([nome, [nota1, nota2], media])

    continuar = str(input('Deseja continuar? [S/N] '))
    if continuar in 'Nn':
        break

print('-='*20)
print('No.  NOME          MÉDIA')
print('-'*30)
for i, v in enumerate(alunos):
    print(f'{i}    ', end='')
    print(f'{alunos[i][0]:13}', end='')
    print(f'{alunos[i][2]:5}')
print('-'*30)

while True:
    num = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    print(f'Notas de {alunos[num][0]} são {alunos[num][1]}')
    if num == 999:
        break

    

