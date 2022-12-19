'''
escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.

para salários superiores a 1250,00 calcule um aumento de 10%

para os inferiores ou iguais, o aumento é de 15%
'''

salario = float(input('qual é o salário do funcionário? '))
if salario > 1250:
    reajuste = salario + (salario*0.10)
else:
    reajuste = salario + (salario*0.15)
print('o novo salário é de: R${}'.format(reajuste))