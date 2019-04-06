""" Exercício Python 049: Refaça o DESAFIO 009, mostrando a tabuada de
um número que o usuário escolher, só que agora utilizando um laço for. """

print('\033[1;34mTABUADA')
x = int(input('Qual tabuada você deseja? '))
for c in range(0, 11):
    print('| {} x {:2} = {:2} |'.format(x, c, x * c))
