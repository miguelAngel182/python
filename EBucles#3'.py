comprobante=True

while comprobante==True:

    n=int(input('Ingrese un número entero positivo:'))

    if n>0:
        
        comprobante=False
        
        resultado=1
        
        i=2
        
        while i<=n:
              
            if i%2==0:
                
                resultado= resultado/(1/i)
            
            else:
                resultado=resultado*(1/i)
            
            i+=1
        
        print('El resultado de la serie es:', round(resultado,2))
        
    else:
        print('Dato inválido. Inténtelo de nuevo.')
        

