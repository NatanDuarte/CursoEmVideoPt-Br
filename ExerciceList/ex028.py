"""Exercício Python 028: Escreva um programa que faça o computador
"pensar" em um número inteiro entre 0 e 5 e peça para o usuário
tentar descobrir qual foi o número escolhido pelo computador. O
programa deverá escrever na tela se o usuário venceu ou perdeu."""

from random import randint  # sorteia números inteiros dentro de um intervalo
from time import sleep  # faz uma pausa para criar a sensação de programa carregando


print('-=' * 20)
print('Pensei em um número entre 0 e 5')
x = int(input('Consegue advinhar? '))
print('-=' * 20)
print('Processando...')
sleep(3)
ale = randint(0, 5)
if ale == x:
    print('Parabéns, você acertou, pensei no número {}'.format(ale))
else:
    print('Você errou... Eu pensei no número {}'.format(ale))
