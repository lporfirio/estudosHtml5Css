'''
desenvolva um progrmaa que leia QUATRO VALORES pelo TECLADO e guarde-os em uma TUPLA. No final, mostre:

A) Quantas vezes apareceu o valor 9
B) Em que posição foi digitado o primeiro valor 3.
C) quais foram os números PARES. 


solução do LUQUINHA

valor1 = int(input('Digite um número de 0 a 10: '))
valor2 = int(input('Digite mais um número de 0 a 10: '))
valor3 = int(input('Digite mais um número de 0 a 10: '))
valor4 = int(input('Digite um último número de 0 a 10: '))

valores = (valor1, valor2, valor3, valor4)

#print(valores)
print(f'Quantidade de vezes que o valor 9 apareceu: {valores.count(9)}')

c = 0
for n in range(0, len(valores)):
    if valores[n] == 3:
        print(f'O primeiro valor 3 foi digitado na {n+1}ª posição')
        c += 1
        break
if c == 0:
    print('O valor 3 não foi digitado.')

print('Os valores pares digitados foram: ', end='')
for n in valores:
    if n % 2 == 0:
        print(f'{n} ', end='')
'''


################################################

valores = (int(input('Digite um número: ')), int(input('Digite outro número: ')), int(input('Digite mais um número: ')), int(input('Digite um último número: ')) )

print(f'você digitou os valores {valores}')

#A) Quantas vezes apareceu o valor 9
print(f'Quantidade de vezes que o valor 9 apareceu: {valores.count(9)}')

#B) Em que posição foi digitado o primeiro valor 3.
if 3 in valores:
    print(f'O primeiro valor 3 foi digitado na {valores.index(3)+1}ª posição')
else:
    print(f'O valor 3 não foi digitado.')

#C) quais foram os números PARES. 
print('Os valores pares digitados foram: ', end='')
for n in valores:
    if n % 2 == 0:
        print(f'{n} ', end='')


