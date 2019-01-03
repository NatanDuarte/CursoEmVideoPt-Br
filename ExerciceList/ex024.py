"""Exercício Python 024: Crie um programa que leia o
nome de uma cidade diga se ela começa ou não com o nome "SANTO"."""

city = str(input('Digite o nome de uma cidade: ').strip()).split()
if city[0].upper() == 'SANTO':
    print('O nome desta cidade começa com SANTO')
else:
    print('O nome desta cidade NÃO começa com SANTO')
