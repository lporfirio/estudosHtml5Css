# escreva um programa que leia um valor em metros e o exiba convertido em centimetro e milimetros:

metros = float(input('digite quantos metros: '))
centimetro = metros * 100
milimetro = metros * 1000
print('{} metros é igual a {} centímetros que é igual a {} milímetros'.format(metros, centimetro, milimetro))