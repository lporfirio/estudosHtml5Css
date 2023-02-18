
'''
variáveis compostas

tuplas
listas 
dicionários

TUPLA

"AS TUPLAS SÃO IMUTÁVEIS"

''' 
lanche = ('hamburger', 'suco', 'pizza', 'pudim')
print(lanche[-2])
print(lanche[1:3])
print(lanche[2])
print(lanche[2:])
print(lanche[:2])
print(lanche[-3:])

print(len(lanche))

for cont in range(0, len(lanche)):
    print(f'eu vou comer {lanche[cont]} na posica {cont}')


for comida in lanche:
    print(f'eu vou comer# {comida}')


for pos, comida in enumerate(lanche):
    print(f'eu vou comer# {comida} na posição {pos}')
print('comi pra caramba!')


print(sorted(lanche)) # ordem alfabética 


a = (2,5,4)
b = (5,8,1,2)
c = b + a
print(c)
print(len(c))
print(c.count(5))
print(c.index(8))
print(c.index(2, 4))

pessoa = ('gustavo', 39, 'M', 98.70)
del(pessoa)
print(pessoa)