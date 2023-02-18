'''
crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final mostre quantos números digitados e qual foi a soma entre eles

SOLUCAÇÃO DO LUQUINHA
'''

c = s = 0
while True:
    n = int(input('digite um valor (999 para parar): '))
    if n == 999:
        break
    c += 1
    s += n
print(f'total de {c} números. A soma entre eles é {s} ')