"""Exercício Python 062: Melhore o DESAFIO 061, perguntando para
o usuário se ele quer mostrar mais alguns termos. O programa
encerrará quando ele disser que quer mostrar 0 termos."""

from time import sleep

total = int(0)
c = int(0)
extra = int(10)

print('     \033[1;34mProgressão Aritmética')

termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))

print('\nOs dez primeiros termos desta PA são:')

while extra != 0:

    total += extra

    while c <= total:
        print(f'{termo:3}', end=' ')
        termo += razao
        c += 1

        sleep(0.8)
    extra = int(input('''\nQuantos termos voce que ver a mais?
[ZERO para encerrar]
>>> '''))

print('Fim Do programa')
