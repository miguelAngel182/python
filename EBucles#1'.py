#Programa que permite calcular la tabla de multiplicar de cualquier numero diferente de los numeros negativos y el 0.

comprobar=True

while comprobar==True:
    
    n=int(input('Ingrese un número entero positivo:'))
    
    if n>0:
        i=1
        
        while i<11:
            print(n,'x',i,'=',n*i)
            i+=1
            comprobar=False
    
    else:
        print('Dato incorrecto ingresado.')