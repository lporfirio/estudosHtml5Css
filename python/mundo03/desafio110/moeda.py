
def moeda(preco = 0, moeda = 'R$'):
    texto = f'{moeda}{preco:.2f}'.replace('.',',')
    return texto


def aumentar(n=0, por=0, form=False):
    res = n+(n * (por / 100))
    return res if form is False else moeda(res)


def diminuir(n=0, por=0, form=False):
    res = n-(n * (por / 100))
    return res if form is False else moeda(res)


def dobro(n=0, form=False):
    res = n*2
    return res if form is False else moeda(res)


def metade(n=0, form=False):
    res = n/2
    return res if not form else moeda(res)

def resumo(p=0,aum=10,red=5):
    print('-'*32)
    print('RESUMO DO VALOR'.center(32))
    print('-'*32)
    print(f'Preço analisado: \t{moeda(p)}')
    print(f'Dobro do preço: \t{dobro(p, True)}')
    print(f'Metade do preço: \t{metade(p, True)}')
    print(f'{aum}% de aumento: \t{aumentar(p, aum, True)}')
    print(f'{red}% de redução: \t{aumentar(p, red, True)}')
    print('-'*32)



