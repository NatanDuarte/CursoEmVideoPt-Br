"""
Exercício Python 040: Crie um programa que leia duas
notas de um aluno e calcule sua média, mostrando uma
mensagem no final, de acordo com a média atingida:
- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO
"""

print('\033[1;34m_____' * 10)
print('          MÉDIA ')
print('=====' * 10)
n1 = float(input(' Digite a nota da primeira prova: '))
n2 = float(input(' Digite a nota da segunda prova: '))
print('=====' * 10)
if (n2 + n1) / 2 >= 7:
    print(' {}: APROVADO'.format((n2+n1) / 2))
    print('=====' * 10)
elif 5 <= (n2 + n1) / 2 < 7:
    print(' {}: RECUPERAÇÃO'.format((n2+n1) / 2))
    print('=====' * 10)
else:
    print(' {}: REPROVADO'.format((n2+n1) / 2))
    print('=====' * 10)
