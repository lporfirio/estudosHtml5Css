''''
crie um programa que tenha uma tupla com várias palavras(não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as vogais.

'''


palavras = ('caneta', 'teclado', 'mouse', 'celular', 'mesa', 'guitarra')
for p in palavras:
    print(f'Na palavra {p.upper()} temos', end='')
    print(' ', end='')
    for letra in p:
        if letra in 'aeiou':
            print(f'{letra} ', end='')
    print('')