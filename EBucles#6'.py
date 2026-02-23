'''

Escribe un programa que, al recibir como dato un número entero N, obtenga el resultado de la siguiente serie:

1^1-2^2+3^3-...+-N^N

Si el usuario escribe un dato incorrecto, el programa no se ejecutará y le volvera a pedir la información al ususario.

'''

comprobante=True

while comprobante:
    
    n=int(input('Ingrese un número entero positivo:'))
    
    resultado=0
    
    if n>0:
        
        i=1
        
        while i<=n:
                    
            if i%2==0:
                resultado-=i**i

            else:
                resultado+=i**i
                
            i+=1
        
        print('El resultado de la serie es: ', resultado)
        
        comprobante=False
        
    else:
        print('Has ingresado un dato incorrecto. Inténtalo nuevamente.')