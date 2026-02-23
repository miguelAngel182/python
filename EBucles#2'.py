comprobante=True

while comprobante==True:


    n=int(input('Ingrese un número positivo:'))

    if n>0:

        resultado=0
        
        i=1
        
        while i<=n: 
            
            resultado+=(1/i)
            i+=1

        print('El resultado de la serie es:',round(resultado,2))
        
        comprobante=False

    else:
        print('El dato ingresado no es correcto. Ingréselo nuevamente.')