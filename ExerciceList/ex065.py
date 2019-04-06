"""Exercício Python 065: Crie um programa que leia vários números inteiros pelo teclado. No final da execução,
mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao
usuário se ele quer ou não continuar a digitar valores. """

bigger = int(0)
smaller = int(10000000)
c = int(1)
add = int(0)
newNum = str('')

while newNum != 'n':
    num = int(input(f'''\033[1;34m
{c} numbers typed
Enter a number: '''))

    if num > bigger:
        bigger = num

    if num < smaller:
        smaller = num

    c += 1
    add += num

    newNum = str(input('''\033[1;33m
    Continue?  [y/n]
    >>> ''').strip()).lower()

average = float(add / c)

print(f'''
    _____________________________
    |Average:        {average:5.2}
    |Bigger number:  {bigger:5}
    |Smaller number: {smaller:5}
    -----------------------------''')
