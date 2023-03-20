def aumentar(n=0, por=0):
    res = n+(n * (por / 100))
    return res


def diminuir(n=0, por=0):
    res = n-(n * (por / 100))
    return res


def dobro(n=0):
    res = n*2
    return res


def metade(n=0):
    res = n/2
    return res


def moeda(preco = 0, moeda = 'R$'):
    texto = f'{moeda}{preco:.2f}'.replace('.',',')
    return texto
