"""Exercício Python 071: Crie um programa que simule o funcionamento de
um caixa eletrônico. No início, pergunte ao usuário qual será o valor a
ser sacado (número inteiro) e o programa vai informar quantas cédulas de
cada valor serão entregues.
OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1."""

from time import sleep

print('\033[1;34m=' * 30)
print('{:^30}'.format('G U A N A B A N C O'))

real = float(100)
cedula = int(0)

total = int(input('Quantos reais deseja sacar? R$'))

while True:
    if total >= real:
        total -= real
        cedula += 1
    else:
        if cedula > 0:
            sleep(0.7)
            print(f'{cedula:3} notas de R$ {real:3.2f}')

        if real == 100:
            real = 50
        elif real == 50:
            real = 20
        elif real == 20:
            real = 10
        elif real == 10:
            real = 5
        elif real == 5:
            real = 2
        elif real == 2:
            real = 1

        cedula = 0

        if total == 0:
            break
