'''
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

- à vista: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros
'''

import time

print('')
produto = float(input('Preço das compras: R$ '))

print('''
FORMAS DE PAGAMENTO:
[1]- à vista: 10% de desconto
[2]- à vista no cartão: 5% de desconto
[3]- em até 2x no cartão: preço normal
[4]- 3x ou mais no cartão: 20% de juros
''')
pagamento = int(input('Escolha a opção: '))

if pagamento == 1:
    valorFinal = produto - (produto * 0.1)
elif pagamento == 2:
    valorFinal = produto - (produto * 0.05)
elif pagamento == 3:
    valorFinal = produto
    print('2 parcelas de: R${:.2f}'.format(valorFinal/2))
elif pagamento == 4:
    valorFinal = produto + (produto * 0.2)
    parcelas = int(input('Em quantas parcelas? '))
    print('{} parcelas de: R${:.2f}'.format(parcelas, valorFinal/parcelas))
else: 
    valorFinal = 0
    time.sleep(2)
    print('\033[31m[ERRO] dados errados, tente novamente.\033[m')

print('o preço final é de: R${:.2f}'.format(valorFinal))

