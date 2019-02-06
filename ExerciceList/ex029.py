"""Exercício Python 029: Escreva um programa que leia a velocidade
de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem
dizendo que ele foi multado. A multa vai custar R$7,00 por cada
Km acima do limite."""

from time import sleep

print('---' * 7)
v = int(input('Digite a Velocidade do Carro: '))
print(str('Processando...').upper())

sleep(2)

if v <= 80:
    print('Veículo dentro da velocidade permitida.')
else:
    multa = float((v - 80) * 7)
    print(('    Voceu foi MULTADO por ultrapassar o limite de velocidade.\n'
           '    Por estar trafegando a {1} Km/h,\n'
           '    sua multa é de {:.2f} reais.\n'
           '    ').format(v, multa))
