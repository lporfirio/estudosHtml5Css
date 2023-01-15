'''crie um programa que faça o computador jogar JOKEMPÔ com você

pedra > tesoura > papel > pedra


\033[style;text;back m
'''
import random
import time
computador = random.choice(['pedra', 'tesoura', 'papel'])

# print(computador)

print('Vamos jogar \033[32mJOKEMPÔ\033[m!!!')
user = str(input('Digite pedra, papel ou tesoura: '))

time.sleep(1)
print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PÔ')

if user == computador:
    print('\033[30mempatou!\033[m')
elif user == 'pedra':
    if computador == 'papel':
        print('\033[31mputz! você perdeu! O computador jogou papel!\033[m')
    else:
        print('\033[32mHA! o computador jogou tesoura.. você venceu!!!\033[m')

elif user == 'papel':
    if computador == 'tesoura':
        print('\033[31mputz! você perdeu! O computador jogou tesoura!\033[m')
    else:
        print('\033[32mHA! o computador jogou pedra.. você venceu!!!\033[m')

elif user == 'tesoura':
    if computador == 'pedra':
        print('\033[31mputz! você perdeu! O computador jogou pedra!\033[m')
    else:
        print('\033[32mHA! o computador jogou papel.. você venceu!!!\033[m')
else:
    print('\033[33mTalvez você tenha jogado errado, tente novamente\033[m')
