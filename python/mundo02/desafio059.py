'''
Crie um programa que leia dois valores e mostre um menu na tela:

[1]somar
[2]multiplicar
[3]maior
[4]novos números
[5]sair do programa

seu programa deverá realizar a operação solicitada em cada caso.
'''

'''
opcao = 4
while opcao != 5:
    print('-=-=-ANALISADOR DE VALORES-=-=-')
    valor1 = int(input('1° valor: '))
    valor2 = int(input('2° valor: '))
    print('Para: \n[1]somar\n[2]multiplicar\n[3]maior\n[4]novos números\n[5]sair do programa\n')
    opcao = int(input('Digite a opção desejada: \n'))
    if opcao == 1:
        print(f'[1] função somar é igual a: {valor1 + valor2}\n\n')
    elif opcao == 2:
        print(f'[2] função multiplicar é igual a: {valor1 * valor2}\n\n')
    elif opcao == 3:
        if valor1 > valor2:
            print(f'[3] função maior: o maior valor é {valor1}\n\n')
        elif valor2 > valor1:
            print(f'[3] função maior: o maior valor é {valor2}\n\n')
        else:
            print(f'[3] função maior: os 2 valores são iguais.\n\n')
    elif opcao == 4:
        print('[4] digite novos números:')
print('[5] você saiu do programa.')
'''
from time import sleep


n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
while opcao !=5:

    print('''[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa ''')
    opcao = int(input(' >>>>>>>>>>>>> Qual é a sua opção? '))
    if opcao == 1:
        print(f'[1] função somar é igual a: {n1 + n2}')
    elif opcao == 2:
        print(f'[2] função multiplicar é igual a: {n1 * n2}')
    elif opcao == 3:
        if n1 > n2:
            print(f'[3] função maior: o maior valor é {n1}')
        elif n2 > n1:
            print(f'[3] função maior: o maior valor é {n2}')
        else:
            print(f'[3] função maior: os 2 valores são iguais.')
    elif opcao == 4:
        print('Informe novos números: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('finalizando...')
    else:
        print('opção inválida, tente novamente.')
    print('-=-=' * 10)
    sleep(1.4)
print('fim do programa...volte sempre')