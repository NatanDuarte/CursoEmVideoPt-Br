"""Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar [ 2 ] multiplicar [ 3 ] maior [ 4 ] novos números [ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso."""

x = int(input('\033[1;34mDigite um número: '))
y = int(input('Digite outro número: '))

menu = int(input('''___________
MENU PRINCIPAL:
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] Sair
-------------
>>> '''))

if menu == 4:
    print('Digite novos valores')
    x = int(input('Digite um número: '))
    y = int(input('Digite outro número: '))

while menu > 5 and menu > 0 or menu == 4:

    menu = int(input('''\n    ~opção inválida~
    MENU PRINCIPAL:
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] Sair

    >>> '''))

if menu == 1:
    print(f'{x} + {y} = {x + y}')
elif menu == 2:
    print(f'{x} * {y} = {x * y}')
elif menu == 3:
    if x > y:
        print(f'{x} é o maior entre os dois números')
    else:
        print(f'{y} é o maior entre os dois números')
elif menu == 5:
    print('\nFim da aplicação')
