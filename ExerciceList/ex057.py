"""Exercício Python 057: Faça um programa que leia o sexo de uma
pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado,
peça a digitação novamente até ter um valor correto."""

print('\n\033[1;34mVALIDAÇÃO DE DADOS')
sexo = str(input('Digite seu sexo [M/F]: ').strip()).upper()

while sexo != 'M' and sexo != 'F':

    sexo = str(input('\n\033[1;31mINVÁLIDO!\nDigite seu sexo [M/F]: \033[m').strip()).upper()

if sexo == 'M':

    print('\n\033[1;34mVocê é do sexo Masculino !')
elif sexo == 'F':

    print('\n\033[1;34mVocê é do sexo Feminino !')
