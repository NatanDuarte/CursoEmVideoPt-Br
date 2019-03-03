"""Exercício Python 037: Escreva um programa em Python que leia um número
inteiro qualquer e peça para o usuário escolher qual será a base de
conversão: 1 para binário, 2 para octal e 3 para hexadecimal."""

print('\033[1;34m____' * 8)
print(str(' conversor de bases numéricas').upper())
print('____' * 8)
num = int(input('Digite um número inteiro: '))
opcao = int(input('''
    Escolha uma Base para realizar a conversão:
        [1] para BINARIO
        [2] para OCTAL
        [3] para HEXADECIMAL
        [outro numero] para sair
    Sua escolha: 
    >>> '''))
if opcao == 1:
    print('[{}] == [{}]'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('[{}] == [{}]'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('[{}] == [{}]'.format(num, hex(num)[2:]))
else:
    print('Fim da aplicaçao')