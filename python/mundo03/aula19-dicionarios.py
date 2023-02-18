'''pessoas = {'nome': 'gustavo', 'sexo': 'M', 'idade': 22}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
pessoas['nome'] = 'Leandro'
pessoas['peso'] = 67
del pessoas['sexo']
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())

for k, v in pessoas.items():
    print(k)
    print(v)

#dicionário dentro de uma lista:
brasil = []
estado1 ={'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}

brasil.append(estado1)
brasil.append(estado2)

print(brasil[0]['uf'])
    
'''

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for k, v in e.itens():
        print(f'o campo {k} tem valor {v}.')