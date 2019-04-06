"""Exercício Python 086: Crie um programa que declare uma matriz de dimensão
3x3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na
tela, com a formatação correta."""

m = [[], [], []]

for c in range(0, 3):
    for d in range(0, 3):
        m[c].append(int(input(f'Digite {c, d}: ')))

print()

for c in range(0, 3):
    for d in range(0, 3):
        if d < 2:
            print(f'[{m[c][d]:^5}]', end='')
        else:
            print(f'[{m[c][d]:^5}]')
