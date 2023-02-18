'''
pessoas = [['pedro', 25],['maria', 19], ['joao', 32]]

print(pessoas[0][0])
print(pessoas[1][1])
print(pessoas[2][0])
print(pessoas[1])



teste = list()
teste.append('Gustavo')
teste.append(40)
galera = []
galera.append(teste[:]) # utilizando o [:] se gera uma cópia e não uma ligação

teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)

#
galera = [['joão', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera[2][1])
for p in galera:
    print(p[0])
#
'''

galera = []
dado = []
totmai = totmen = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
print(galera)

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} tem mais de 21 anos')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade')
        totmen += 1

print(f'temos {totmai} maiores e {totmen} menores de idade')

