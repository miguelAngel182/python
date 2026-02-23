#Programa que genera contraseñas aleatorias

import random

minus='abcdefghijklmnopqrstuvwxyz'
mayus=minus.upper()
numeros='0123456789'
simbolos='@\!"#~$%€&¬/()=?¡`^[]+*|´¨ç},.;:-_'
concatenacion=minus+mayus+numeros+simbolos
longitud=12
for _ in range(1):
    muestra=random.sample(concatenacion, longitud)
    password=''.join(muestra)
    print(password)