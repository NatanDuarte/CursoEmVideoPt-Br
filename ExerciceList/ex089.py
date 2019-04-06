"""Exercício Python 089: Crie um programa que leia nome e duas notas de vários
alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo
a média de cada um e permita que o usuário possa mostrar as notas de cada aluno
individualmente."""

aluno = []
nome = []
nota = []
dados = []

continuar = str('')

while True:
    nome.append(str(input('\033[1;34mNome: ')))

    for c in range(0, 2):
        nota.append(float(input(f'{c + 1}ª Nota: ')))

    dados.append(nome[:])
    dados.append(nota[:])

    aluno.append(dados[:])

    nome.clear()
    nota.clear()
    dados.clear()

    continuar = input('Continuar? [S/N]: ').strip()
    if continuar.upper() == 'N':
        break

print('')
for c in range(0, len(aluno)):
    print(f'{c}) {aluno[c][0][0]:^10} {"-----":^5} {((aluno[c][1][0] + aluno[c][1][1]) / 2):.1f}')


while True:
    vn = int(input('''
Ver notas de algum aluno?
999 = fim do programa
>>> '''))

    if vn == 999:
        break

    print(f'\n\033[36;1mAs notas de {aluno[vn][0][0].upper()} são {aluno[vn][1][0]:.1f} e {aluno[vn][1][1]:.1f}\033[1;34m')

print('\nFim do programa.')
