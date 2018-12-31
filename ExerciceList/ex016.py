# Crie um programa que leia um número Real
# qualquer pelo teclado e mostre na tela a sua porção Inteira.

""" import math  # Usando import
    x = float(input('digite um número real: '))
    print('a porção inteira de {} é {}'.format(x, math.trunc(x))) """

x = float(input('Digite um número real: '))  # sem importar nada
print('o número {} tem parte absoluta {}'.format(x, int(x)))
