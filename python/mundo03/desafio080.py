'''
crie um programa onde o usuário possa digitar cinco NÚMEROS e cadastre-os em uma lista, já na posição correta de inserção(sem usar o sort())
no final, mostre a lista ordenada na tela 


solução do LUQUINHA:
lista = []

for n in range(0,5):
    valor = int(input('digite um número: '))
    lista.append(valor)
print(lista)

maior = max(lista)
menor = min(lista)

lista.remove(maior)
lista.remove(menor)

segundoMaior = max(lista)
segundoMenor = min(lista)

lista.remove(segundoMaior)
lista.remove(segundoMenor)

lista.insert(0, menor)
lista.insert(1, segundoMenor)
lista.insert(3, segundoMaior)
lista.insert(4, maior)

print(lista)
'''

lista = []
for c in range(0,5):
    n = int(input('digite um número: '))
    # para colocar no final (maior número)
    if c == 0 or n > lista[-1]: ### lista[-1] o último elemento da lista 
        lista.append(n)
        (print('adicionado ao final da lista...'))
    else:
    # para colocar na posição específica
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'adicionado na posição {pos}')
                break
            pos += 1

print(lista)


