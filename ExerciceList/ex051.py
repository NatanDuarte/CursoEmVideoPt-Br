"""Exercício Python 051: Desenvolva um programa que leia o primeiro termo e
a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão."""

print('     \033[1;34mProgressão Aritmética')

termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))

print('\nOs dez primeiros termos desta PA são:')

for c in range(1, 10 + 1):
    print(f'{termo:2}', end=' ')
    termo += razao
    c += 1
