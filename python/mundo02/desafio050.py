'''
desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor for impar, desconsidere-o.

'''

s = 0 # soma
cont = 0 # contador
for c in range(1,7):
    n = int(input(f'digite o {c}º número: '))
    if n % 2 == 0:
        s += n
        cont += 1
print(f'Você informou {cont} números pares e a soma foi igual a {s}')
