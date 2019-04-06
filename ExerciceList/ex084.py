"""Exercício Python 084: Faça um programa que leia nome e peso de
várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves."""

leitura = []
principal = []

heavy = lighter = 0

while True:
    leitura.append(str(input('Digite seu nome: ')))
    leitura.append(float(input('Digite seu peso: ')))

    if len(principal) == 0:
        heavy = lighter = leitura[1]
    else:
        if leitura[1] > heavy:
            heavy = leitura[1]
        elif leitura[1] < lighter:
            lighter = leitura[1]

    principal.append(leitura[:])
    leitura.clear()

    OneMore = str(input('Continuar [S/N] ? ').strip())
    if OneMore.upper() == 'N':
        break

print(f'''\nTotal de cadastros: {len(leitura)}''')
print(f'O maior pesado: {heavy} -- ', end='')
for c in principal:
    if c[1] == heavy:
        print(f'[{c[0]}] ', end='')

print(f'\nO mais leve: {lighter} -- ', end='')
for c in principal:
    if c[1] == lighter:
        print(f'[{c[0]}] ', end='')
