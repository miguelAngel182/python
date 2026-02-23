n=int(input('Ingrese un número entero positivo: '))
prime = True

if n%2 == 0:
    print(f'{n} no es primo, ya que es divisible por 2.')
    prime = False
else:
    for i in range(3, n//2, 2):
        if n%i == 0:
            print(f'{n} no es primo, ya que es divisible por ' + str(i) + '.')
            prime = False
            break
        
if prime == True:
    print(f'{n} es primo.')
    
    
