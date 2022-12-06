# crie um progrma que leia o nome de uma cidade e diga se ela começa ou não com a palavra "SANTO"

cidade = str(input('qual cidade você nasceu?: ')).strip()
cidade2 = cidade.lower()
print('santo' in cidade2)
print(cidade2[:5] == 'santo')