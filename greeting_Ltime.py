#Write a Python script that asks the user to enter their name, then waits 3 seconds, and finally prints a personalized greeting with the current time.

import time

def greeting(name):
    time.sleep(3)
    return f"¡Hello, {name}!"

name = input("Enter your name: ").title()
print(greeting(name))