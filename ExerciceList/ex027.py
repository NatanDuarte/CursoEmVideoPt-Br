"""Exercício Python 027: Faça um programa que leia o nome completo de uma
pessoa, mostrando em seguida o primeiro e o último nome separadamente."""

nome = str(input('Digite seu nome completo: ').strip()).split()
print('Primeiro nome: {}'.format(nome[0]))
print('Ultimo nome: {}'.format(nome[len(nome)-1]))
