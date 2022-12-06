# faça um algoritimo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto


preco = float(input('qual o preço do produto? '))


print('com desconto de 5%, ficará {:.2f}'.format(preco-(preco*0.05)))