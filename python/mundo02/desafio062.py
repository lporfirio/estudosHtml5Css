'''
Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disse que quer mostrar 0 termos.

SOLUÇÃO DO LUQUINHA
'''

primeiro = int(input('primeiro termo: '))
razao = int(input('razao: '))
termo = primeiro
cont = 1
repeticoes = 10
contTermo = 0
while repeticoes != 0:
    while cont <= repeticoes:
        print(f'{termo} > ', end='')
        termo += razao
        cont += 1
        contTermo += 1
    print('pausa')
    repeticoes = int(input('Quantos termos você quer mostrar a mais? '))
    cont = 1
print(f'fim... total de {contTermo} termos')

'''
SOLUÇÃO DO CURSO
primeiro = int(input('primeiro termo: '))
razao = int(input('razao: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{termo} > ', end='')
        termo += razao
        cont += 1
    print('pausa')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print(f'fim... total de {total} termos mostrados')
'''