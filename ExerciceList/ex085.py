"""Exercício Python 085: Crie um programa onde o usuário possa digitar sete
valores numéricos e cadastre-os em uma lista única que mantenha separados
os valores pares e ímpares. No final, mostre os valores pares e ímpares em
ordem crescente."""

ParesImpares = [[], []]

for c in range(0, 7):
    num = int(input(f'Digite o {c + 1}° número: '))

    if num % 2 == 0:
        ParesImpares[0].append(num)
    else:
        ParesImpares[1].append(num)

print(f'Lista de pares: {sorted(ParesImpares[0])}')
print(f'Lista de impares: {sorted(ParesImpares[1])}')
