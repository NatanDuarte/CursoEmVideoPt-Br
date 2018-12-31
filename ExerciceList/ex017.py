""" Faça um programa que leia o comprimento do cateto oposto e do
    cateto adjacente de um triângulo retângulo.
    Calcule e mostre o comprimento da hipotenusa. """

from math import hypot

co = float(input('Insira o tamanho do cateto oposto: '))
ca = float(input('Insira o tamanho do cateto adjacente: '))
print('A hipotenusa vele {:.2f}'.format(hypot(co, ca)))
