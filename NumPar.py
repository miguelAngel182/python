#Programa que permite saber si un mumero es par o impar

n = int(input('Ingrese un número para saber si es par o impar: '))

if n / 2 == int(n * 0.5):
    print(n, 'es un número par.')
else:
    print(n, 'es un número impar.')