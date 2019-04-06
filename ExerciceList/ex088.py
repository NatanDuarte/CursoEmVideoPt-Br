"""Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA
a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai
sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma
lista composta."""

from random import sample
from time import sleep

mega = []

game = int(input('\033[1;34mQuantos jogos você deseja gerar? '))

for c in range(0, game):
    mega.append(sorted(sample(range(60), 6)))

for c in range(0, game):
    sleep(0.679)
    print(f'\n{c + 1}° - ', end='')

    for d in range(0, 6):
        print(f'|{mega[c][d]:^5}|', end='')

    print()

sleep(0.345)
print('\nBoa Sorte!')
