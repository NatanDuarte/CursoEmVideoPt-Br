"""Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha."""

m = [[], [], []]
par = terc = maior = 0

for l in range(0, 3):
    for c in range(0, 3):
        m[l].append(int(input(f'Digite {l, c}: ')))

        if m[l][c] % 2 == 0:
            par += m[l][c]

        if c == 2:
            terc += m[l][c]

        if m[l][c] > maior:
            maior = m[l][c]

print()

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{m[l][c]:^5}]', end='')
    print()

print(f'''
A soma de todos os valores pares digitados: {par}
A soma dos valores da terceira coluna: {terc}
O maior valor da segunda linha: {maior}''')
