"""Exercício Python 080: Crie um programa onde o usuário possa digitar cinco
valores numéricos e cadastre-os em uma lista, já na posição correta de
inserção (sem usar o sort()). No final, mostre a lista ordenada na tela."""

L = list()
new = 0
p = 0

for c in range(0, 5):
    new = int(input('Digite um número: '))

    if c == 0 or new > L[-1]:
        L.append(new)
    else:
        while p < len(L):
            if new <= L[p]:
                L.insert(p, new)
                break

            p += 1

print(L)
