#Código optimizado por GitHub Copilot
'''
A group of astronomers wants to develop a program to calculate a person's weight on different celestial bodies.
The program asks for the person's weight on Earth and then calculates their weight on Mars, Jupiter, and the Moon.
To calculate the weight, use the formula: weight = mass * gravity.
The mass is calculated as mass = earth_weight / 9.8.
Gravity values: Mars = 3.711, Jupiter = 24.79, Moon = 1.622.
The program should display the weights on Mars, Jupiter, and the Moon.
'''

def weight_on_celestial_bodies(earth_weight):
    mass = earth_weight / 9.8
    moon_weight = round(mass * 1.622, 4)
    jupiter_weight = round(mass * 24.79, 4)
    mars_weight = round(mass * 3.711, 4)
    return (
        f'Your weight on the Moon is: {moon_weight} kg\n'
        f'Your weight on Jupiter is: {jupiter_weight} kg\n'
        f'Your weight on Mars is: {mars_weight} kg'
    )

def main():
    try:
        earth_weight = float(input('Enter your weight in kilograms: '))
        print()
        result = weight_on_celestial_bodies(earth_weight)
        print(result)
    except ValueError:
        print('Please enter a valid number for your weight.')

if __name__ == '__main__':
    main()