"""
Exercício Python 039: Faça um programa que leia o ano de nascimento de um
jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao
serviço militar, se é a hora exata de se alistar ou se já passou do tempo
do alistamento. Seu programa também deverá mostrar o tempo que falta ou
que passou do prazo.
"""

from datetime import date

print(' \033[1;34mALISTAMENTO MILITAR')
print('_____' * 8)
idade = int(input(' Informe o ano do seu nascimento: '))
ano = date.today().year
if idade == ano - 19:
    print(' Este é o seu ano de alistamento\n'
          ' Você tem do primeiro dia útil do mês de janeiro e vai até o último\n'
          ' dia útil de junho para comparecer a junta mais próxima de sua residência')
elif idade > ano - 18:
    print(' Ainda falta {} ano(s) para o seu alistameno'.format(ano - idade))
else:
    print(' Seu prazo para se alistar ja expirou a {} ano(s) se ainda\n'
          ' não se alistou procure a junta mais próxima de sua\n'
          ' residência imediatamente.'.format((ano - 19) - idade))
