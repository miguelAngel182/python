check=True

while check:
        
    def quadrant(x, y):
        
        if (x > 0 and y > 0):
            
            quadrant = 'first'
        
        elif x < 0 and y > 0:
            
            quadrant = 'second'
            
            
        elif (x < 0 and y < 0):
            
            quadrant = 'third'

        elif x > 0 and y < 0:
            
            quadrant = 'fourth'
            
        return f'The coordinate {x, y} belongs to the {quadrant} quadrant.'
            
        
    x = float(input('Enter the x point: '))
    y = float(input('Enter the y point: '))
    result = quadrant(x, y)

    print(result)