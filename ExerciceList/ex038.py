"""
Exercício Python 038: Escreva um programa que leia dois números
inteiros e compare-os. mostrando na tela uma mensagem:
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais
"""

x = int(input(' \033[1;33mDigite um número: '))
y = int(input(' \033[1;35mDigite outro número:\033[m '))
if x > y:
    print(' \033[1;34mO primeiro número ({}) é maior que o segundo ({})'.format(x, y))
elif y > x:
    print(' \033[1;34mO Segundo número ({}) é maior que o primeiro ({})'.format(y, x))
else:
    print(' \033[1;34mNão existe valor maior, os dois números são iguais')
