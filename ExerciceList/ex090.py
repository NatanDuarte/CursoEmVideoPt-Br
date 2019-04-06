"""Exercício Python 090: Faça um programa que leia nome e média de um aluno,
guardando também a situação em um dicionário. No final, mostre o conteúdo da
estrutura na tela."""

student = dict()

student['Nome:'] = str(input('\033[1;35mNome: '))
student['Média:'] = float(input('Média: '))

if student['Média:'] >= 7:
    student['Situação:'] = str('Aprovado(a)')
elif 7 > student['Média:'] >= 5:
    student['Situação:'] = str('Em recuperação')
else:
    student['Situação:'] = str('Reprovado(a)')

print('|--------------------------|')

for k, v in student.items():
    print(f'|{k:<10} {v:^15}|')

print('|--------------------------|')
