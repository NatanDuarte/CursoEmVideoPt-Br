"""Exercício Python 058: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar"
em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar,
mostrando no final quantos palpites foram necessários para vencer."""

from random import randint

erro = int(0)
a = randint(1, 10)

print('\033[1;34m     JOGO DA ADIVINHAÇÃO')
x = int(input('''Pensei num número entre 1 e 10
    Qual é o número?\n>> '''))


while x != a:

    erro += 1

    if a > x:
        print('Mais...')
    elif a < x:
        print('Menos...')

    x = int(input('''
    Tente novamente
    >>> '''))

print(f'\n\033[1;32mVOCÊ ACERTOU!\n errou {erro} vezes \nPensei no número {x}')
