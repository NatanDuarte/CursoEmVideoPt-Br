"""Exercício Python 050: Desenvolva um programa que leia seis números inteiros e mostre
a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o. """

par = int(0)
inpar = int(0)

for c in range(1, 7):
    num = int(input('Digite o {}° número: '.format(c)))
    if num % 2 == 0:
        par += num
    else:
        inpar += num

print("""\n    A soma dos números pares foi {}
    A soma dos números ímpares foi {}""".format(par, inpar))
