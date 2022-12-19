'''
Escreva um programa aque leia um número inteiro qualquer e peça para o usuário escolher qual será a base da conversão:
- 1 para binário
- 2 para octal
- 3 para hexadecimal
'''

inteiro = int(input('digite um número inteiro: '))

print('''escolha a base da conversao sabendo que :

- 1 para binário 
- 2 para octal 
- 3 para hexadecimal 

''')

conversao = int(input('sua opção: '))

bin = bin(inteiro)[2:]
oct = oct(inteiro)[2:]
hex = hex(inteiro)[2:]

if conversao == 1:
    print('{} convertido para binário fica: {}'.format(inteiro, bin))
elif conversao == 2:
    print('{} convertido para octal fica: {}'.format(inteiro, oct))
elif conversao == 3:
    print('{} convertido para hexadecimal fica: {}'.format(inteiro, hex))
else:
    print('opção inválida, tente novamente')
