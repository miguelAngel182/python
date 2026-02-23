comprobante=True

while comprobante==True:

    n=int(input('Ingrese un número entero positivo:'))

    if n>0:
        
        comprobante=False
        
        resultado=1
        
        for i in range(2,n+1):
            
            if i%2==0:
                
                resultado= resultado/(1/i)
            
            else:
                resultado=resultado*(1/i)
        
        
    else:
        print('Dato inválido. Inténtelo de nuevo.')