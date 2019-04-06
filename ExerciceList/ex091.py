"""Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado
e tenham resultados aleatórios. Guarde esses resultados em um dicionário
em Python. No final, coloque esse dicionário em ordem, sabendo que o
vencedor tirou o maior número no dado."""

from random import randint
from time import sleep
from operator import itemgetter

players = dict()
ranking = list()

for c in range(0, 4):
    players[f'player {c+1}'] = randint(1, 6)

for k, v in players.items():
    sleep(0.695)
    print(f'{k:<8} rolou {v:^3}')

ranking = sorted(players.items(), key=itemgetter(1), reverse=True)

print('Ranking')

for i, v in enumerate(ranking):
    print(f'|{i+1}° lugar: {v[0]} com {v[1]}|')
