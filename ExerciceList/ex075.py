"""Exercício Python 075: Desenvolva um programa que leia quatro
valores pelo teclado e guarde-os em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares."""

nine = int(0)
tres = 0
par = int(0)

a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))
c = int(input('Digite mais um número: '))
d = int(input('Digite o último número: '))

valor = (a, b, c, d)

print('\nOs valores digitados foram: ', end='')
for cont in valor:
    print(f'{cont}', end=' ')
    if cont == 9:
        nine += 1
    elif cont == 3:
        tres = valor.index(3) + 1
    elif cont % 2 == 0:
        par += 1

print(f'''
O número 9 apareceu {nine} vezes,
O 3 apareceu na {tres}ª posição,
{par} valores são pares.''')
