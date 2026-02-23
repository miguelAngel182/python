#"Programa que calcule la tabla de multiplicar de cualquier número entero dado por el usuario. Debe calcular la tabla desde el 1 hasta el 12."

def calculartabla(n1,n2):
    return str(n1) + 'x' + str(n2) + '=' + str(n1*n2)

n=int(input('Ingrese un número entero:'))
for i in range(1,13):       
    print(calculartabla(n,i))
