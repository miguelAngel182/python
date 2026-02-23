import time

def temporizador(segundos):
    while segundos:
        mins= segundos // 60
        seg= segundos % 60
        tiempo_restante= f'{mins:02d}:{seg:02d}'
        print(tiempo_restante, end='\r')
        time.sleep(1)
        segundos -= 1
    print('¡Tiempo finalizado!')
        
tiempo_ingresado=int(input('Ingresa la cantidad de segundos para el temporizador:'))
temporizador(tiempo_ingresado)
    