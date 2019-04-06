"""Exercício Python 060: Faça um programa que
leia um número qualquer e mostre o seu fatorial.
Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120"""

from math import factorial

x = int(input('\033[1;33mDigite um número: '))
cont = int(x - 1)

print(f'{x}! = {x}', end=' ')

while cont >= 1:

    print(f'* {cont}', end=' ')
    cont -= 1

print(f'= {factorial(x)}')
