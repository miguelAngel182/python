#Crear un programa que permita al usuario escribir texto y devuelva este al revez.

def cadena_invertida(cadena):
    cadena_inversa=cadena[::-1]
    return cadena_inversa

cadena=str(input('Ingresa algo:'))
resultado=cadena_invertida(cadena)
print(resultado)