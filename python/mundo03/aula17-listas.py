num = [2,5,9,1]
num[2] = 3
num.append(7)
num.sort()
print(num)
num.sort(reverse=True)
num.insert(2,2) # primeiro é a posição, e depois o valor
num.remove(2) # remove o primeiro valor encontrado
num.pop()
num.pop(0)
if 4 in num:
    num.remove(4)
else:
    print('não achei o número 4')
print(num)
print(f'essa lista tem {len(num)} elementos')


valores = []
valores.append(5)
valores.append(9)
valores.append(4)
valores.pop()
valores.pop()
valores.pop()

for cont in range(0, 5):
    valores.append(int(input('digite um valor: ')))

for v in valores:
    print(f'{v}...', end='')

print('')
for chave, valor in enumerate(valores):
    print(f'na posição {chave} encontrei o valor {valor}')

##########
print('')

a = [2,3,4,7]
b = a             
## no python isso é uma ligação de listas e não uma cópia, caso a lista 'b' seja alterado a 'a' também será
b[2] = 8
print(f'lista a {a}')
print(f'lista b {b}')

## para criar uma cópia:
b = a[:]
b[2] = 5
print(f'lista a {a}')
print(f'lista b {b}')
