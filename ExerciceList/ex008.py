print('CONVERSOR DE UNIDADES')

x = float(input('Informe uma medida em métros: '))

print('[{} Metros] == [{:.0f} Kilometros ]'.format(x, x*(10**3)))
print('[{} Metres] == [{:.0f} Hectometros]'.format(x, x*(10**2)))
print('[{} Metros] == [{:.0f} Decametros ]'.format(x, x*10))
print('[{} Metros] == [{:.3f} Decimetros ]'.format(x, x*(10**-1)))
print('[{} metros] == [{:.3f} Centimetros]'.format(x, x*(10**-2)))
print('[{} Metros] == [{:.3f} Milimetros ]'.format(x, x*(10**-3)))
