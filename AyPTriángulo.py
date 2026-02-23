comprobante=True
while comprobante:
        

    def area_y_perimetro(base,altura):
        
        area=(base*altura)/2
        perimetro=(2*base)+(2*altura)
        
        return f'El área del triángulo es: {area}\nY su perímetro es: {perimetro}'

    base=float(input('Ingrese la base del triángulo: '))
    altura=float(input('Ingrese la altura del triángulo: '))
    resultado=area_y_perimetro(base,altura)

    print(resultado)
