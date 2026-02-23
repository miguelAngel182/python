import math

prove=True

while prove:
    

    n=int(input('Enter a positive integer value: '))

    if n>=0:
        
        factorial=math.factorial(n)
        print(factorial)
        
        prove=False
        
    else:
        print('Please, try it again.')
        