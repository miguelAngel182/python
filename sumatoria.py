comprobante = True
while comprobante:

    def sumatoria(n):
        resultado_i = 1
        resultado_n = 1
        s = 0
        for i in range(1, n + 1):
            resultado_i *= i
        for n in range(1, n + 1):
            resultado_n *= n
        for s in range(1, n + 1):
            s += (pow(resultado_i + 1, 2)) / resultado_n
        return s

n = int(input('Ingrese un número entero diferente de cero: '))
resultado = sumatoria(n)
print(resultado)