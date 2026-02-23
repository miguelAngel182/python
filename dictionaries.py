"""
In Python, dictionaries are data structures that store key-value pairs. Each element in the dictionary has a unique key and an associated value. They are defined using curly braces { }.

What are they for?
- They allow you to store and access data quickly using a key, instead of a numeric index.

Los valores de un diccionario pueden ser de cualquier tipo: cadenas de texto, números, listas, otros diccionarios, booleanos, etc.
"""

# Basic exercises with dictionaries in Python

# ---- > E1: Create a dictionary with names and ages, and allow the user to query the age of a person by entering their name.

# fruits = {
#     "apple": 1200,
#     "banana": 800,
#     "orange": 950,
#     "pear": 1100
# }

# fruit = input("Enter the name of a fruit: ").lower()

# if fruit in fruits:
#     print(f"The price of {fruit} is ${fruits[fruit]}")
# else:
#     print("That fruit is not in the dictionary.")



# ---- > E2: Create a dictionary with names and ages, and allow the user to query the age of a person by entering their name.

# ages = {"Francisco":23, 
#         "María": 14, 
#         "Miguel Ángel": 18,
#         "Luis":43,
#         "Margarita": 89,
#         "Isabel": 19}

# name = input("Enter the name of a person to know their age: ").title() 
# capitalize() converts the first letter to uppercase and the rest to lowercase
# If the name has more than one word, you can use the title() method to capitalize the first letter of each word. The title() method also respects accents present in the name.

# if (name in ages):
#     print(f"The age of {name} is {ages[name]}")
# else:
#     print("Person not registered.")

#E3
# "Crear un diccionario por consola"
# dict = {}
# n = int(input("Number of elements of the dictionary:"))

# for i in range(n):
#     key = input("Enter the key:")
#     value = input("Enter the value:")
#     dict[key] = value

# print(dict)

#E4

country_capitals = {"Colombia": "Bogotá",
                    "United States": "Washington D.C.",
                    "México": "Ciudad de México",
                    "Argentina": "Buenos Aires",
                    "Perú": "Lima",
                    "España": "Madrid"
                    }

country = input("Enter the name of a country: ").title()

if(country in country_capitals):
    print(f"The capital of {country} is {country_capitals[country]}")
else:
    print(f"{country} is not registered.")