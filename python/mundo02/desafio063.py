'''
Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma 'sequencia de fibonacci'.

ex:
0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8 -> 13



SOLUÇÃO DO LUQUINHA
n = int(input('Quantos termos você quer mostrar '))
c = 1
elemento = 0
f1 = 1
while c <= n:
    print(f'{elemento} -> ', end='' )
    f0 = f1
    f1 = elemento
    elemento = f0 + f1
    c += 1
print('FIM')
'''
n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print(f'{t1} > {t2}', end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(f' > {t3}', end='')
    t1=t2
    t2=t3
    cont += 1
print(' > FIM')



'''
elemento = 0
f1 = 1
print(f'{elemento} > ')
f0 = f1
f1 = elemento
elemento = f0 + f1
print(f'{elemento} > ')
f0 = f1
f1 = elemento
elemento = f0 + f1
print(f'{elemento} > ')
f0 = f1
f1 = elemento
elemento = f0 + f1
print(f'{elemento} > ')
f0 = f1
f1 = elemento
elemento = f0 + f1
print(f'{elemento} > ')
f0 = f1
f1 = elemento
elemento = f0 + f1
print(f'{elemento} > ')
f0 = f1
f1 = elemento
elemento = f0 + f1
print(f'{elemento} > ')
f0 = f1
f1 = elemento
elemento = f0 + f1
print(f'{elemento} > ')
f0 = f1
f1 = elemento
elemento = f0 + f1
print(f'{elemento} > ')
f0 = f1
f1 = elemento
elemento = f0 + f1
print(f'{elemento} > ')
'''





