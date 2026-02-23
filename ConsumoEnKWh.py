#Crear un programa que calcule la cantidad de energia consumida en un determinado tiempo de horas en base al numero de watts del dispositivo.

def calculador_de_consumo(nw,t):
    calculador=round((nw/1000)*t,2)
    print('El consumo durante',t,'horas del dispositivo fue de:', calculador,'KWh.')

nw=float(input('Ingrese aquí el número de W del dispositivo:'))
t=float(input('Ingrese aquí el tiempo en horas:'))
if nw or t==str:
    print('Ingrese un dato válido.')
else:
    consumo_final=calculador_de_consumo(nw,t)


    
    