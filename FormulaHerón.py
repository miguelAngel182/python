from math import sqrt
    
def Area(a,b,c):
    
    try:
        sm=(a+b+c)/2
        area=sm*(sm-a)*(sm-b)*(sm-c)
        raiz=round(sqrt(area),3)
        
        if area>=0:
                
            return f'+++ PROGRMA FÓRMULA HERÓN +++\nEl triángulo con los lados: \na= {a}\nb= {b}\nc= {c}\nTiene un área de: {raiz} m^2'
        
    except ValueError:
                
            return 'Las dimensiones no forman el área de un triángulo.'
        
comprobante=True
while comprobante:
        
    print('+++ PROGRAMA FÓRMULA HERÓN +++')
    a=float(input('Digite el valor de a: '))
    b=float(input('Digite el valor de b: '))
    c=float(input('Digite el valor de c: '))
    print('')
    
    resultado=Area(a,b,c)
    print(resultado)
    print('')
