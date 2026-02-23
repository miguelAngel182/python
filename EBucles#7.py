'''

Un número n es un número primo si y solo si sus únicos divisores son 1 y n. Realizar un programa que lea un número n y muestre por pantalla todos los números primos menores a dicho número.

Si el usuario escribe un número incorrecto, el programa no se ejecutará. En cambio, le pedira que vuelva a ingresar el dato hasta que este sea correcto.

'''

n=int(input('Ingrese un número positivo mayor a 0:'))

if n>0:
    
    for i in range(2,n):
        
        creciente=2
        esPrimo=True
        
        while esPrimo and creciente <i:
            
            if i%creciente==0:
                
                esPrimo=False
            
            else:
                
                creciente+=1
        if esPrimo:
            print(i, 'es primo.')
else:
    print('Dato inválido. Inténtelo nuevamente.')