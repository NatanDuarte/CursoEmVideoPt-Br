"""Exercício Python 025: Crie um programa que leia o
nome de uma pessoa e diga se ela tem "SILVA" no nome."""

nome = str(input('Insira seu nome: ').strip())
if True == 'SILVA' in nome.upper():
    print('Você possue Silva no nome!')
else:
    print('Você NÃO possue Silva no nome...')
