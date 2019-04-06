"""Exercício Python 053: Crie um programa que leia uma frase
qualquer e diga se ela é um palíndromo, desconsiderando os espaços."""

print('\033[1;34m      DETECTOR DE PALÍNDROMOS')
enter = str(input('''   Digite enter para continuar
   ou digite ´ajuda´ para saber
   o que diabos é um palíndromo: ''').strip())

if enter.upper() == 'AJUDA':

    print('''\n\033[1;33m    Palíndromos são palavras ou frases que podem ser lidas 
    da esquerda para a direita ou da direita para a esquerda. Podemos 
    dizer que o palíndromo, comparado à frase comum, é como um bilhete 
    de ida-e-volta. "Ana", por exemplo, é um nome palindrômico.\n''')


frase = str(input('\033[1;34m   Digite uma palavra ou frase: ').strip()).upper()
palavra = ''.join(frase.split())
reverso = ''


for letra in range(len(palavra) - 1, -1, -1):

    reverso += palavra[letra]

# palavra[::-1] para fazer o inverso de uma string sem o FOR

if palavra == reverso:

    print(f'''   O oposto de ´{palavra}´
   é ´{reverso}´
   \033[1;32mÉ UM PALÍNDROMO!''')

else:

    print(f'''   O oposto de ´{palavra}´
   é ´{reverso}´
   \033[1;33mNÃO É UM PALÍNDROMO!''')
