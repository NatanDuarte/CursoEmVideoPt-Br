"""Exercício Python 034: Escreva um programa que pergunte o salário
de um funcionário e calcule o valor do seu aumento. Para salários
superiores a R$1250,00, calcule um aumento de 10%. Para os
inferiores ou iguais, o aumento é de 15%."""

print('_____' * 8)
sal = int(input('Qual o seu salário? :'))
if sal <= 1250:
    sal = sal + ((sal * 10) / 100)
else:
    sal = sal + ((sal * 15) / 100)
print('Seu novo salario é de R$ {:.2f}'.format(float(sal)))
print('_____' * 8)
