
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





