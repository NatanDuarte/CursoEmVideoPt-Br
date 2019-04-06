"""Exercício Python 066: Crie um programa que leia números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de
parada. No final, mostre quantos números foram digitados e qual foi a soma entre
elas (desconsiderando o flag)."""

c = number = s = int(0)

while True:  # loop
    number = int(input('  Enter a number\n(999 == Finalize): '))
    if number == 999:  # flag
        break
    c += 1  # contage
    s += number  # sum of all numbers
print(f'{c} numbers were entered\nThe sum of all numbers is {s}')
