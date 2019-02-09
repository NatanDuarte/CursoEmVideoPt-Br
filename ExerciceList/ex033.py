"""Exercício Python 033: Faça um programa que leia três
números e mostre qual é o maior e qual é o menor."""


n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
# Maior
if n1 > n2 and n1 > n3:
    maior = n1
elif n2 > n1 and n2 > n3:
    maior = n2
else:
    maior = n3
# Menor
if n1 < n2 and n1 < n3:
    menor = n1
elif n2 < n1 and n2 < n3:
    menor = n2
else:
    menor = n3
print('___' * 8)
print('Dos números que você digitou\n'
      '{} é o maior e {} é o menor'.format(maior, menor))
