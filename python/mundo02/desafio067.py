'''
Faça um progrmaa que mostre a TABUADA de VÁRIOS NÚMEROS, um de cada vez, para cada valor digitado pelo usuário. O programa será INTERROMPIDO quando o número solicitado for NEGATIVO.
'''

while True:
    n = int(input('quer ver a tabuada de qual valor? '))
    if n < 0:
        break
    c = 1
    while c <= 10:
        print(f'{n} x {c:2} = {n*c}')
        c += 1
print('Programa Encerrado')   
        