'''
if carro.esquerda():
    bloco True
else:
    bloco False

tempo=int(input('quantos anos tem seu carro?'))
print('carro novo' if tempo<=3 else 'carro velho')



'''

'''nome=str(input('qual é seu nome? '))
if nome == 'Lucas':
    print('Belo nome!!!')
else:
    print('Seu nome é tão normal')
print('Bom dia, {}!'.format(nome))'''

n1 = float(input('digite a primeira nota: '))
n2 = float(input('digite a segunda nota: '))
m = (n1+n2)/2
print('a sua media foi {:.1f}'.format(m))
if m >= 6.0:
    print('sua media foi boa! PARABÉNS!')
else:
    print('sua média foi ruim! Estude mais!!!')
# print('PARABÉNS' if m >=6.0 else 'ESTUDE MAIS')