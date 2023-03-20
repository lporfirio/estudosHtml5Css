'''
Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.



def fatorial(num, show=False):
    print('-'*35)
    f = 1
    if show == True:
        for c in range(num, 0, -1):
            f = f*c
            print(f'{c} ', end='')
            if c > 1:
                print('x ', end='')
            if c == 1:
                return (f'= {f}')
    if show == False:
        for c in range(num, 0, -1):
            f = f*c
    return f
'''


def fatorial(num, show=False):
    '''
    --> Calcula o Fatorial de um número.
    '''
    print('-'*35)
    f = 1
    for c in range(num, 0, -1):
        f = f*c
        if show == True:
            print(f'{c} ', end='')
            if c > 1:
                print('x ', end='')
            if c == 1:
                print(f'= ', end='')
    return f


print(fatorial(4))
print(fatorial(6, True))


help(fatorial)