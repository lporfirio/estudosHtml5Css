'''
Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

an = a1 + (n - 1) * r


SOLUÇÃO DO LUQUINHA

a1 = int(input('Qual é o primeiro termo da PA? '))
r = int(input('Qual é a razão da PA? '))
c = 1
while c <= 10:
    termo = a1 + (c - 1) * r
    #print(f'o {c}° termo é {termo}')
    print(f'{termo}', end=' > ')
    c += 1
print('Acabou')

'''

primeiro = int(input('primeiro termo: '))
razao = int(input('razao: '))
termo = primeiro
cont = 1
while cont <= 10:
    print(f'{termo} > ', end='')
    termo += razao
    cont += 1
print('fim')
