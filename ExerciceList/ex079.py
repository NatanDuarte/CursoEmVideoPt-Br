"""Exercício Python 079: Crie um programa onde o usuário possa digitar vários
valores numéricos e cadastre-os em uma lista. Caso o número já exista lá
dentro, ele não será adicionado. No final, serão exibidos todos os valores
únicos digitados, em ordem crescente. """

add = 0
more = ''
num = list()

while True:
    add = int(input('digite um numero: '))

    if add in num:
        print('Valor existente. Nao foi possivel adiciona-lo')

        more = str(input('Continuar [S/N]? '))
        more = more.upper()

        if more == 'N':
            break
    else:
        num.append(add)

        more = str(input('Continuar [S/N]? '))
        more = more.upper()

        if more == 'N':
            break

print(f'Lista final: {sorted(num)}')
