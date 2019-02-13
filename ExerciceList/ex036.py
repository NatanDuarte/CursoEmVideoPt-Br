"""Exercício Python 036: Escreva um programa para aprovar o empréstimo
bancário para a compra de uma casa. Pergunte o valor da casa, o salário
do comprador e em quantos anos ele vai pagar. A prestação mensal não pode
exceder 30% do salário ou então o empréstimo será negado."""

print(' I M P R E S T I M O -- B A N C A R I O')
print('====' * 10)
nome = str(input(' Nome: ').strip())
valor = int(input(' Valor do impréstimo: R$'))
salario = int(input(' Salário: R$'))
parcela = int(input(' Tempo para pagar [anos]: '))
print('====' * 10)
if valor / parcela > salario * 30 / 100:
    print(' \033[31;1mNão será possivel efetuar o imprestimo\n'
          ' \033[31;1mSalário insuficiente.')
else:
    print(' Imprestimo efetuado\n'
          ' {}\n'
          ' total: R${:.2f}\n'
          ' em {} anos/{} meses'
          ' '.format(nome, float(valor),
                     parcela, parcela * 12))
