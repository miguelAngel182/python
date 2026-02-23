#Cree un programa que calcule el IVA de una compra, siendo el IVA del 19% sobre el valor total de una compra

def calculodelIVA(p):
    IVA=p*0.19
    return IVA

PrecioCompra=float(input('Ingrese aquí el costo de la compra: '))
IVA=calculodelIVA(PrecioCompra)
print('El precio de la compra es de: ', PrecioCompra)
print('El precio de la compra con el IVA incluido es de: ', PrecioCompra+IVA)