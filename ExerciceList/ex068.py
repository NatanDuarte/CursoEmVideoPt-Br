"""Exercício Python 068: Faça um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias
consecutivas que ele conquistou no final do jogo."""

from random import randint

victory = int(0)
num = int(1)

print('\033[1;34m         Par ou Ímpar')  # tittle

while True:

    computer = randint(1, 5)  # computer's "choice"
    player = int(input('''
        Sua escolha
    [1] Par
    [2] Ímpar
    ==> '''))

    num = int(input('Digite um número de 1 a 5: '))

    if player == 1:  # Par
        if (computer + num) % 2 == 0:
            print(f'''\n\033[1;35m
        Você Venceu!
        computador = {computer}
        Jogador = {num}\033[m''')
            victory += 1
        else:
            print(f'''\033[1;31m
        Você Perdeu!
        computador = {computer}
        Jogador = {num} 
            \033[m''')
            break
    elif player == 2:  # Ímpar
        if (computer + num) % 2 != 0:
            print(f'''\033[1;35m
        Você Venceu!
        computador = {computer}
        Jogador = {num}\033[m''')
            victory += 1
        else:
            print(f'''\033[1;31m
        Você Perdeu!
        computador = {computer}
        Jogador = {num}\033[m''')
            break

print(f'''\033[1;34m
    Fim:
Vitórias = {victory}''')
