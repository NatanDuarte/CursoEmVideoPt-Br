"""
Exercício Python 042: Refaça o DESAFIO 035 dos triângulos,
acrescentando o recurso de mostrar que tipo de triângulo será formado:
- EQUILÁTERO: todos os lados iguais
- ISÓSCELES: dois lados iguais, um diferente
- ESCALENO: todos os lados diferentes
"""

print('\033[1;34m====' * 8)
print('     Análise de triângulos')
print('====' * 8)
print(' Por favor, digite o comprimento dos segmentos:')
a = int(input(' 1°: '))
b = int(input(' 2°: '))
c = int(input(' 3°: '))
if a < b + c and b < a + c and c < b + a:
    if a == b and b == c:
        print(' Os três segmentos formam um TRIÂNGULO EQUILATERO\n'
              ' Um triângulo com tres lados iguais')
    elif a != b and b != c:
        print(' Os três segmentos formam um TRIÂNGULO ESCALENO\n'
              ' Um triangulo com três lados diferentes')
    elif a == b or a == c or b == c:
        print(' Os três segmentos formam um TRIÂNGULO ISÓCELES\n'
              ' um triangulo com dois lados iguais e um diferente')
else:
    print(' \033[1;31mOs três segmentos NÃO formam um triângulo.\033[m')
