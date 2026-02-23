#Area circulo: π * radio^2
#Longitud circulo: 2 * π * radio

import math

r=float(input('Ingrese el radio de la circunferencia:'))
area=round(math.pi*pow(r,2),3)
longitud=round(math.pi*r*2,3)

print(f'El área de la circunferencia es:{area}')
print(f'La longitud de la circunferencia es: {longitud}')