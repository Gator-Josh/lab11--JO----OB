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
        print("Value Error")
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
        result = b / a
        return result
    except ZeroDivisionError:
        print("division by zero")
def log(a, b):
    try:
        result = math.log(b, a)
        return result
    except ValueError:
        print("Value Error")
def exp(a, b):
    return a**b

