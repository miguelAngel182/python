#Calculador de probabilidad

def probabilidad(a,b):
    division=round(a/b,2)
    return division

x=int(input('Ingrese aqui la cantidad de casos posibles:'))
while (x<0):
    x = int(input('Error. Ingrese nuevamente la cantidad de casos posibles:'))
y=int(input('Ingrese aqui la cantidad de casos totales:'))
while (y<=0):
    y = int(input('Error. Ingrese nuevamente la cantidad de casos totales:'))
print('La probabilidad es de:', probabilidad(x,y))







    


        
