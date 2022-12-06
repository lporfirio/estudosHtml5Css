# crie um algorítimo que leia um número e mostre seu dobro, triplo e raiz quadrada

n = int(input('digite um número: '))
dobro = n * 2
triplo = n * 3
raiz = n ** (1/2)
print('o dobro é {}, o triplo é {} e a raiz quadrada é {:.2f}'.format(dobro, triplo, raiz))
print('o dobro é {}, o triplo é {} e a raiz quadrada é {:.2f}'.format((n*2), (n*3), pow(n, (1/2))))