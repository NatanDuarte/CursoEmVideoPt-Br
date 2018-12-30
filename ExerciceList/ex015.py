# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e
# a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

print('-' * 20)
km = float(input('quantos quilometros o csrro alugado percorreu? '))
dia = int(input('Por quantos dias o carro ficou alugado? '))
car = ((km*0.15)+(dia*60))
print('O total é de {:.2f} reais'.format(car))
