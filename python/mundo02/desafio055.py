'''
faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos


'''


maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input(f'qual é o peso da {c}ª pessoa? '))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print('O menor peso é {}'.format(menor))
print('O maior peso é {}'.format(maior))
