#Crear un programa que genere un número aleatorio y que le permita al usuario adivinar el número. Si el número es correcto se le dará un premio. Sino, tendrá que volver a intentarlo.
import random
    
print('¡Bienvenido(a), en este juego tendrás que adivinar un número del 1 al 10!')

random_number=random.randint(1,10)

while True:
    
    adivinar_el_número=int(input('Adivina el número:'))
    
    if adivinar_el_número==random_number:
        print('¡Enhorabuena, haz adivinado el número!')
        break    
    else:
        print('Número incorrecto. Inténtalo de nuevo.') 