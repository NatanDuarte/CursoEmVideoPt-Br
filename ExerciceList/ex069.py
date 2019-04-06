"""Exercício Python 069: Crie um programa que leia a idade e o sexo de
várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar
se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos."""

a = b = c = int(0)

while True:
    print('\033[1;35m ')
    age = int(input('Digite a sua idade: '))
    genre = str(input('Digite seu gênero [M/F]: ').upper())

    if genre == 'M':
        b += 1
    elif genre == 'F' and age > 18:
        a += 1
    elif genre == 'F' and age < 20:
        c += 1

    again = str(input('Cadastrar outro? [S/N] > ').upper())

    if again == 'N':
        break

print(f'''
A) {a} pessoas tem mais de 18 anos.
B) {b} homens foram cadastrados.
C) {c} mulheres tem menos de 20 anos.''')
