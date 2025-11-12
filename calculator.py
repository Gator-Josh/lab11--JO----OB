import math
"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
def square_root(a):
    try:
        result = math.sqrt(a)
        return result
    except ValueError:
        raise ValueError
def hypotenuse(a, b):
    return math.hypot(a, b)
def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    try:
        return b / a
    except:
        raise ZeroDivisionError
def log(a, b):
    try:
        result = math.log(b, a)
        return result
    except ValueError:
        raise ValueError
def exp(a, b):
    return a**b
pass
