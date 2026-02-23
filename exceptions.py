"""
Exception: An event that interrupts the flow of a program.
For example:
ZeroDivisionError, TypeError, ValueError
To handle this, we use:
1. try
2. except
3. finally
"""
# There are many exceptions, but in this code, we are going to work only with these two

def division(n1, n2):
    # Place dangerous code inside try
    try:
        return round(int(n1) / int(n2), 2)
    except ZeroDivisionError:
        return "You can't divide by zero."
    except ValueError:
        return "Please enter only numbers."

n1 = input("Enter a number: ")
n2 = input("Enter a second number: ")
print(division(n1, n2))
