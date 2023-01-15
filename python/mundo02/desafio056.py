'''
desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
> a média de idade do grupo
> qual é o nome do homem mais velho.
> quantas mulheres tem menos de 20 anos.

'''
'''
idadeTotal = 0
idadeHomemMaisVelho = 0
mulheresJovens = 0
for p in range(1, 5):
    nome = str(input(f'Qual o nome da {p}ª pessoa? '))
    idade = int(input(f'Qual é a idade da {p}ª pessoa? '))
    sexo = str(input(f'Qual é o sexo da {p}ª pessoa? Masculino ou Feminino? ')).lower()

    # média de idade do grupo
    idadeTotal += idade

    # para descobrir o homem mais velho
    if sexo == 'masculino':
        if idade > idadeHomemMaisVelho:
            idadeHomemMaisVelho = idade
            nomeHomemMaisVelho = nome
    
    # número de mulheres com menos de 20 anos
    if sexo == "feminino":
        if idade < 20:
            mulheresJovens += 1

print(f'a média de idade do grupo é de {idadeTotal / 4} anos')
print(f'o homem mais velho do grupo é o {nomeHomemMaisVelho}, com {idadeHomemMaisVelho} anos')
print(f'existe um total de {mulheresJovens} mulheres com menos de 20 anos no grupo')
'''

somaIdade = 0
idadeHomemMaisVelho = 0
nomeVelho = ''
totMulher20 = 0
for p in range(1,5):
    print(f'---- {p}ª PESSOA ----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaIdade += idade

    if p ==1 and sexo in 'Mm':
        idadeHomemMaisVelho = idade
        nomeVelho = nome
    if sexo in 'Mm' and idade > idadeHomemMaisVelho:
        idadeHomemMaisVelho = idade
        nomeVelho = nome
    if sexo in 'Ff' and idade < 20:
        totMulher20 += 1

print(f'a média de idade do grupo é {somaIdade / 4} anos')
print(f'o homem mais velho tem {idadeHomemMaisVelho} anos e se chama {nomeVelho}')
print(f'existe um total de {totMulher20} mulheres com menos de 20 anos.')



