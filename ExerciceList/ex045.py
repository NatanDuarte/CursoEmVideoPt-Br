"""
Exercício Python 045: Crie um programa que faça o
 computador jogar Pedra Papel e Tezoura com você.
"""

from random import randint
from time import sleep

print('\033[1;34m_____' * 9)
print('  GAME:\n     PEDRA, PAPEL E TEZOURA')
player = int(input('  escolha a sua ação:\n'
                   ' 1 -> pedra\n'
                   ' 2 -> papel\n'
                   ' 3 -> tezoura\n'
                   ': '))
bot = randint(1, 3)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')
if player != bot:
    if player == 1 and bot == 3:
        print('[JOGADOR] pedra X tezoura [Bot]\n'
              '     \033[1;33mJOGADOR VENCEU\033[m')
    elif player == 3 and bot == 1:
        print('[JOGADOR] tezoura X pedra [Bot]\n'
              '     \033[1;31mBOT VENCEU\033[m')
    elif player == 2 and bot == 1:
        print('[JOGADOR] papel X pedra [Bot]\n'
              '     \033[1;33mJOGADOR VENCEU\033[m')
    elif player == 1 and bot == 2:
        print('[JOGADOR] pedra X papel [BOT]\n'
              '     \033[1;31mBOT VENCEU\033[m')
    elif player == 3 and bot == 2:
        print('[JOGADOR] tezoura X papel [BOT]\n'
              '     \033[1;33mJOGADOR VENCEU\033[m')
    elif player == 2 and bot == 3:
        print('[JOGADOR] papel X tezoura [BOT]\n'
              '     \033[1;31mBOT VENCEU\033[m')
elif player == bot:
    if player == 1 and bot == 1:
        print('[JOGADOR] pedra X pedra [BOT]\n'
              '     \033[1;31mEMPATE\033[m')
    elif player == 2 and bot == 2:
        print('[JOGADOR] papel X papel [BOT]\n'
              '     \033[1;31mEMPATE\033[m')
    elif player == 3 and bot == 3:
        print('[JOGADOR] tezoura X tezoura [BOT]\n'
              '     \033[1;31mEMPATE\033[m')
print('_____' * 9)
