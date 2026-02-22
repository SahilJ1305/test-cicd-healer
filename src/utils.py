import os
import json

def add(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def greet(name):
    message = "Hello, " + name + "!"
    return message