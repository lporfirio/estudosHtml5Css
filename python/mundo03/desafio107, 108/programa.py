'''
107- Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.

108 - Adapte o código do desafio anterior, criando uma função adicional chamada moeda() que consiga mostrar os números como valor monetário formado
'''
from moeda import moeda, metade, aumentar, dobro, diminuir


preco = (int(input('Digite o preço: R$')))
porcentagem = 10

print(f'A metade de {moeda(preco)} é {moeda(metade(preco))}')
print(f'O dobro de {moeda(preco)} é {moeda(dobro(preco))}')
print(f'Aumentando {porcentagem}%, temos {moeda(aumentar(preco, porcentagem))}')
print(f'Diminuindo {porcentagem}%, temos {moeda(diminuir(preco, porcentagem))}')




