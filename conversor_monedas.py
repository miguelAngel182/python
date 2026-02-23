#Crear una aplicación que convierta valores de una moneda a otra utilizando tasas de conversión predefinidas.

"""
- Puedes definir funciones al principio.
- Las variables usadas como argumentos deben existir en el momento de llamar la función, no cuando se define.
- Lo importante es el orden en que las cosas se ejecutan, no se definen.
"""

def funcion_conversiones(pc, opc):
        if opc == 1:
            dolares = round(0.00024 * pc, 2)
            return f'${pc} pesos colombianos equivalen a ${dolares} dólares'
        elif opc == 2:
            euros = round(0.00021 * pc, 2)
            return f'${pc} pesos colombianos equivalen a ${euros} euros'
        else:
            return "Opción no válida. Debe elegir 1,2 o 3."
        
while True:
    # Entrada de datos
    pc = int(input("Ingrese la cantidad de pesos colombianos a convertir: "))

    if pc < 0:
        print("Ingrese solo valores positivos.")
    else:
        print("---- CONVERSIONES ----\n\n1. Dólares\n2. Euros\n3.Salir")
        opc = int(input("Ingrese su opción: "))
        if opc == 3:
            print("Usted ha salido del programa.")
            break
        resultado = funcion_conversiones(pc, opc)
        print(resultado)