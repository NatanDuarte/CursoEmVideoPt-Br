"""Exercício Python 030: Crie um programa que leia um 
número inteiro e mostre na tela se ele é PAR ou ÍMPAR."""

num = int(input('Digite um número: '))
if num % 2 == 0:
    print('O numero {} é PAR.'.format(num))
else:
    print('O número {} é ÍMPAR.'.format(num))
