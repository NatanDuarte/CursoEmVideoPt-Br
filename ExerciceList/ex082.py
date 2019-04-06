"""Exercício Python 082: Crie um programa que vai ler vários números e colocar
em uma lista. Depois disso, crie duas listas extras que vão conter apenas os
valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre
o conteúdo das três listas geradas."""

a = []  # original

for c in range(5):
    a.append(int(input('Digite um número: ')))

p = []  # par
i = []  # ímpar

for d in a:
    if d % 2 == 0:
        p.append(d)
    else:
        i.append(d)

print(f'\nLista Completa: {a} \nPares: {p} \nImpares: {i}')
