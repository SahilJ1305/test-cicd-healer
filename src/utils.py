import os
import json

def add(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return a / b

def multiply(a, b):
    return a * b

def is_even(a):
    return a % 2 == 0

def max_of_two(a, b):
    if a > b:
        return a
    elif a < b:
        return b
    else:
        return a

def greet(name):
    message = "Hello, " + name + "!"
    return message