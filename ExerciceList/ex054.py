"""Exercício Python 054: Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores."""

from datetime import date

maioridade: int = (0)

for c in range(1, 8):

    pessoa = int(input(f'{c} - Digite a data do seu nascimento: '))

    if pessoa <= date.today().year - 18:

        maioridade += 1

print(f'''Das sete pessoas, {maioridade} são maiores perante a lei.''')
