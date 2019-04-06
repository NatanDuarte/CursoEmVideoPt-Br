"""Exercício Python 072: Crie um programa que tenha uma dupla totalmente
preenchida com uma contagem por extenso, de zero até vinte. Seu programa
deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso."""

user = int(0)
number = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove',
          'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete',
          'dezoito', 'dezenove', 'vinte')

while True:
    while True:
        user = int(input('\033[34mDigite um número outro: '))
        if 0 <= user <= 20:
            break
        else:
            print(f'\033[1;31mNúmero inválido, tente novamente:')

    print(f'\033[1;33mVocê digitou o número {number[user]}')

    if number[user] == 'zero':
        print(f'{"Fim":^20}')
        break
