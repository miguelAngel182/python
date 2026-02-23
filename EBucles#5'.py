'''
Construye un programa que, al recibir como datos la altura, el peso y el genero de n personas que pertenecen al estado de un país, obtenga el promedio del peso y el promedio de la altura, tanto de la población masculina como de la población femenina.
'''

comprobante=True

while comprobante==True:

    n=int(input('Ingrese la cantidad de personas a evaluar:'))

    if n>0:
        
        peso_hombres=0
        altura_hombres=0
        peso_mujeres=0
        altura_mujeres=0
        cantidad_hombres=0
        cantidad_mujeres=0
        
        comprobante=False
        
        i=1
        
        while i <=n:
                    
            peso=float(input('Ingrese el peso en Kg:'))
            altura=int(input('Ingrese la altura en cm:'))
        
            comprobante_género=True
            
            while comprobante_género==True:
                
                genero=input('Indique si es de sexo masculino(M) o femenino(F):')
                
            
                if genero.upper()=='M':
                    peso_hombres+=peso
                    altura_hombres+=altura
                    cantidad_hombres+=1
                    
                    comprobante_género=False
                        
                elif genero.upper()=='F':
                    peso_mujeres+=peso
                    altura_mujeres+=altura
                    cantidad_mujeres+=1
                    
                    comprobante_género=False
                    
                else:
                    print('Ha ingresado un género incorrecto. Intentelo nuevamente:')  
                    
                i+=1
                   
        promedio_pesoH=0
        promedio_alturaH=0
        
        if cantidad_hombres>0:
            
            promedio_pesoH=peso_hombres/cantidad_hombres
            promedio_alturaH=altura_hombres/cantidad_hombres
        
        promedio_pesoM=0
        promedio_alturaM=0
        
        if cantidad_mujeres>0:
            
            promedio_pesoM=peso_mujeres/cantidad_mujeres
            promedio_alturaM=altura_mujeres/cantidad_mujeres
        
        print('\nLos resultados obtenidos fueron:'
            '\nEl promedio de peso en hombres fue:', promedio_pesoH,
            '\nEl promedio de peso en mujeres fue:', promedio_pesoM,
            '\nEl promedio de altura en hombres fue:', promedio_alturaH,
            '\nEl promedio de altura en mujeres fue:', promedio_alturaM)
            
    else:
        print('Ha ingresado un dato incorrecto. Inténtelo nuevamente.')

