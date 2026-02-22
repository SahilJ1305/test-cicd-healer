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
    else:
        return b

def greet(name):
    message = "Hello"
    return message