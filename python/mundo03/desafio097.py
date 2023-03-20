'''
Exercício Python 097: Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.                                  Ex:                                                                                                                                                                        
escreva('Olá, Mundo!') Saída:                                                                                                       ~~~~~~~~~~
Olá, Mundo
~~~~~~~~~~
'''

def escreva(texto):
    finalText = f'  {texto}  '
    carac = len(finalText)
    print('~'*carac)
    print(finalText)
    print('~'*carac)


t = str(input('Texto: '))

escreva(t)

