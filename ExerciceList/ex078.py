"""Exercício Python 078: Faça um programa que leia 5 valores numéricos
e guarde-os em uma lista. No final, mostre qual foi o maior e o menor
valor digitado e as suas respectivas posições na lista."""

# bigger = int(0)  # variaveis do jeito mais trabalhoso
# smaller = int(10000)
# posB = posM = 0

numbers = list()

for n in range(0, 5):  # declarando variaveis com o laço
    numbers.append(int(input('Digite um valor: ')))

print(f'''
O maior valor da lista: {max(numbers)} na posição {numbers.index(max(numbers))}
O menor valor da lista: {min(numbers)} ma posição {numbers.index(min(numbers))}''')


# OUTRO JEITO (MAIS TRABALHOSO)
#
# for m in numbers:
#     if m > bigger:
#         bigger = m
#         posB = numbers.index(m)
#
#     if m < smaller:
#         smaller = m
#         posM = numbers.index(m)
#
# print(f'''
# O maior valor da lista: {bigger} na posicao {posB}
# O menor valor da lista: {smaller} na posicao {posM}''')
