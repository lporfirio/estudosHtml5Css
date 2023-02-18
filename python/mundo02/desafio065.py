'''
crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.



SOLUÇÃO DO LUQUINHA
'''

continuar = True
total = 0
maior = 0
menor = 0
c = 0
while continuar == True:
    n = int(input('digite um número: '))
    c += 1
    total = total + n
    if c == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n


    correto = False
    while correto == False:
        pergunta = str(input('você quer continhar ? [S/N] ')).upper()
        if pergunta == 'S':
            continuar = True
            correto = True
        elif pergunta == 'N':
            continuar = False
            correto = True
        else:
            correto = False
print(f'o maior valor é: {maior}, o menor é: {menor}')
print(f'a média dos {c} valores é {(total / c):.2f}')
print(f'Operação encerrada. \nObrigado, volte sempre.')

'''
resp = 'S'
media = quant = soma = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1

    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num


    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
media = soma / quant
print(f'voce digitiou {quant} e a média foi {media}')
print(f'o maior valor foi {maior} e o menor foi {menor}')
'''