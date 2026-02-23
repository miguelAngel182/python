#Programa que permite calcular la tabla de multiplicar de cualquier numero diferente de los numeros negativos y el 0.

repetidor=True

while repetidor==True:
    
    try:

        n=int(input('Ingrese un número entero positivo:'))
        if n <=0:
            print('Dato inválido.')
        elif n>0:  
            for i in range(1,11):
                print(n,'x',i,'=',n*i)
                repetidor=False
                
            print('¿Desea ingresar otro número?\nIngrese 1 para Sí y 2 para No.')
            SoN=int(input(''))
            
            if SoN==1:
                
                repetidor=True
                
            
            elif SoN==2:
                
                print('Gracias por usar la calculadora.')
                
            else:
                
                x=True
                while x:
                    
                    try:
                        
                        print('Opción incorrecta. Intente de nuevo')
                        print('¿Desea ingresar otro número?\nIngrese 1 para Sí y 2 para No.')
                        SoN=int(input(''))
                        
                        if SoN==1:
                            
                            repetidor=True
                            x=False
                            
                        
                        elif SoN==2:
                            
                            print('Gracias por usar la calculadora.')
                            x=False
                    
                    except:
                        print('Dato inválido. Intente de nuevo.')
                        repetidor=False
                        x=True
                    
    except:
        
        print('Dato inválido.')
        repetidor=True