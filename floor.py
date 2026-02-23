import math

prove=True

while prove:
    
    try:
        
        Float=float(input('Enter a float value: '))
        
        if Float.is_integer():
            print('Please, enter a float number.')
        else:
            floor=math.floor(Float)
            print(floor)
            prove=False
        
    except ValueError:
        
        print('Please, try it again.')