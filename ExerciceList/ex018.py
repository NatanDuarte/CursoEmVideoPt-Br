"""  Exercício Python 018: Faça um programa que leia um ângulo qualquer
     e mostre na tela o valor do seno, cosseno e tangente desse ângulo.  """

from math import sin
from math import cos
from math import tan

x = int(input('Digte um ângulo: '))
print('o seno de {} é {:.3f}'.format(x, sin(x)))
print('O cosseno de {} é {:.3f}'.format(x, cos(x)))
print('A tangente de {} e {:.3f}'.format(x, tan(x)))
