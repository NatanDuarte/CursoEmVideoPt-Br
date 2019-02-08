"""Exercício Python 031: Desenvolva um programa que pergunte a distância
de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km
para viagens de até 200Km e R$0,45 parta viagens mais longas."""

print(' Vai viajar? Eu posso calcular o preço da viajem')
dist = int(input('  Quantos Km daqui até seu destino?\n'
                 ': '))

if dist <= 200:
    custo = float(dist * 0.50)
    print(' Sua viajem custará {:.2f} reais.'.format(custo))
else:
    custo = float(dist * 0.45)
    print(' Sua viajem custará {:.2f} reais.'.format(custo))
