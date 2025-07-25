import math

# Main program
try:
    number = float(input("Enter a number: "))
    if number < 0:
        print("Cannot compute square root or logarithm for negative numbers.")
    else:
        print("Square root:", math.sqrt(number))
        print("Logarithm:", math.log(number))  # natural log
    print("Sine:", math.sin(number))  # sine in radians
except ValueError:
    print("Please enter a valid number.")
