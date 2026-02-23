#Crear un codigo que convierta de minutos a segundos, de dias a horas y de años a meses

#1 minuto = 60 segundos
#1 dia = 24 horas
#1 año = 12 meses

opcion = int(input('MENU\n1. Minutos a segundos \n2. Dias a horas \n3. Años a meses \n'
                      'Ingrese la opcion que desea:'))

if opcion == 1:
    print('')
    minutos = int(input('Ingrese la cantidad de minutos a convertir:'))
    segundos = minutos * 60
    print(minutos, 'minutos equivalen a', segundos, 'segundos.')
elif opcion == 2:
    print('')
    Dias = int(input('Ingrese la cantidad de dias a convertir:'))
    horas = Dias * 24
    print(Dias, 'dias equivalen a', horas, 'horas.')
elif opcion == 3:
    print('')
    años = int(input('Ingrese la cantidad de años a convertir:'))
    meses = años * 12
    print(años, 'años equivalen a', meses, 'meses.')
else:
    print('Ingrese una opcion valida.')
    
    
#Solucion con diccionarios

def Minutos_a_segundos():
    print('')
    Minutos = int(input('Ingrese la cantidad de minutos a convertir:'))
    Segundos = Minutos * 60
    print(Minutos, 'minutos equivalen a', Segundos, 'segundos.')
    
def Dias_a_horas():
    print('')
    Dias = int(input('Ingrese la cantidad dias a convertir:'))
    Horas = Dias * 24
    print(Dias, 'dias equivalen a', Horas, 'horas.')
    
def Años_a_meses():
    print('')
    Años = int(input('Ingrese la cantidad de años a convertir:'))
    Meses = Años * 12
    print(Años, 'años equivalen a', Meses, 'meses.')
    
option = int(input('MENU \n1.Minutos a segundos \n2. Dias a horas \n3. Años a meses \n'
                   'Ingrese la opcion que desea:'))

Dictionary = {1: Minutos_a_segundos, 2: Dias_a_horas, 3: Años_a_meses}

try:
    Dictionary[option]()
except:
    print('Ingrese una opcion valida.')

    