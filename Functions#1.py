#Programa que tome las 3 notas de un alumno y muestre la nota final del curso. Las 2 primeras notas valen 30% cada una y la tercera vale un 40%

def calcularnota(n1,n2,n3):
    return (n1*0.3)+(n2*0.3)+(n3*0.4)

n1=float(input('Ingrese la primera nota:'))
n2=float(input('Ingrese la segunda nota:'))
n3=float(input('Ingrese la tercera nota:'))

NotaFinal=calcularnota(n1,n2,n3)
print('La nota final del estudiante es:', round(NotaFinal,1))