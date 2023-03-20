'''
- interactive help
- docstrings
- argumentos opcionais
- escopo de variáveis
- retorno de resultados

'''

'''


def exemplo(i=1, f=2, p=3):
    global a # faz com que a função mude a variável global
    a = 4
    """
    DOCSTRING
    -> funciona como se fosse um manual da função
    """
    print(f'é isso: {i}, {f} e {p}')

a = 2
#exemplo(4, 5, 7)
help(exemplo)

##########
variáveis globais
variáveis locais
exemplo()
print(a)
'''

def fatorial(num = 1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f

n = int(input('Digite um número: '))
print(f'o fatorial de {n} é igual a {fatorial(n)}')


def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False
    
num = int(input('Digite um número para saber se é par ou impar: '))
if par(num):
    print('É par')
else:
    print('É impar')