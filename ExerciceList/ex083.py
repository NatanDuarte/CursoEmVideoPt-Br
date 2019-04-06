"""Exercício Python 083: Crie um programa onde o usuário digite uma expressão
qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão
passada está com os parênteses abertos e fechados na ordem correta."""

check = []
expression = str(input('Digite a expressão: '))

for c in expression:
    if c == '(':
        check.append(c)
    elif c == ')':
        if len(check) > 0:
            check.pop()
        else:
            check.append(c)

if check == 0:
    print('expressão correta')
else:
    print('expressão incorreta')
