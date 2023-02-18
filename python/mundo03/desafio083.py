'''
crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.



*tentar usar a quantidade de parêntese... se for ímpar a expressão está errada



SOLUÇÃO DO LUQUINHA:
expressao = str(input('Digite uma expressão para ver se ela está correta: '))

abrir = []
fechar = []
for chave, valor in enumerate(expressao):
    if valor == '(':
        abrir.append(chave)
    elif valor == ')':
        fechar.append(chave)

#print(abrir, fechar)

chavesOk = []
if len(abrir) == len(fechar):
    for chave, valor in enumerate(abrir):
        if valor < fechar[chave]:
            chavesOk.append(chave)
            #print(chavesOk)
    if len(chavesOk) == len(abrir):
        print('A expressão está correta')
    else:
        print('A expressão está incorreta')
else:
    print('Desculpe, a expressão está incorreta.')
'''

expressao = str(input('Digite uma expressão para ver se ela está correta: '))
pilha = []

for v in expressao:
    if v == '(':
        pilha.append('(')
    if v == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if pilha == 0:
    print('A expressão está correta')
else:
    print('A expressão está incorreta')
