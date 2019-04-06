""" Exercício Python 048: Faça um programa que calcule a soma entre todos os
números que são múltiplos de três e que se encontram no intervalo de 1 até 500. """

total = int(0)
val = int(0)
for c in range(500, 0, -1):
    if c % 3 == 0 and c % 2 == 1:
        total += c
        val += 1
print('''    a soma entre todos os números que são múltiplos de
    três e que se encontram no intervalo de 1 até 500 é {}
    e o total é de {} números.'''.format(total, val))