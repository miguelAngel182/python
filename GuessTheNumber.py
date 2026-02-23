#Crear un programa que genere un numero aleatorio y pida al usuario que adivine cual es. Que le diga si su intento es mayor o menor que el numero correcto hasta que lo adivine.

import random

print('Bienvenido(a) a este juego de adivinanzas.')
print('Tendras que adivinar un número.')
print('Si el número es un poco mayor o un poco menor, tendrás que avanzar o retroceder de a 1 unidad.')
print('Si el número es mayor o menor, tendrás que avanzar o retroceder de a 10 unidades.')
print('Si el número es mucho mayor o mucho menor, tendrás que avanzar o retroceder de a 100 unidades.')
print('Empecemos.')

random_n=random.randint(1,999)

while True:
    
    try:
        adivinar_n=int(input('Ingresa un número comprendido entre 1 y 999:'))
        
        if adivinar_n>1:
        
            if 1<=random_n-adivinar_n<=10:
                print('Avanza de a 1 unidad.')
                
            elif -10<=random_n-adivinar_n<0:
                print('Retrocede de a 1 unidad')
            
            elif 10<=random_n-adivinar_n<=100:
                print('Avanza de a 10 unidades.')
                
            elif -100<=random_n-adivinar_n<0:
                print('Retrocede de a 10 unidades')
            
            elif 100<=random_n-adivinar_n<=1000:
                print('Avanza de a 100 unidades.')
                
            elif -1000<=random_n-adivinar_n<0:
                print('Retrocede de a 100 unidades')
            
            elif random_n==adivinar_n:
                print('¡Felicidades, haz adivinado el número!')
                break
        
        else:
            print('Ingresa un número positivo mayor a 0.')
            
    except:
        print('Dato incorrecto.')