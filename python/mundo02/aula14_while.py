'''
estrutura de repetição com teste lógico

while not apple:
    if chão:
        passo
    if vazio:
        pula
    if moeda:
        pega
pega
'''
'''
for c in range(1,10):
    print(c)
print('fim')


c = 1
while c < 10:
    print(c)
    c += 1
print('fim')

for c in range(1, 5):
    n = int(input('digite um valor: '))
print('fim')

n = 1
while n != 0:
    n = int(input('digite um valor: '))
print('fim')

r = 'S'
while r == 'S':
    n = int(input('digite um valor: '))
    r = str(input('Quer continuar? [S/N] ')).upper()
print('Fim')
'''

## quantos números pares e impares
n = 1
par = impar = 0
while n != 0:
    n = int(input('digite um valor: '))
    if n != 0:
        if n & 2 == 0:
            par += 1
        else:
            impar += 1
print('fim')
print(f'par: {par}, impar: {impar}.')
