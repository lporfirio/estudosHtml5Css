def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')


soma(b=4, a=5)

#empacotando parâmetros
def contador(*num):
    for valor in num:
        print(valor, end=' ')
    print('fim')

contador(2,1,7)
contador(8,0)
contador(4,4,7,6,2)

#listas
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1

valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)