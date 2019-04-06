"""Exercício Python 070: Crie um programa que leia o nome e
o preço de vários produtos. O programa deverá perguntar se
o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato."""

expensive = int(0)
total = float(0)
cheap = int(100000000000)
goodPrice = str('')

print('\033[1;36mESTATÍSTICAS DE PRODUTO')

while True:
    name = str(input('\033[1;34mNome do produto: ').lower()).strip()
    price = float(input('Preço do produto: '))

    total += price

    if price > 1000:
        expensive += 1

    if price < cheap:
        cheap = price
        goodPrice = name

    new = str(input('Cadastrar outro produto?\n[S/N] > ').upper()).strip()
    print(' ')
    if new == 'N':
        break

print(f'''
A) {total:.2f} é o total gasto na compra
B) {expensive} produto(s) ultrapassa(m) de R$ 1000.00
C) {goodPrice}: o nome do produto mais barato''')
