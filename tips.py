#Append(Agregar un objeto al final de la lista.)

lista=[0,1,2,3,4,5,6,7,8]
lista.append(9)
print(lista)

'''
comentarios de multiples lineas
'''

#1
name=input('Enter your name:')
name=name.strip() #Eliminar los espacios
name=name.title()
print(f'Hello, {name}')

#2
name=input('Enter your name:').strip().title()
first,last=name.split(' ') #Dividir la cadena en el nombre y el apellido
print(f'Hello, {first}')

#Por defecto la funcion input devolverá un string asi le digites un numero. 

#Ordenar lista
List_Numbers = [1,12,67,4,90,35,2,3]
List_Numbers.sort()

print('Lista ordenada = ' , List_Numbers)

#Cuenta las ocurrencias de un caracater especifico de una cadena

texto = 'Muy buenas a todos, damas y caballeros.'
Repeticiones = texto.count('o')

print('El caracter "o" se repite' , Repeticiones , 'veces')

#Divide una cadena en una lista de subcadenas

cadena = 'God Of War'
divison = cadena.split()
print(divison)

#Identificar si una palabra es un palindromo

word = 'radar'
palindromo = word == word[::-1]

print('¿Es palindromo?:',  palindromo)

#Eliminar un elemento de una lista

list = ['Archivo', 'Python', 5, 10.7, True]
print('Antigua lista =', list)

list.remove('Python')
print('Nueva lista =', list)

#Crea una lista que contenga los numeros del 1 al 100

numeros = list(range(1,101))
print(numeros)

#Intercambia los valores de 2 variables con asignacion multiple

a = 1
b = 2
a,b = b,a
print(a,b)

#Realiza operaciones basicas con conjuntos union e interseccion

conjuntoUno = {1,2,3,4}
conjuntoDos = {4,5,3,7}
union = conjuntoUno | conjuntoDos
interseccion = conjuntoUno & conjuntoDos
print('La union es:', union)
print('La interseccion es:', interseccion)
conjuntolet1 = {'a','b','c','d','e','f'}
conjuntolet2 = {'e','f','g','h','i','j'}
UnionLet = conjuntolet1 | conjuntolet2
InterLet = conjuntolet1 & conjuntolet2
print('La union es:', UnionLet)
print('La interseccion es:', InterLet) 
#Al parecer no lo hace en orden.

#Extraer un elemento de una tupla
tupla = (1,2,3,4,5,6,7,8,9,0)
elemento_extraido = tupla[3]
print('El elemento extraido fue:', elemento_extraido)