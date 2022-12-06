# escreva um programa que converta uma temperatura digitada em °C e converta para °F


c = float(input('digite a temperatura em graus °C: '))

f = (c * (9/5))+32
print('{}°C equivalem a {}°F'.format(c, f))