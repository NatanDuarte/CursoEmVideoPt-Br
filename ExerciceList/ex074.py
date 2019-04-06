"""Exercício Python 074: Crie um programa que vai gerar cinco números
aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de
números gerados e também indique o menor e o maior valor que estão na
tupla."""

from random import randint

x = (randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9))

print('Os números sorteados foram: ', end='')
for c in x:
    print(f'{c}', end=' ')
print(f'\nO maior número é {max(x)}')
print(f'O menor número é {min(x)}')
