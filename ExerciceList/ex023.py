"""Exercício Python 023: Faça um programa que leia um número
de 0 a 9999 e mostre na tela cada um dos dígitos separados."""

num = int(input('Digite um número entre 0 e 9999: '))
m = num // 1000 % 10
c = num // 100 % 10
d = num // 10 % 10
u = num // 1 % 10
print('Analizando {}:'.format(num))
print('Milhar  | {} |'.format(m))
print('centena | {} |'.format(c))
print('dezena  | {} |'.format(d))
print('unidade | {} |'.format(u))
