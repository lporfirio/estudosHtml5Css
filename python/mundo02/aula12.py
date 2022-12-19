# if, elif, else

nome = str(input('qual é seu nome? '))
if nome == 'Lucas':
    print('que nome bonito!!!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Cláudia Jéssica':
    print('Belo nome feminino.')
else:
    print('seu nome é bem normal')
print('tenha um bom dia, {}'.format(nome))