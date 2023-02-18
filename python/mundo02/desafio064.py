'''
crie um programa que leia vários números inteiros pelo teclado. 
O programa só vai pagar quando o usuário digitar o número '999', que é a condição de para. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag)




SOLUCAÇÃO LUQUINHA

numero = 0
total = 0
c = 0
print('caso queira parar digite o número 999')
while numero != 999:
    total = numero + total
    c += 1
    numero = int(input('digite um número inteiro: '))
print(f'foram digitados {c-1} números.. e a soma entre eles é {total}')
'''

c = soma = 0
num = int(input('Digite um número [999 para parar]: '))
while num != 999:
    soma += num
    c += 1
    num = int(input('Digite um número [999 para parar]: '))
print(f'você digitou {c} números e a soma entre eles foi {soma}')