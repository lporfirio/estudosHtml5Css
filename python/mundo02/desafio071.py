'''
crie um progrma aque simule o funcionamento de um CAIXA ELETRÔNICO. No início, pergunte ao usuário qual será o VALOR A SER SACADO(número inteiro) e o programa vai informar quantas CÉDULAS de cada valor serão entregues.

obs: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1





SOLUÇÃO DO LUQUINHA

valor = int(input('quanto você deseja sacar? '))
notas50 = notas20 = notas10 = notas1 = 0
while True:
    if valor >= 50:
        notas50 += 1
        valor = valor - 50
    else:
        if valor >= 20:
            notas20 += 1
            valor = valor - 20
        else:
            if valor >= 10:
                notas10 += 1
                valor = valor - 10
            else:
                if valor >= 1:
                    notas1 += 1
                    valor = valor - 1
                else:
                    break
if notas50 > 0:
    print(f'{notas50} notas de R$50.')
if notas20 > 0:
    print(f'{notas20} notas de R$20.')
if notas10 > 0:
    print(f'{notas10} notas de R$10.')
if notas1 > 0:
    print(f'{notas1} notas de R$1.')
'''


valor = int(input('Que valor você quer sacar? R$'))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'total de {totced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print('encerrado')
