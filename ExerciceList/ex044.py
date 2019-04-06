"""
Exercício Python 044: Elabore um programa que calcule o valor a ser pago
por um produto, considerando o seu preço normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço formal
- 3x ou mais no cartão: 20% de juros
"""

print('  CAIXA')
compra = int(input(' Valor da compra: '))
pag = str(input(' Escolha uma forma de pagamento \n'
                ' [dinheiro] [cartão] \n'
                ' : ').strip())
if pag.upper() == 'DINHEIRO':
    print(' Pagamento em dinheiro, 10% de desconto:')
    print(' Total a pagar: {:.2f}'.format(compra - (compra * 10 / 100)))
elif pag.upper() == 'CARTAO' or pag.upper() == 'CARTÃO':
    cart = int(input('  forma de pagamento \n'
                     '  digite: \n'
                     ' 1 para debito \n'
                     ' 2 para credito \n'
                     ' 3 para cancelar \n'
                     ' : '))
    if cart == 1:
        print('  DÉBITO \n'
              ' 5% de desconto \n'
              ' Total a pagar: {:.2f}'.format(compra - (compra * 5 / 100)))
    elif cart == 2:
        print('  CREDITO')
        prest = int(input(' Digite o número de parcelas: '))
        if prest < 3:
            print(' Total: {:.2f}\n'
                  ' Parcelas: {}\n'
                  ' R$ {:.2f} por parcela'.format(compra, prest, compra / prest))
        else:
            print(' Total: {:.2f}\n'
                  ' Juros de 20%\n'
                  ' Parcelas: {}\n'
                  ' R$ {:.2f} por parcela'.format(compra + compra * 20 / 100,
                                                  prest, (compra + (compra * 20 / 100)) / prest))
    elif cart == 3:
        print(' compra cancelada.')
