"""Exercício Python 055: Faça um programa que leia o peso de cinco
pessoas. No final, mostre qual foi o maior e o menor peso lidos."""

maior = int(0)
menor = int(5000)
for c in range(1, 6):

    peso = int(input(f'Pessoa {c}) Digite seu peso: '))

    if peso > maior:

        maior = peso

    if peso <= menor:

        menor = peso

print(f'Das cinco pessoas a mais leve pesa {menor} kg e a maior {maior} kg')
