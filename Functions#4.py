#Crear un programa que permita calcular las ganancias al dia en una tienda de hamburguesas.
def ganancias(NhamburguesasV):
    Hamburguesa = 5000
    return NhamburguesasV * Hamburguesa

Total = str(ganancias(int(input('Ingrese aqui la cantidad de hamburguesas vendidas:'))))
texto = "El valor de sus ganancias el día de hoy fue de: "
print(texto + Total)