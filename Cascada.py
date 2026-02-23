number = input('Ingrese un numero de 4 digitos:')
if int(number[0]) % 2 == 0:
    if int(number[1]) % 2 == 0:
         if int(number[2]) % 2 == 0:
                 if int(number[3]) % 2 == 0:
                  print('Todos los digitos son pares.')
                 else:
                      print('No todos los digitos son pares.')
         else:
              print('No todos los digitos son pares.')     
    else:
         print('No todos los digitos son pares.') 
else:
     print('No todos los digitos son pares.')