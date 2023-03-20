'''
Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.
'''
from moeda import moeda, metade, aumentar, dobro, diminuir


preco = (int(input('Digite o preço: R$')))
porcentagem = 10

print(f'A metade de {moeda(preco)} é {metade(preco, True)}')
print(f'O dobro de {moeda(preco)} é {dobro(preco, True)}')
print(f'Aumentando {porcentagem}%, temos {aumentar(preco, porcentagem, True)}')
print(f'Diminuindo {porcentagem}%, temos {diminuir(preco, porcentagem, True)}')




