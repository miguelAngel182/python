comprobante=True

while comprobante==True:


    n=int(input('Ingrese un número positivo:'))

    if n>0:

        resultado=0

        for i in range(1,n+1):

            resultado+=(1/i)

        print('El resultado de la serie es:',round(resultado,2))
        
        comprobante=False

    else:
        print('El dato ingresado no es correcto. Ingréselo nuevamente.')