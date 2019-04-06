"""Exercício Python 076: Crie um programa que tenha uma tupla única
com nomes de produtos e seus respectivos preços, na sequência. No
final, mostre uma listagem de preços, organizando os dados em forma
tabular."""


l = ('Livro star wars - arquivo rebelde', 69.90, 'Party game Black Stories 2', 39.90,
     'Csneca I Do What I Want', 49.90, 'Camiseta Alura Innovation', 69.90,
     'luminaria de led Estrela', 84.90)


print('\033[1;34m-' * 45)
print(f'{"NERDSTORE":^40}')
print('-' * 45)
for i in range(0, len(l)):
    if i % 2 == 0:
        print(f'{l[i]:.<40}', end='')
    else:
        print(f'{l[i]:.>5.2f}')
print('-' * 45)
