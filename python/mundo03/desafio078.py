'''
faça um programa que leia 5 VALORES NUMÉRICOS e guarde os em uma lista.
no final mostre qual foi o maior e o menor valor digitado e suas respectivas posições na lista


solução do luquinha
'''
valores = []
maior = menor = 0
for num in range(0,5):
    valores.append(int(input(f'Digite um número para a posição {num}: ')))
    #print(valores[num])
    if num == 0:
        maior = valores[num]
        menor = valores[num]
    if valores[num] > maior:
        maior = valores[num]
    if valores[num] < menor:
        menor = valores[num]
print(valores)

print(f'O maior valor é {maior} na posição', end='')
for index, valor in enumerate(valores):
    if valor == maior:
        print(f' {index}...', end='')

print(f'\nO menor valor é {menor} na posição', end='')
for index, valor in enumerate(valores):
    if valor == menor:
        print(f' {index}...', end='')