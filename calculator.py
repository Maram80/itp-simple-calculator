
# calculator.py

def add(a, b):
    """Return the sum of a and b."""
    return a + b

def subtract(a, b):
    """Return the difference between a and b."""
    return a - b

def multiply(a, b):
    """Return the product of a and b."""
    return a * b

def divide(a, b):
    """Return the result of dividing a by b. 
    If b is 0, return a string warning about division by zero."""
    if b == 0:
        return "Invalid value for denominator, can't divide by 0!"
    return a / b

import math

def square(x):
    """Return the square of x."""
    return x * x

def power(x, y):
    """Return x raised to the power of y."""
    return x ** y

def sqrt(x):
    """Return the square root of x. 
    If x is negative, return an error message."""
    if x < 0:
        return "Cannot compute the square root of a negative number."
    return math.sqrt(x)

