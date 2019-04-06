"""Exercício Python 052: Faça um programa que leia um
número inteiro e diga se ele é ou não um número primo."""

while True:

    div = int(0)
    c = int(0)

    print('\033[1;34m______' * 4)
    print('  NÚMEROS PRIMOS')
    num = int(input('Digite um número: '))

    while num == 0 or num < 0:
        num = int(input('''Número inváildo
        Digite outro: '''))

    for c in range(1, num + 1):

        if num % c == 0:
            print('\033[33m', end=' ')
            div += 1
        else:
            print('\033[31m', end=' ')

        print(f'{c}', end='')

    if num == 1:
        print(f'\n\033[1;31m{num} NÂO É um número primo!\033[m')
    elif div == 2:
        print(f'\n\033[1;33m{num} É um número primo!\033[m')
    else:
        print(f'\n\033[1;31m{num} NÂO É um número primo!\033[m')

    print('\033[1;34m------' * 4)
    print(' ')
