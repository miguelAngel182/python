#Multiplicación y División: Escribe una función que tome dos números como argumentos y devuelva su multiplicación y división.

def product_and_divison(a,b):
    if b==0:
        print('It is not possible to divide between 0.')
        return None,None
    else:
        product=a*b
        division=a/b
        return product,division

while True:
    a=int(input('Enter a number:'))
    b=int(input('Enter a number:'))
    product,division=product_and_divison(a,b)
    if product is not None and division is not None:
        print('The result of the product is:',product)
        print('The result of the division is:',division)

#2 manera de hacerlo con la excepcion ZeroDivisionError.

def product_and_divison(a, b):
    try:
        product = a * b
        division = a / b
        return product, division
    except ZeroDivisionError:
        print("No es posible dividir entre cero.")
        return None, None

while True:
    a = int(input('Ingrese un número: '))
    b = int(input('Ingrese otro número: '))
    product, division = product_and_divison(a, b)
    if product is not None and division is not None:
        print('El resultado del producto es:', product)
        print('El resultado de la división es:', division)