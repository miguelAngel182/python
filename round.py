#Programa que calcula el imc de una persona.
weight = float(input('Introduce your weight in kilograms: '))
height = float(input('Introduce your height in meters: '))
imc = round(weight/(height)**2,2)
print('Tu indice de masa corportal es:', imc)