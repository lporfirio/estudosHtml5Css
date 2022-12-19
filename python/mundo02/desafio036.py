'''
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.

Calcule o valor da prestação mensal, sabendo que ele não pode exceder 30% do salário ou então o empréstimo será negado.

'''



casa = float(input('qual o valor da casa? R$'))
salario = float(input('qual o salário do comprador? R$'))
anos = float(input('em quantos anos será pago? '))

parcela = casa / (anos * 12)
parcelaMax = salario * 0.3

if parcela > parcelaMax:
    print('Seu empréstimo foi negado. Valor da parcela de R${:.2f} é muito alto'.format(parcela))
else:
    print('Seu empréstimo foi aprovado! Sua parcela será de R${:.2f}'.format(parcela))