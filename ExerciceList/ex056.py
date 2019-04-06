"""Exercício Python 056: Desenvolva um programa que leia o nome, idade e sexo
de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é
o nome do homem mais velho e quantas mulheres têm menos de 20 anos."""

media = int(0)
mulher = int(0)
homem = str('')
velho = int(0)

for c in range(1, 5):

    print(f'\n {c}ª pessoa')
    nome = str(input('Digite seu nome: ').strip()).upper()
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite seu sexo: ').strip()).upper()

    media += idade

    if sexo == 'MASCULINO':
        if idade > velho:

            velho = idade
            homem = nome

    if sexo == 'FEMININO' and idade < 20:

        mulher += 1

print(f'''      RESULTADO:
    A média da idade dessas pessoas é de {media/4} 
    anos {homem} é o homem mais velho e {mulher} 
    mulheres têm menos de vinte anos.''')
