'''
crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
ex: 

- apos a sopa
- a sacada da casa
- a torre da derrota
- anotaram a data da maratona
'''
'''
frase = str(input('digite uma frase para saber se ela é um palíndromo: '))
frase = frase.upper()
dividido = frase.split(' ')
junto = ''.join(dividido)

inverter = junto[::-1] # método para inverter a string

print(junto, inverter)

if junto == inverter:
    print(f'{frase} é um palíndromo! Olha como fica invertido: {inverter}')
else:
    print(f'{frase} não é um palíndromo! Olha como fica invertido: {inverter}')
'''

frase = str(input('Digite uma frase: ')).strip().upper()
dividido = frase.split()
junto = ''.join(dividido)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso = inverso + (junto[letra])
if junto == inverso:
    print(f'{frase} é um palíndromo! Olha como fica invertido: {inverso}')
else:
    print(f'{frase} não é um palíndromo! Olha como fica invertido: {inverso}')