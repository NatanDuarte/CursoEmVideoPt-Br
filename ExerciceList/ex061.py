"""Exercício Python 061: Refaça o DESAFIO 051, lendo o primeiro termo e a razão
de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while."""

from time import sleep

c = int(0)

print('     \033[1;34mProgressão Aritmética')

termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))

print('\nOs dez primeiros termos desta PA são:')

while c < 10:
    print(f'{termo:3}', end=' ')
    termo += razao
    c += 1

    sleep(0.8)
