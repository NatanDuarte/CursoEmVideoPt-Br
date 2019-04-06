"""Exercício Python 081: Crie um programa que vai ler vários números e colocar
em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista."""

L = list()

for c in range(0, 5):
    L.append(int(input('Digite um número: ')))

print(f'''\n{len(L)} números foram digitados.
A lista ordenada de maneira crescente: {sorted(L)}''')

if 5 in L:
    print(f'5 está na lista.')
else:
    print(f'5 não está na lista.')
