'''
cont = 1
while cont <= 10:
    print( cont, ' -> ', end='')
    cont += 1
print('acabou')

cont = 1
while True:          # PARA REPETIR PARA SEMPRE
    print( cont, ' -> ', end='')
    cont += 1
print('acabou')
'''

n = s = 0
while True:
    n = int(input('digite um número: '))
    if n == 999:
        break
    s += n
print(f'a soma vale {s}')



