"""
Exercício Python 046: Faça um programa que mostre na tela uma contagem
regressiva para o estouro de fogos de artifício, indo de 10 até 0, com
uma pausa de 1 segundo entre eles. """

import emoji
from time import sleep

for c in range(10, 0, -1):
    print(' \033[1;34m{}!'.format(c))
    sleep(1)
print(emoji.emojize(' \033[1;33mFELIZ ANO NOVO! :fireworks:'))
