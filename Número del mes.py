check=True

def month(n):
    months = {
        1: 'January',
        2: 'February',
        3: 'March',
        4: 'April',
        5: 'May',
        6: 'June',
        7: 'July',
        8: 'August',
        9: 'September',
        10: 'October',
        11: 'November',
        12: 'December'
    }
    return months.get(n, None)

while check:
    try:
        n = int(input('Enter a number to know the corresponding month: '))
        result = month(n)
        if result:
            print('The number', n, 'corresponds to the month of', result)
        else:
            print('Invalid option. Please try again.')
    except:
        print('Only numbers are allowed. Please try again.')