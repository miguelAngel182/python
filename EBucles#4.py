#Crear un programa que le pregunte al usuario un número determinado de datos a procesar y que luego, en base a este número, le permita ingresar números enteros en base al número que eligió, y que luego muestre la cantidad de números positivos, números negativos y números nulos que hay.

Comprobante=True

while Comprobante==True:
    
    n=int(input('Ingrese un número entero positivo:'))

    if n>0:
        
        números_positivos=0
            
        números_negativos=0
            
        números_nulos=0
        
        for i in range(n):
            
            dato=int(input('Ingrese un número entero:'))
            
            if dato>0:
                números_positivos+=1
            
            elif dato<0:
                números_negativos+=1
                
            else:
                números_nulos+=1
                
        print('Número de datos positivos:',números_positivos, 
                '\nNumero de datos negativos:',números_negativos,
                '\nNúmero de datos nulos:', números_nulos)
        
        Comprobante=False
            
    else:
        print('Dato incorrecto ingresado. Inténtelo nuevamente.')
