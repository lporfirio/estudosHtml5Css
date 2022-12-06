# faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor

n = int(input('digite um número: '))

sucessor = n + 1
antecessor = n - 1
print('o número é {}, seu sucessor é {} e seu antecessor é {}'.format(n, sucessor, antecessor))
print('o número é {}, seu sucessor é {} e seu antecessor é {}'.format(n, (n+1), (n-1)))