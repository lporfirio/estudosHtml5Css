# crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar // considere US$1,00 = R$3,27

dinheiro = float(input('quanto dinheiro você tem? '))

dolar = dinheiro / 3.27

print('com R$ {}, você pode comprar US$ {:.2f}'.format(dinheiro, dolar))