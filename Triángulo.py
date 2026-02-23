from math import sqrt
        
def medidas_del_triángulo(a,b):
    
    if a>b:
        
        print(f'El mayor cateto es el de medida: {a}')
    
    elif a<b:
        
        print(f'El mayor cateto es el de medida: {b}')
        
    hipotenusa=round(sqrt(pow(a,2)+pow(b,2)),1)
    
    return f'La medida de la hipotenusa es: {hipotenusa}'

a=int(input('Ingrese el valor del primer cateto: '))
b=int(input('Ingrese el valor del segundo cateto: '))
resultado=medidas_del_triángulo(a,b)

print(resultado)       