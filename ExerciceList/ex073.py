"""Exercício Python 073: Crie uma tupla preenchida com os
20 primeiros colocados da Tabela do Campeonato Brasileiro
de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense."""


team = ('Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo',
         'Atlético-MG', 'Athletico-PR', 'Cruzeiro', 'Botafogo', 'Santos',
         'Bahia', 'Fluminense', 'corinthians', 'Chapecoense', 'Ceará',
         'Vasco', 'Sport', 'América-MG', 'Vitória', 'Parana')


print('Tabela Libertadores - 09/01/2019')
print('5 primeiros colocasdos')
for c in range(0, len(team[:5])):
    print(f'{c + 1:2}°.....{team[c]:<}')

print('\n4 ultimos colocados')
for cont in range(16, len(team)):
    print(f'{cont + 1:2}°.....{team[cont]:<}')

print('\nEm ordem alfabética:')
print(sorted(team))

print('\nPosição da Chapecoense:')
for c in range(0, len(team)):
    if team[c] == 'Chapecoense':
        print(f'{c + 1:2}°.....{team[c]:<}')
