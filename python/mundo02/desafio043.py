'''
Desenvolva uma lógica que leia o peso e altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:

-abaixo de 18.5: abaixo do peso
-entre 18.5 e 25: peso ideal
-25 até 30: sobrepeso
-30 até 40: obesidade
-acima de 40: obesidade mórbida

'''

peso = float(input('Qual seu peso? (Kg) '))
altura = float(input('Qual sua altura? (m) '))
imc = peso / (altura ** 2)

print('Seu IMC é {:.3f}kg/m²'.format(imc))

if imc < 18.5:
    print('abaixo de 18.5: abaixo do peso')
elif imc < 25:
    print('entre 18.5 e 25: peso ideal')
elif imc < 30:
    print('entre 25 até 30: sobrepeso')
elif imc < 40:
    print('entre 30 até 40: obesidade')
else:
    print('acima de 40: obesidade mórbida')