"""Exercício Python 063: Escreva um programa que leia um número N inteiro qualquer
e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.
Ex: 0 - 1 - 1 - 2 - 3 - 5 - 8"""

from time import sleep

c = int(0)
N = int(0)
first = int(1)
second = int(1)
show = int(0)
more = int(10)

print('     Sequencia Fibonacci')

print(f'0 - {first}', end=' ')
while more != 0:
    N += more

    while c < N - 2:
        show = first + second
        print(f'- {first}', end=' ')
        second = first
        first = show
        c += 1

        sleep(0.6)

    more = int(input('''\n
Quantos elementos da sequencia
Fibonacci voce quer ver a mais?
  [ ZERO == Fim do programa ]
>>> '''))

print('\nFIM DO PROGRAMA')
