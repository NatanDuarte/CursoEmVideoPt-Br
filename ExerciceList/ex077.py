"""Exercício Python 077: Crie um programa que tenha uma tupla com várias
palavras (não usar acentos). Depois disso, você deve mostrar, para cada
palavra, quais são as suas vogais."""

frase = ('Aula', 'Tente', 'Levante', 'Persista', 'Projeto', 'Meme', 'Aranhaverso')

for p in frase:
    print(f'\033[1;34m\n{p.upper():<11} tem as vogais:', end=' ')

    for letra in p:
        if letra.lower() in 'aeiou':
            print(f'\033[1;32m{letra}', end=' ')
