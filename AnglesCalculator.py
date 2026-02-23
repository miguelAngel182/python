#Make a Python calculator to calculate angles in radians and to calculate radians in sine, cosine and tangent.

import math

print('Welcome to the angles and radians calculator.',
          '\nHere you can calculate angles in radians.',
          'Also you can know the value in x angles for sine, cosine and tangent.')

proof=True

while proof==True:

    option=int(input('Press 1 to calculate angles in radians,'
                     '\nor press 2 to calculate angles in sine, cosine and tangent:'))
    
    if option==1:
        
        angles=float(input('Write here the angles you want to calculate in radians:'))

        converter=round(math.radians(angles),3)

        print(angles,'angles are equal to', converter,'radians.')
        
        proof=False
        
               
    elif option==2:
        
        sin_cos_tan=input('Press S to calculate in sine, press C to calculate in cosine and press T calculate in tangent:')
                
        if sin_cos_tan.upper()=='S':
            
            angles=float(input('Write here the angles you want to calculate to sine:'))
            angles_to_radians=math.radians(angles)
            calculatorSin=math.sin(angles_to_radians)
            
            print('The sine of',angles,'angles is:',calculatorSin)
            
            proof=False
            
        
        elif sin_cos_tan.upper()=='C':
            angles=float(input('Write here the angles you want to calculate to cosine:'))
            angles_to_radians=math.radians(angles)
            calculatorCos=math.cos(angles_to_radians)
            
            print('The cosine of',angles,'angles is:',calculatorCos)
            
            proof=False
            
        
        elif sin_cos_tan.upper()=='T':
            angles=float(input('Write here the angles you want to calculate to tangent:'))
            angles_to_radians=math.radians(angles)
            calculatorTan=math.tan(angles_to_radians)
            
            print('The tangent of',angles,'angles is:',calculatorTan)
            
            proof=False
            
        else:
         
            while sin_cos_tan.upper() not in ['S', 'C', 'T']:
                    
                print('Please, write a valid option.')
                sin_cos_tan=input('Press S to calculate in sine, press C to calculate in cosine and press T calculate in tangent:')
                
                if sin_cos_tan.upper()=='S':
                
                    angles=float(input('Write here the angles you want to calculate to sine:'))
                    angles_to_radians=math.radians(angles)
                    calculatorSin=math.sin(angles_to_radians)
                    
                    print('The sine of',angles,'angles is:',calculatorSin)
                    
                    proof=False
                    
            
                elif sin_cos_tan.upper()=='C':
                    angles=float(input('Write here the angles you want to calculate to cosine:'))
                    angles_to_radians=math.radians(angles)
                    calculatorCos=math.cos(angles_to_radians)
                    
                    print('The cosine of',angles,'angles is:',calculatorCos)
                    
                    proof=False
                    
            
                elif sin_cos_tan.upper()=='T':
                    angles=float(input('Write here the angles you want to calculate to tangent:'))
                    angles_to_radians=math.radians(angles)
                    calculatorTan=math.tan(angles_to_radians)
                    
                    print('The tangent of',angles,'angles is:',calculatorTan)
                    
                    proof=False

    else:
        print('Please digit a valid option. ')
        
        

        
        

