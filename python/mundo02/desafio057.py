'''
faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.
'''
'''
resposta = ''
while resposta != 'correto' :
    sexo = str(input('Qual o sexo da pessoa? [M/F] : ')).upper()
    if sexo == 'M':
        resposta = 'correto'
        sexo = 'Masculino'
    elif sexo == 'F':
        resposta = 'correto'
        sexo = 'Feminino'
    else:
        resposta = 'incorreto'
        print("Entrada inválida. Por favor, informe 'M' ou 'F'.")
print(f'OK, obrigado \nSexo: {sexo}')
'''

sexo = str(input('informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso')