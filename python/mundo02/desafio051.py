'''
desenvolva um programa que leia o primeiro termo e a razão de uma PA(progressão aritmética). no final, mostre os 10 primeiro termos dessa progressão.

an = a1 + (n - 1) * r

'''
'''
print('-='*20)
print('10 termos de uma PA')
print('-='*20)
a1 = int(input('qual o primeiro termo? '))
r = int(input('qual a razão? '))
#total = a1

print(f'1° termo = {a1}')
for n in range (1, 10):
    a1 = a1 + r
    print(f'{n+1}º termo = {a1}')
'''

#------------------------------------------

primeiro = int(input('primeiro termo: '))
razao = int(input('razão: '))
decimo = primeiro + (10 - 1) * razao
for c in range(primeiro, decimo+razao, razao):
    print(f'{c}', end=' > ')
print('Acabou')


    
