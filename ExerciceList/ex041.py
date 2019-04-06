"""

Exercício Python 041: A Confederação Nacional de Natação precisa
de um programa que leia o ano de nascimento de um atleta e mostre
sua categoria, de acordo com a idade:

- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JÚNIOR
- Até 25 anos: SÊNIOR
- Acima de 25 anos: MASTER

"""

from datetime import date

print('\033[1;34m____' * 11)
print(' \033[4;34m~~~Confederação Nacional de Natação~~~')
print('\033[1;34m----' * 11)
ano = int(date.today().year)
print('     CADASTRO ')
nome = str(input(' Nome: ').strip())
estado = str(input(' Estado: '))
cidade = str(input(' Cidade: '))
rg = int(input(' Rg(sem espaços ou pontos): '))
nasc = int(input(' Ano de nascimento: '))
if ano - nasc <= 9:
    cate = str('MIRIN')
elif 9 < ano - nasc <= 14:
    cate = str('INFANTIL')
elif 14 < ano - nasc <= 19:
    cate = str('JÚNIOR')
elif 19 < ano - nasc <= 25:
    cate = str('SÊNIOR')
else:
    cate = str('MASTER')
print('____' * 11)
print(' NADADOR REGISTRADO\n'
      ' Nome: {}\n'
      ' Estado: {} Cidade: {}\n'
      ' Rg: {}\n'
      ' Idade: {}\n'
      ' Categoria: {}'.format(nome, estado, cidade, rg, ano - nasc, cate))
