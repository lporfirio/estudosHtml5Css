'''
Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício indo de 10 até 0, com uma pausa de 1 segundo entre elas.
'''


import time

for c in range(10, -1, -1):
    time.sleep(1)
    print(c)
print('\033[31mBOOOM!!!!!\033[m \033[33m**** FOGOS EXPLODINDO ****\033[m \033[31m!!!!!!!!!\033[m')