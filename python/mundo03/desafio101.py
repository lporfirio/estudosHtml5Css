'''
Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

'''



def voto(nasc):
    from datetime import datetime
    anoAtual = datetime.now().year
    idade = anoAtual - nasc
    if idade < 16:
        return f'Com {idade} anos: AINDA NÃO TEM IDADE PARA VOTAR'
    elif 18 >= idade < 65:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'
    else:
        return f'Com {idade} anos: VOTO OPCIONAL'
         


nasc = int(input('Que ano você nasceu? '))
print(voto(nasc))