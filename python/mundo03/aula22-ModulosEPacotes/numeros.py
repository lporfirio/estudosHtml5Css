from uteis import numeros

num = int(input('Digite um valor: '))
fat = numeros.fatorial(num)
print(f'o fatorial de {num} é {fat}')
print(f'o dobro de {num} é {numeros.dobro(num)}')


# DENTRO DO PYTHON, TODAS AS PASTAS SÃO CONSIDERADAS PACOTES
# -pacotes são para projetos muito grandes
# -dentro das pastas sempre temos que ter o arquivo __init__.py