print('AREA DE UMA PAREDE')
h = float(input('Qual a altura [em metros] da parede? '))
larg = float(input('Qual a área [em metros] da parede? '))
a = h * larg
print('Para pintar uma essa parede, de área {} m², serão necessários {} litros de tinta.'.format(a, a/2))
