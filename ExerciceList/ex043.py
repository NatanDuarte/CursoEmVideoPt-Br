"""
Exercício Python 043: Desenvolva uma lógica que leia o peso e a altura de
uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status,
de acordo com a tabela abaixo:
- IMC abaixo de 18,5: Abaixo do Peso
- Entre 18,5 e 25: Peso Ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida
"""

print('=====' * 8)
print(' INDICE DE MASSA CORPORAL (IMC)')
print('=====' * 8)
m = int(input(' Digite seu peso: '))
h = float(input(' Digite sua altura: '))
if m/(h**2) > 40:
    print(' Obesidade morbida\n'
          ' procure um médico')
if 30 < m/(h**2) <= 40:
    print(' Obesidade')
if 25 < m/(h**2) <= 30:
    print(' Sobrepeso')
if 18.5 < m/(h**2) <= 25:
    print(' Ideal')
if m/(h**2) <= 18.5:
    print(' Abaixo do peso')
print('=====' * 8)
