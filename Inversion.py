#Calcular capital obtenido por inversion.

cost_inv=float(input('¿Cuanto desea invertir?:'))
interes_anual=float(input('¿Cual es el interes anual de la inversion?:'))
num_años=int(input('¿Por cuantos años desea tener el dinero invertido?:'))
capital_obt=round(cost_inv*interes_anual*num_años,2)

print('El capital obtenido con su inversion fue de:', capital_obt)