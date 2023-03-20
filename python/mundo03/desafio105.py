'''
Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:

- quantidade de notas
- a maior nota
- a menor nota
- a média da turma
- a situação(opcional)
'''

def notas(*n, sit = False):
    '''
    essa função é para analisar as notas de vários alunos:
    -> pode colocar várias notas como parâmetro.
    -> sit é opcional.
    -> retorna um dicionário com várias informações.
    '''
    maior = menor = media = 0
    resposta = {}
    for i, v in enumerate(n):
        if i == 0:
            maior = v
            menor = v
        else:
            if v > maior:
                maior = v
            if v < menor:
                menor = v
    
    media = sum(n) / len(n)
    if media < 5:
        situacao = 'RUIM'
    elif media < 7:
        situacao = 'REGULAR'
    else:
        situacao = 'BOA' 

    resposta['total'] = len(n)
    resposta['maior'] = maior
    #resposta['maior'] = max(n) #para saber o maior 
    resposta['menor'] = menor 
    #resposta['menor'] = min(n) #para saber o menor
    resposta['media'] = media
    if sit == True:
        resposta['situação'] = situacao

    return resposta

resp = notas(3.5, 5.5, 3, 7, sit=True)
print(resp)
help(notas)