"""Exercício Python 067: Faça um programa que mostre a tabuada de vários
números, um de cada vez, para cada valor digitado pelo usuário. O programa
será interrompido quando o número solicitado for negativo. """

from time import sleep

t = c = int(0)
tittle = str('tabuada').upper()

print('\033[1;34m')  # color

print(f'\t{tittle:^21}')  # tittle

while True:  # loop

    t = int(input('''
   Enter a number to see tabuada:
(enter a negative number to stop)
>>> '''))

    if t < 0:  # flag
        break

    for c in range(0, 10+1):  # tabuada
        print(f'{c:2} x {t} = {c * t:}')
        sleep(0.6)

print('\n      finished'.upper())
