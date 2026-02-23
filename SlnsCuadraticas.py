comprobante=True
while comprobante:
        
    a = int(input('Ingrese a: '))
    b = int(input('Ingrese b: '))
    c = int(input('Ingrese c: '))

    primer_término = pow(b, 2)
    segundo_término = 4 * a * c

    if primer_término > segundo_término:
        print('La ecuación tiene 2 soluciones.')
    elif primer_término == segundo_término:
        print('La ecuación tiene 1 solución.')
    else:
        print('La ecuación no tiene solución en el dominio de los números reales.')