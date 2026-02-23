import math
proof = True

while proof:
    try:
        n = int(input('Enter a integer value greater than or equal to 0: '))
        result = round(math.sqrt(n), 3)
        print('The square root of', n, 'is', result)
        proof = False
    except ValueError:
        print('Please, try it again.') 