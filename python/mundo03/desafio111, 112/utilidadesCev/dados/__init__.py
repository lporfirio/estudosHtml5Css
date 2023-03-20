def leiadinheiro(text):
    while True:
        p = input(text).replace(',', '.')
        try:
            f = float(p)
            return f
        except ValueError:
            print(f'\033[31m[ERRO] "{p}" é um valor inválido. Tente novamente.\033[m')

