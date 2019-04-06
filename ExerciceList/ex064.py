"""Exercício Python 064: Crie um programa que leia vários números inteiros pelo
teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a
condição de parada. No final, mostre quantos números foram digitados e qual foi
a soma entre eles (desconsiderando o flag)."""

cont = add = user = int(0)

while user != 999:
    user = int(input('''\n\033[1;34m    Enter a number:
    [999 = End program]
    >>> '''))

    if user != 999:
        cont += 1
        add += user

print(f'''\n    Digitized numbers: {cont}
    The sum of all numbers: {add}''')
