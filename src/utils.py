import math

def calculate_area(radius):
    if radius < 0:
        return None
    return math.pi * radius ** 2

def print_welcome_message():
    print("Welcome to the Autonomous DevOps Agent!")

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return a / b

def add(a, b):
    return a + b