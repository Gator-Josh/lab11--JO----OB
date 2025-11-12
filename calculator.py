"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math
# First example
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
        raise(ZeroDivisionError)
def log(a, b):
    try:
        result = math.log(b, a)
        return result
    except ValueError:
        print("Value Error")
def exp(a, b):
    return a**b
pass
