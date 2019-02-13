"""Exercício Python 035: Desenvolva um programa que leia o comprimento
de três retas e diga ao usuário se elas podem ou não formar um triângulo."""

print('Analise de triângulos')
print('______' * 10)
lado1 = float(input('Digite o comprimento do 1° segmento: '))
lado2 = float(input('Digite o comprimento do 2° segmento: '))
lado3 = float(input('Digite o comprimento do 3° segmento: '))
print('======' * 10)
if lado1 < lado2 + lado3 and lado2 < lado3 + lado1 and lado3 < lado1 + lado2:
    print('Estes segmentos formam um triângulo!')
else:
    print('\033[31;1mNão é possível formar um triângulo com estes segmentos.\033[m')
