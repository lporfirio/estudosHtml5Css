# escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por km rodado.

km = int(input('quantos Km rodados? '))
dias = int(input('por quantos dias o carro foi alugado? '))

preco = dias * 60 + km * 0.15

print('o total a pagar é de R${}'.format(preco))